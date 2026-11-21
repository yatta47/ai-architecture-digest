---
type: case
title: Salesforceの本番変更レビューを24時間から12秒にしたROAMエージェント
title_original: How an AI agent cut production change reviews from 24 hours to 12 seconds
company: Salesforce
industry: other
cloud: []
patterns:
- ai-agent
- decision-execution
- human-in-the-loop
components:
- Agentforce
- Slack
- GitHub
outcome:
  type: speed
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/how-an-ai-agent-cut-production-change-reviews-from-24-hours-to-12-seconds/
published_at: '2026-11-20'
---

## 概要

Salesforceのチームは、18製品の本番変更レビュー(CAB)を自動化するエージェントROAMを作り、中央値の審査時間を約24時間から12秒に短縮した。承認の有無はモデルの解釈ではなく検証済みレコードで判定する決定論的ゲートで確認する。

## 設計のポイント

- 非構造な承認証跡を解釈する部分と、ゲート充足を判定する部分を分離し、判定は検証可能な記録に基づかせる。
- Slackや変更記録などスキーマの異なるデータを統合する際、スキーマ不一致で承認が黙って欠落しないよう検証する。
- CABのフロー図をGitHubに置き、最終承認は人が押す運用を残している。

## 使いどころ

- 承認証跡が複数システムに散らばるリリース審査を自動化したいとき。
- エージェントによる承認判断に監査可能性が求められるとき。
