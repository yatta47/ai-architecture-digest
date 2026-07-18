# GA4 + BigQuery 分析ガイド

## 1. 目的

本書は、AI Architecture Digest のGA4データをBigQueryで確認・分析するための手順とSQLをまとめる。単にクエリを実行するだけでなく、GA4 Exportの構造、集計単位、費用を抑える方法を理解することを目的とする。

## 2. 現在の構成

| 項目 | 値 |
|---|---|
| 公開サイト | `https://yatta47.github.io/ai-architecture-digest/` |
| GA4測定ID | `G-7XTD8QLYTM` |
| GCPプロジェクト | `life-project-analytics` |
| Export方式 | 日次Export |
| BigQueryデータセット | `analytics_<GA4_PROPERTY_ID>` |
| 日次テーブル | `events_YYYYMMDD` |

`GA4_PROPERTY_ID`は数字のGA4プロパティIDであり、測定IDの`G-7XTD8QLYTM`とは異なる。実際のデータセット名はBigQuery Explorerで確認する。

GA4とBigQueryのリンク設定後、最初のテーブル作成まで24時間程度かかる場合がある。日次テーブルは遅延イベントを反映するため、イベント発生日から最大3日程度更新されることがある。

## 3. クエリ実行前の準備

以降のSQLにある次の部分を、実際の数字のプロパティIDへ置き換える。

```text
analytics_PROPERTY_ID
```

例:

```text
life-project-analytics.analytics_123456789.events_*
```

サンプルSQLの日付は`YYYYMMDD`形式で指定する。まずデータが存在する日付をBigQuery Explorerのテーブル名で確認する。

## 4. GA4 Exportの基本構造

### 4.1 1行は原則として1イベント

`events_YYYYMMDD`には、`page_view`、`session_start`、`first_visit`などのイベントが格納される。

主な列:

| 列 | 内容 |
|---|---|
| `event_date` | プロパティのタイムゾーンに基づく日付 |
| `event_timestamp` | イベント発生時刻。マイクロ秒 |
| `event_name` | `page_view`などのイベント名 |
| `user_pseudo_id` | ブラウザ・デバイス単位の仮名ID |
| `event_params` | イベント固有パラメータの繰り返しレコード |
| `device` | デバイス、OS、ブラウザ情報 |
| `geo` | 国、地域などの地理情報 |
| `traffic_source` | ユーザーを最初に獲得した流入元 |
| `collected_traffic_source` | イベント時点で収集された流入情報 |

### 4.2 `event_params`を取り出す

`page_location`や`ga_session_id`は通常の列ではなく、`event_params`の中に入っている。相関サブクエリまたは`UNNEST`を使って取り出す。

```sql
SELECT
  event_name,
  (
    SELECT value.string_value
    FROM UNNEST(event_params)
    WHERE key = 'page_location'
  ) AS page_location,
  (
    SELECT value.int_value
    FROM UNNEST(event_params)
    WHERE key = 'ga_session_id'
  ) AS ga_session_id
FROM
  `life-project-analytics.analytics_PROPERTY_ID.events_*`
WHERE
  _TABLE_SUFFIX = '20260719'
LIMIT 100;
```

同じパラメータを複数回参照する場合は、先にCTEで列へ展開すると読みやすくなる。

## 5. 基礎クエリ

### 5.1 日別・イベント別の件数

最初に実行する確認用クエリ。

```sql
SELECT
  event_date,
  event_name,
  COUNT(*) AS event_count
FROM
  `life-project-analytics.analytics_PROPERTY_ID.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20260719' AND '20260725'
GROUP BY
  event_date,
  event_name
ORDER BY
  event_date,
  event_count DESC;
```

### 5.2 日別ユーザー数

```sql
SELECT
  event_date,
  COUNT(DISTINCT user_pseudo_id) AS users
FROM
  `life-project-analytics.analytics_PROPERTY_ID.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20260719' AND '20260725'
GROUP BY
  event_date
ORDER BY
  event_date;
```

この値は`user_pseudo_id`が存在するイベントを基にしたデバイス単位の概算である。GA4画面の「アクティブユーザー」とは定義が異なるため、完全一致は期待しない。

### 5.3 ページ別PV

```sql
WITH page_views AS (
  SELECT
    event_date,
    (
      SELECT value.string_value
      FROM UNNEST(event_params)
      WHERE key = 'page_location'
    ) AS page_location,
    (
      SELECT value.string_value
      FROM UNNEST(event_params)
      WHERE key = 'page_title'
    ) AS page_title
  FROM
    `life-project-analytics.analytics_PROPERTY_ID.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN '20260719' AND '20260725'
    AND event_name = 'page_view'
)
SELECT
  page_location,
  ANY_VALUE(page_title) AS page_title,
  COUNT(*) AS page_views
FROM
  page_views
WHERE
  page_location IS NOT NULL
GROUP BY
  page_location
ORDER BY
  page_views DESC;
```

### 5.4 ページパス別PV

クエリ文字列を除き、同じページを一つにまとめる。

```sql
WITH page_views AS (
  SELECT
    REGEXP_EXTRACT(
      (
        SELECT value.string_value
        FROM UNNEST(event_params)
        WHERE key = 'page_location'
      ),
      r'https?://[^/]+([^?#]*)'
    ) AS page_path
  FROM
    `life-project-analytics.analytics_PROPERTY_ID.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN '20260719' AND '20260725'
    AND event_name = 'page_view'
)
SELECT
  page_path,
  COUNT(*) AS page_views
FROM
  page_views
WHERE
  page_path IS NOT NULL
GROUP BY
  page_path
ORDER BY
  page_views DESC;
```

### 5.5 外部サイトからの参照元

```sql
WITH page_views AS (
  SELECT
    (
      SELECT value.string_value
      FROM UNNEST(event_params)
      WHERE key = 'page_referrer'
    ) AS page_referrer
  FROM
    `life-project-analytics.analytics_PROPERTY_ID.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN '20260719' AND '20260725'
    AND event_name = 'page_view'
)
SELECT
  page_referrer,
  COUNT(*) AS page_views
FROM
  page_views
WHERE
  page_referrer IS NOT NULL
  AND page_referrer NOT LIKE 'https://yatta47.github.io/ai-architecture-digest/%'
GROUP BY
  page_referrer
ORDER BY
  page_views DESC;
```

### 5.6 UTM流入

note、Substack、Threads、BlueskyなどにUTM付きリンクを掲載した後に利用する。

```sql
SELECT
  COALESCE(collected_traffic_source.manual_source, '(direct)') AS source,
  COALESCE(collected_traffic_source.manual_medium, '(none)') AS medium,
  COALESCE(collected_traffic_source.manual_campaign_name, '(not set)') AS campaign,
  COUNT(*) AS events,
  COUNT(DISTINCT user_pseudo_id) AS users
FROM
  `life-project-analytics.analytics_PROPERTY_ID.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20260719' AND '20260725'
GROUP BY
  source,
  medium,
  campaign
ORDER BY
  events DESC;
```

`traffic_source`はユーザーの初回獲得情報であり、今回の訪問元を調べる用途とは異なる。個別の投稿やキャンペーンを比較する場合は、`collected_traffic_source`やランディングページのUTMを利用する。

### 5.7 デバイス別ユーザー数

```sql
SELECT
  device.category AS device_category,
  device.operating_system,
  COUNT(DISTINCT user_pseudo_id) AS users,
  COUNTIF(event_name = 'page_view') AS page_views
FROM
  `life-project-analytics.analytics_PROPERTY_ID.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20260719' AND '20260725'
GROUP BY
  device_category,
  operating_system
ORDER BY
  users DESC;
```

## 6. セッション分析

### 6.1 セッションキー

`ga_session_id`は単独ではユーザー間で重複する可能性がある。`user_pseudo_id`と組み合わせてセッションを識別する。

```sql
CONCAT(
  user_pseudo_id,
  '-',
  CAST(ga_session_id AS STRING)
)
```

### 6.2 日別セッション数

```sql
WITH events AS (
  SELECT
    event_date,
    user_pseudo_id,
    (
      SELECT value.int_value
      FROM UNNEST(event_params)
      WHERE key = 'ga_session_id'
    ) AS ga_session_id
  FROM
    `life-project-analytics.analytics_PROPERTY_ID.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN '20260719' AND '20260725'
)
SELECT
  event_date,
  COUNT(DISTINCT CONCAT(
    user_pseudo_id,
    '-',
    CAST(ga_session_id AS STRING)
  )) AS sessions
FROM
  events
WHERE
  user_pseudo_id IS NOT NULL
  AND ga_session_id IS NOT NULL
GROUP BY
  event_date
ORDER BY
  event_date;
```

### 6.3 セッションごとの閲覧ページ数と滞在時間

```sql
WITH events AS (
  SELECT
    user_pseudo_id,
    event_timestamp,
    event_name,
    (
      SELECT value.int_value
      FROM UNNEST(event_params)
      WHERE key = 'ga_session_id'
    ) AS ga_session_id
  FROM
    `life-project-analytics.analytics_PROPERTY_ID.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN '20260719' AND '20260725'
),
sessions AS (
  SELECT
    CONCAT(user_pseudo_id, '-', CAST(ga_session_id AS STRING)) AS session_key,
    COUNTIF(event_name = 'page_view') AS page_views,
    TIMESTAMP_DIFF(
      TIMESTAMP_MICROS(MAX(event_timestamp)),
      TIMESTAMP_MICROS(MIN(event_timestamp)),
      SECOND
    ) AS observed_duration_seconds
  FROM
    events
  WHERE
    user_pseudo_id IS NOT NULL
    AND ga_session_id IS NOT NULL
  GROUP BY
    session_key
)
SELECT
  COUNT(*) AS sessions,
  ROUND(AVG(page_views), 2) AS average_page_views,
  ROUND(AVG(observed_duration_seconds), 2) AS average_observed_duration_seconds
FROM
  sessions;
```

ここで求める時間は、セッション内の最初と最後のイベントの差である。最後のイベント以降に読んでいた時間は含まれないため、GA4の平均エンゲージメント時間とは別の指標として扱う。

## 7. コンテンツ分析

### 7.1 事例詳細ページの閲覧数

```sql
WITH page_views AS (
  SELECT
    REGEXP_EXTRACT(
      (
        SELECT value.string_value
        FROM UNNEST(event_params)
        WHERE key = 'page_location'
      ),
      r'/ai-architecture-digest/cases/([^/?#]+)'
    ) AS case_id
  FROM
    `life-project-analytics.analytics_PROPERTY_ID.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN '20260719' AND '20260725'
    AND event_name = 'page_view'
)
SELECT
  case_id,
  COUNT(*) AS page_views
FROM
  page_views
WHERE
  case_id IS NOT NULL
GROUP BY
  case_id
ORDER BY
  page_views DESC;
```

### 7.2 ファセットページの利用状況

```sql
WITH page_views AS (
  SELECT
    REGEXP_EXTRACT(
      (
        SELECT value.string_value
        FROM UNNEST(event_params)
        WHERE key = 'page_location'
      ),
      r'/ai-architecture-digest/(cloud|patterns|industries|components|companies|outcomes|data-sources)/'
    ) AS facet_type
  FROM
    `life-project-analytics.analytics_PROPERTY_ID.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN '20260719' AND '20260725'
    AND event_name = 'page_view'
)
SELECT
  facet_type,
  COUNT(*) AS page_views
FROM
  page_views
WHERE
  facet_type IS NOT NULL
GROUP BY
  facet_type
ORDER BY
  page_views DESC;
```

現時点ではページビューを基にした分析であり、トップページの種別フィルター操作などは計測していない。必要になった段階でカスタムイベントを追加する。

## 8. 費用を抑えるルール

### 8.1 `_TABLE_SUFFIX`を必ず指定する

ワイルドカードテーブルを使う場合は、対象日を限定する。

```sql
WHERE _TABLE_SUFFIX BETWEEN '20260719' AND '20260725'
```

学習中に全期間を無条件で走査しない。

### 8.2 実行前に処理量を確認する

BigQueryコンソールのクエリエディタには、実行前に推定処理量が表示される。想定より大きい場合は、日付、列、イベント名を絞る。

### 8.3 `SELECT *`を常用しない

構造確認のために少数行を見る場合を除き、必要な列だけを選択する。

```sql
SELECT event_date, event_name
FROM `life-project-analytics.analytics_PROPERTY_ID.events_*`
WHERE _TABLE_SUFFIX = '20260719'
LIMIT 100;
```

### 8.4 保存クエリと集計テーブルを使う

同じ複雑なクエリを繰り返すようになった場合は、保存クエリ、View、日次集計テーブルを検討する。アクセス規模が小さい初期段階では、先にクエリの正しさを確認し、必要になるまで集計基盤を増やさない。

## 9. GA4画面とBigQueryの数値差

GA4画面とBigQueryの値は完全には一致しない場合がある。主な理由は次のとおりである。

- GA4画面ではモデリングやレポート用の処理が適用される場合がある。
- BigQuery Exportは観測された生イベントが中心である。
- GA4の指標と独自SQLで定義した指標が異なる場合がある。
- タイムゾーンが異なると日付境界がずれる。
- 日次テーブルには遅延イベントが後から追加される。
- 同意状態やブラウザの追跡防止により、イベントが送信されない場合がある。

比較するときは、日付範囲、タイムゾーン、データストリーム、イベント除外設定、指標定義をそろえる。

## 10. データ取り扱い

- GA4へ氏名、メールアドレス、その他の個人識別情報を送らない。
- URLやカスタムイベントパラメータに個人情報を含めない。
- BigQueryデータセットの閲覧権限は必要な利用者だけに付与する。
- 公開サイトに計測目的とプライバシーに関する案内を用意する。
- カスタムイベントを追加するときは、収集目的と保存項目を先に定義する。

## 11. SQL学習の順序

1. `event_name`別の件数を確認する。
2. `event_params`から`page_location`を取り出す。
3. 日別、ページ別に`GROUP BY`する。
4. `user_pseudo_id`でユーザーを概算する。
5. `ga_session_id`と組み合わせてセッション化する。
6. UTMを付け、チャネル別流入を比較する。
7. 事例IDやファセットをURLから抽出してコンテンツ分析する。
8. 必要なカスタムイベントをサイトへ追加する。
9. 定期実行やLooker Studioによる可視化を検討する。

## 12. Issue #4の完了条件

- [x] GA4測定タグが公開サイトへ反映されている。
- [x] GA4とBigQueryの日次Exportが設定されている。
- [ ] GA4リアルタイムで`page_view`を確認する。
- [ ] BigQueryに`analytics_<GA4_PROPERTY_ID>`が作成される。
- [ ] `events_YYYYMMDD`が作成される。
- [ ] 日別・イベント別件数のSQLが成功する。
- [ ] `event_params`の`UNNEST`を使ったページ別PVのSQLが成功する。
- [ ] セッション化のSQLが成功する。

## 13. 公式リファレンス

- [GA4 BigQuery Export](https://support.google.com/analytics/answer/9358801)
- [BigQuery Exportの設定](https://support.google.com/analytics/answer/9823238)
- [GA4 BigQuery Exportスキーマ](https://support.google.com/analytics/answer/7029846)
- [GA4とBigQueryの数値を比較する](https://support.google.com/analytics/answer/13578783)
