---
type: case
title: M&Aデューデリジェンスを複数エージェントで並列化するAgentCoreリファレンス構成
title_original: Accelerating M&A due diligence with Amazon Bedrock AgentCore
industry: logistics
cloud:
- aws
patterns:
- multi-agent-orchestration
- rag
- ai-agent
components:
- Amazon Bedrock AgentCore
- Strands Agents SDK
- Amazon Aurora PostgreSQL
- Amazon Quick
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/accelerating-ma-due-diligence-with-amazon-bedrock-agentcore/
published_at: '2026-08-13'
---

## 概要

M&Aデューデリジェンスを、supervisorエージェントが複数の専門エージェント（ターゲットスクリーニング・財務分析など）に処理を振り分けるマルチエージェント構成で高速化するリファレンスアーキテクチャ。自然言語からSQLへの変換によるターゲット探索や、引用付き根拠のガバナンス機構を備え、従来数週間かかっていた分析を数時間に短縮する。

## 設計のポイント

- supervisorエージェントがagents-as-toolsパターンで専門エージェントへタスクをルーティングする
- 全ての主張に引用を紐づけ、citation-checkエバリュエーターで検証することでコンプライアンス部門の監査要求に応える
- 案件ごとの分析結果を共有メモリ層に蓄積し、以降の案件がゼロから調査をやり直さずに済むようにする

## 使いどころ

- 複数の買収候補を並行して評価する必要があるM&Aチーム
- 独自の評価モデルや戦略適合性フレームワークを持ち、既製BIツールでは対応しきれない企業
