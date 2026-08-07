---
type: guidance
title: ユーザー単位でAIトラフィックを制御するAgentCore Gatewayのレート制限機能
title_original: Configure rate limits for AI traffic on AgentCore gateway
industry: cross-industry
cloud:
- aws
patterns:
- llm-gateway
- guardrails
components:
- Amazon Bedrock AgentCore Gateway
- AgentCore Identity
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/configure-rate-limits-for-ai-traffic-on-agentcore-gateway/
published_at: '2026-08-06'
---

## 概要

Amazon Bedrock AgentCore Gatewayに、ユーザー単位でリクエスト数・同時接続数・トークンスループットを制御できるレート制限機能が追加された。ディメンションキー(ターゲット名・ツール名・モデルID・JWTクレームなど)と各エントリの組み合わせでバケットを定義でき、Basic/Advanced/Betaのようなユーザーグループごとに独立したレート制限を適用する例を示している。

## 設計のポイント

- ディメンションキー(targetName等)とJWTクレームを組み合わせ、ターゲット×ユーザーグループごとに独立したレートバケットを作る
- トークンレート制限は呼び出し前に概算で先取りし、実際の入出力トークン数が確定した時点で精算するため、ストリーミング応答でも過剰許可を防ぐ
- 名前指定エントリをワイルドカードより優先させ、高トラフィックターゲットだけ個別の上限を設定し残りはデフォルトで一律に制御する
- 顧客定義のレート制限とサービスクォータを2段階で評価し、まず自社ポリシーで絞ってからアカウント全体の上限を適用する

## 使いどころ

- 複数の権限レベルのユーザーに同じAIゲートウェイを公開し、階層ごとに利用量を差別化したいSaaS/社内プラットフォーム
- 新しいモデルをベータユーザーだけに開放し、本番展開前に性能・適合性を検証したい場合
- ストリーミング推論など長時間接続を占有するリクエストから他ターゲットを守りたい運用チーム
