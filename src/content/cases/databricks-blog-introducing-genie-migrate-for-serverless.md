---
type: announcement
title: Genie Migrate for Serverlessがクラシック計算資源のサーバーレス移行を差分提示で自動化
title_original: Introducing Genie Migrate for Serverless
company: Databricks
industry: cross-industry
cloud:
- multi-cloud
patterns:
- ai-agent
- human-in-the-loop
components:
- Genie Migrate for Serverless
- Databricks Serverless Compute
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/introducing-genie-migrate-serverless
published_at: '2026-11-19'
---

## 概要

Genie Migrate for Serverless(Beta)は、クラシックなワークロードを走査し、計算設定とライブラリをサーバーレス向けに変換する。変更はレビュー可能な差分として示し、30日間ロールバックできる。

## 設計のポイント

- 書き込む前に差分を提示し、移行をレビューと承認の作業にする。
- 不確かなSpark設定は黙って削除せず、人の判断に回す。
- 変更を可逆にし、30日のロールバックを付ける。

## 使いどころ

- 多数のクラシックジョブをサーバーレスへ移したい基盤チーム。
- 移行の試行錯誤の工数を減らしたいとき。
