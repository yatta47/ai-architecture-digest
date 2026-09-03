---
type: guidance
title: LangGraphエージェントをAmazon Bedrock AgentCoreへ段階移行する手順
title_original: Migrate agentic workloads to Amazon Bedrock AgentCore
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- unified-runtime
- llmops
components:
- Amazon Bedrock AgentCore
- AgentCore Runtime
- AgentCore Gateway
- AgentCore Memory
- LangGraph
- Strands Agents
- Amazon Bedrock Guardrails
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/migrate-agentic-workloads-to-amazon-bedrock-agentcore/
published_at: '2026-09-03'
---

## 概要

既存のLangGraphカスタマーサポートエージェントを、コード変更を最小限に抑えながらAmazon Bedrock AgentCoreのRuntime/Gateway/Memoryへ段階的に移行する手順を解説する記事。ステージ1でホスティングとツール認証・状態管理を委譲し、ステージ2でモデル駆動のプランニングへ再構築する二段階アプローチを示す。

## 設計のポイント

- グラフ構造を変えずにRuntime/Gateway/Memoryへ1つずつ移行し、変化する変数を最小限に保つ段階的移行
- Gatewayにツール認証を委譲し、独自IAM実行ロールでLambdaターゲットを呼び出すことで認証コードを自前で持たない
- MemorySaverからAgentCoreMemorySessionManagerへ置き換え、ターン・プロセス・日をまたぐ会話状態を永続化する
- 本番投入時にAmazon Bedrock Guardrailsで有害コンテンツフィルタ・根拠検証・プロンプトインジェクション対策を追加する

## 使いどころ

- ノートブックで動くエージェントを本番運用可能な形に持っていきたいチーム
- OSパッチ適用・オートスケーリング・セッション分離などの運用負荷を切り離したい場合
- ハンドメイドの分岐ロジックからモデル駆動プランニングへ移行を検討するチーム
