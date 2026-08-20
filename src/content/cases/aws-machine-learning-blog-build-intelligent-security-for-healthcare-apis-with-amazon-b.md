---
type: guidance
title: Amazon Bedrockで実現するFHIR APIの振る舞いベースセキュリティ監視
title_original: Build intelligent security for healthcare APIs with Amazon Bedrock
industry: healthcare
cloud:
- aws
patterns:
- guardrails
- anomaly-detection
components:
- Amazon Bedrock
- AWS Lambda
- Amazon API Gateway
- AWS HealthLake
- Amazon EventBridge
- Amazon Cognito
- Amazon Bedrock Guardrails
- Amazon Comprehend Medical
- Amazon DynamoDB
- Amazon CloudWatch
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-intelligent-security-for-healthcare-apis-with-amazon-bedrock/
published_at: '2026-08-20'
---

## 概要

FHIR APIの静的なアクセス制御ルールは臨床ワークフローの変化に追随できず維持コストも高いという課題に対し、Amazon BedrockのFMを使ってアクセスパターンの異常検知・データ機微度の自動分類・自然言語のコンプライアンスレポート生成を行うアーキテクチャを示す。セキュリティ監視をFHIR APIのリクエストパスから分離し非同期で処理することで、レイテンシに影響を与えずに継続的な監視を実現する。

## 設計のポイント

- セキュリティ分析をAmazon EventBridge経由の非同期処理として本流のFHIRリクエストパスから切り離し、分析基盤が落ちてもAPIは通常どおり応答を続ける
- Amazon Bedrock GuardrailsとAmazon Comprehend Medicalを多層で組み合わせ、プロンプト・応答・監査ログのそれぞれでPHIを匿名化/redactする
- 生のIPアドレスをモデルに渡さず内部/外部の分類のみ渡す、アラート通知にはハッシュ化した参照IDのみを含めるなど、機微情報が経路上に漏れないよう最小化する
- Structured OutputsでJSONスキーマとenum制約付きフィールドを使い、モデル応答の形式を予測可能にして下流処理での不測のPHI露出を減らす

## 使いどころ

- HIPAA等の規制下でFHIR APIを運用しており、静的ルールだけでは検知できないアクセス異常を捉えたい医療機関・ベンダー
- アクセス制御は既存のRBAC/JWT認可のまま維持しつつ、振る舞いベースの追加監視レイヤーを後付けしたいチーム
- 監査証跡やコンプライアンスレポート作成にかかる手作業を減らしたいセキュリティ・コンプライアンス担当
