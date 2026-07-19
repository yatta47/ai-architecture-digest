---
type: guidance
title: Unity AI Gatewayでモデルプロバイダーを一元登録し、鍵管理とコスト按分を集中統制する
title_original: Meta's Spark Muse 1.1 is now available on Databricks, fully governed by Unity AI Gateway
company: Databricks
industry: cross-industry
cloud:
- multi-cloud
patterns:
- llm-gateway
- multi-model-routing
- policy-as-code
- cost-optimization
components:
- Unity AI Gateway
- Unity Catalog
- Amazon Bedrock
- OpenAI
- Anthropic
- Meta Muse Spark 1.1
outcome:
  type: risk-compliance
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/metas-spark-muse-11-now-available-databricks-fully-governed-unity-ai-gateway
published_at: '2026-07-17'
---

## 概要

DatabricksはUnity AI GatewayにModel Provider Servicesを追加し、Meta Muse Spark 1.1のような新モデルをUnity Catalogへ一度登録するだけで全チームに提供開始日から安全に公開できるようにした。APIキーはカタログ内で暗号化保管されクライアントに直接露出せず、GRANT/REVOKEによる既存の権限モデルでアクセスを統制し、トークン数・レイテンシ・コストを自動計測してチーム単位の予算管理と監査を可能にする。

## 設計のポイント

- モデルプロバイダーをUnity Catalogの一級オブジェクトとして登録し、GRANT/REVOKEという既存の権限モデルをそのまま転用してアクセス制御する
- APIキーはUnity Catalogの接続情報として暗号化保存し、呼び出し側には一切露出させずゲートウェイがリクエスト時に付与する
- 許可済みモデル一覧をゲートウェイ側で強制し、未許可モデルへのリクエストはプロバイダーに届く前に遮断する
- 全リクエストのトークン数・レイテンシ・ステータスコードを既定で計測し、ユーザー/チーム/アプリ単位のコスト按分と監査ログを標準機能として提供する

## 使いどころ

- 新モデルのリリース当日から複数チームに安全に使わせたいプラットフォームチーム
- モデルプロバイダーごとのAPIキー乱立と支出の可視性低下に悩む組織
- モデル利用の監査ログとコスト按分をコンプライアンス要件として残したい規制業種
