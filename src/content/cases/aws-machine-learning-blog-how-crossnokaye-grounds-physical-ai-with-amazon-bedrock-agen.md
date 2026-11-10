---
type: case
title: CrossnoKayeの産業プラント向けフィジカルAIエージェントAURA
title_original: How CrossnoKaye grounds physical AI with Amazon Bedrock AgentCore
company: CrossnoKaye
industry: manufacturing
cloud:
- aws
patterns:
- ai-agent
- reasoning-computation-separation
- context-engineering
components:
- Amazon Bedrock AgentCore
- ATLAS
- AURA
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-crossnokaye-grounds-physical-ai-with-amazon-bedrock-agentcore/
published_at: '2026-11-09'
---

## 概要

CrossnoKayeは自社のATLAS基盤上で、プラント全体の状態にアクセスできるエージェントAURAをAgentCoreで構築した。LLMは解釈と計画を担い、統計や物理収支の計算は別処理に任せる。100拠点超で制御アプリがスループット11〜17%向上、エネルギー費用平均21%削減と報告している。

## 設計のポイント

- 単一のセキュリティ境界内でプラント文脈にネイティブにアクセスさせる。
- LLMには計画を、数値計算は決定論的ツールに分担させる。

## 使いどころ

- 産業冷凍や製造の運転最適化
- OT環境のデータ統合型エージェント
