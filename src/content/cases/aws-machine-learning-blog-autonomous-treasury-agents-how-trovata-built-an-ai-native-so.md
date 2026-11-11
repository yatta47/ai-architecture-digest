---
type: case
title: TrovataがBedrockとAgentCoreで構築した自律的な資金管理エージェント
title_original: 'Autonomous treasury agents: How Trovata built an AI-native solution on Amazon Bedrock and AgentCore'
company: Trovata
industry: financial-services
cloud:
- aws
patterns:
- ai-agent
- guardrails
- human-in-the-loop
components:
- Amazon Bedrock
- Amazon Bedrock AgentCore
- Trovata AI Chat
- Agent Builder-Configurator
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/autonomous-treasury-agents-how-trovata-built-an-ai-native-solution-on-amazon-bedrock-and-agentcore/
published_at: '2026-11-10'
---

## 概要

Trovataは1万超の銀行と接続する資金・流動性管理基盤に、Bedrockによる自然言語照会とAgentCoreによるエージェント実行を組み込んだ。スケジュールやトリガーで動く常駐エージェントが差異説明や異常検知を行い、RBACで銀行ブランド展開を支える。報告された成果は年100万ドル超のコスト削減、TMS費用77%減、レポート作成が1分未満など。

## 設計のポイント

- AIを汎用チャットでなく資金管理の実オブジェクトに結び付ける。
- エージェント構成コンソールで挙動と範囲を管理者が制御する。
- RBACでAI機能の公開範囲を制御する。

## 使いどころ

- 複数銀行のデータを集約する財務部門。
- 銀行が自社ブランドでAI機能を提供する場合。
