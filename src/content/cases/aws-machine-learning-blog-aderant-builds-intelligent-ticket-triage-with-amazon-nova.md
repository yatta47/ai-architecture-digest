---
type: case
title: Amazon Nova Liteによるサポートチケットの自動トリアージ
title_original: Aderant builds intelligent ticket triage with Amazon Nova
company: Aderant
industry: other
cloud:
- aws
patterns:
- ai-agent
- event-driven
- human-in-the-loop
- cost-optimization
components:
- Amazon Nova Lite
- Amazon Bedrock Converse API
- AWS Lambda
- Amazon EventBridge
- Amazon Athena
- Amazon DynamoDB
- Amazon CloudWatch
- AWS Secrets Manager
- Jira
- Confluence
- Microsoft SharePoint
- Microsoft Teams
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/aderant-builds-intelligent-ticket-triage-with-amazon-nova/
published_at: '2026-09-24'
---

## 概要

法務業界向けソフトウェアのAderantが、EventBridgeで毎時起動するLambdaとNova Liteで、未割当チケットの文脈収集・分類・振り分けを自動化した事例。初期2.5週で109件を約96%の精度で振り分け、週8〜14時間を削減し、月額コストは30ドル未満に収まった。

## 設計のポイント

- Identify/Enrich/Classify/Act/Observeの5段階を単一Lambdaのサーバーレスワークフローとして構成する。
- Jira・Confluence・Athenaなど複数ソースの文脈を集めてからNovaに構造化分類させ、根拠のある推奨を出す。
- 信頼度が閾値以上のみ自律実行し、低信頼は人手レビューに回して統制を保つ。
- 実チケットで複数モデルを比較し、コスト効率の高い軽量モデルを選ぶ。

## 使いどころ

- 少人数の運用チームで、チケット調査に毎回15〜25分かかる負担を減らしたい場合。
- ミスルーティングや経験差による判断のばらつきを抑えたい場合。
- 低コストでAIによる運用自動化を始めたいAWS利用組織。
