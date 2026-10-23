---
type: case
title: Bayer Crop Science のMLワークフロー基盤に載せたマルチエージェント自然言語インターフェース
title_original: How Bayer Crop Science built an agentic decision engine on Amazon Bedrock AgentCore with AWS Unified Operations
company: Bayer Crop Science
industry: other
cloud:
- aws
patterns:
- multi-agent-orchestration
- ai-agent
- human-in-the-loop
components:
- Amazon Bedrock AgentCore
- AgentCore Gateway
- LangGraph
- AWS Unified Operations
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-bayer-crop-science-built-an-agentic-decision-engine-on-amazon-bedrock-agentcore-with-aws-unified-operations/
published_at: '2026-10-23'
---

## 概要

Bayerは育種向けMLワークフロー基盤CDEの上に、スーパーバイザーが専門エージェントへ質問を振り分けるマルチエージェントのADEを構築した。AgentCoreでホスティング・セッション分離・ツールアクセスを任せ、第1フェーズで質問の約8割をエンジニア介在なしで解決している。

## 設計のポイント

- スーパーバイザーエージェントが質問を専門エージェントへルーティングし、各エージェントが該当システムから文脈を取得する構成にしている。
- セッション分離とIAM権限範囲のツールアクセス(AgentCore Gateway)を基盤側に寄せ、認証認可をエージェントコードの外に置いている。
- フレームワーク非依存のランタイムを選び、既存のLangGraphオーケストレーションとモデル選択を持ち込んでいる。
- TAMと生成AI専門エンジニアが週3回の技術スタンドアップで設計判断に伴走する運用体制を取った。

## 使いどころ

- 複数システムに散らばる運用メタデータや実行履歴を横断して説明させたいMLプラットフォーム部門。
- エージェント基盤の運用を自前で抱えず、本番投入まで進めたい企業。
