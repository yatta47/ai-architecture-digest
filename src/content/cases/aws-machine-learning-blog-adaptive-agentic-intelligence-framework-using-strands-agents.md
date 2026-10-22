---
type: case
title: 小型モデルでローカル処理し複雑な依頼のみBedrockへ回す適応型エージェント
title_original: Adaptive agentic intelligence framework using Strands Agents
industry: cross-industry
cloud:
- aws
- on-prem
patterns:
- multi-model-routing
- ai-agent
- cost-optimization
components:
- Strands Agents
- Ollama
- Amazon Bedrock
- llama3.2:1b
- llama3.2-vision
- boto3
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/adaptive-agentic-intelligence-framework-using-strands-agents/
published_at: '2026-10-21'
---

## 概要

AAIFは、軽量SLMが依頼を分類し、定型処理はローカルのSLM、複雑な分析はAmazon Bedrockの大型モデルへ振り分ける3層構成のフレームワークである。IoT監視を参考実装として示し、コスト・遅延の抑制とオフライン動作を狙う。

## 設計のポイント

- 1BクラスのSLMをオーケストレーターに据え、固定ルールなしで依頼を分類して経路を決める。
- テレメトリ取得や画像解析などの定型処理はローカルで完結させ、複数ステップの推論が必要な処理だけクラウドへ送る。
- ローカル処理とクラウド処理をそれぞれツールとして定義し、同一エージェントから呼び分ける。

## 使いどころ

- すべての依頼を大型モデルに送ってAPI費用や遅延が膨らんでいるエージェント基盤。
- ネットワーク断でも一部機能を維持したいエッジ・IoT環境。
