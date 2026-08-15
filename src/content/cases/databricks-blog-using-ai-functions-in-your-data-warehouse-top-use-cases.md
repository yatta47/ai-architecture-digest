---
type: guidance
title: SQLネイティブなAI Functionsでデータウェアハウス内にAI推論を統合
title_original: Using AI Functions in your Data Warehouse — Top Use Cases
company: Databricks
industry: cross-industry
cloud: []
patterns:
- document-processing
- multilingual-localization
- sql-native-ai
components:
- Databricks AI Functions
- Databricks ai_parse_document
- Databricks ai_extract
- Databricks ai_classify
- Databricks ai_translate
- Databricks ai_query
- Unity Catalog
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/using-aifunctions-your-data-warehouse-top-use-cases
published_at: '2026-08-14'
---

## 概要

Databricksは、SQLクエリ内から直接AIモデルを呼び出せるAI Functions(ai_parse_document、ai_extract、ai_classify、ai_translate、ai_query等)を使い、データウェアハウス内でUnity Catalogのガバナンスを保ったままAI推論を実行するアーキテクチャを紹介する。請求書PDFの構造化抽出、顧客レビューの感情分析、多言語データの正規化、サポートチケットの分類・ルーティング、営業通話の構造化抽出、生成的なメール下書き作成という6つの用途を例示し、外部のOCRサービスやカスタムAIパイプラインを個別構築する複雑さを単一のSQLクエリに集約できるとしている。AI利用料もsystem.billing.usageに標準ウェアハウスコストと並べて計上され、コスト管理も統一される。

## 設計のポイント

- AI推論をUnity Catalogの権限管理下に置くことで、データを外部AI環境へ移動させずにガバナンスを保ったまま推論できる。
- 汎用的なai_queryだけでなく、ai_classify/ai_extract/ai_parse_document/ai_translateなどタスク特化関数を用意し、精度とコストを両立する。
- 並列実行やリトライなどのオーケストレーションをDatabricks側が管理するため、1行でも数百万行でも同じSQLクエリのままスケールする。
- AI利用料をsystem.billing.usageに標準SQLウェアハウスコストと合わせて計上し、ジョブ単位のタグ付けでコスト帰属を明確にする。

## 使いどころ

- PDF請求書や画像などの非構造化ファイルを、カスタムOCRパイプラインなしに構造化テーブルへ変換したいデータチーム。
- サポートチケットや通話録音を自動分類し、担当チームへのルーティングを自動化したいカスタマーサポート部門。
- 多言語で届く顧客レビューを単一言語に正規化してから感情分析や集計を行いたいBI・分析チーム。
- 商談の議事録から次のアクションやリスクフラグを抽出し、営業ダッシュボードに反映したいセールスオペレーション。
