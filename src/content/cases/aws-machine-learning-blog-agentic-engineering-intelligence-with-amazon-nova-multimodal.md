---
type: case
title: 部品代替評価を行う航空宇宙向けマルチエージェント技術支援
title_original: Agentic engineering intelligence with Amazon Nova Multimodal Embeddings and Amazon Bedrock AgentCore
industry: manufacturing
cloud:
- aws
patterns:
- multi-agent-orchestration
- rag
- human-in-the-loop
components:
- Amazon Bedrock AgentCore
- Amazon Nova Multimodal Embeddings
- Strands Agents SDK
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/agentic-engineering-intelligence-with-amazon-nova-multimodal-embeddings-and-amazon-bedrock-agentcore/
published_at: '2026-11-02'
---

## 概要

部品の陳腐化や長納期時に、データシート・ICD・認定記録を横断して代替部品の根拠を集めるマルチエージェント支援を紹介する。プランナーが3つの専門エージェントに振り分け、マルチモーダル検索、決定論的な許容差判定、写真比較、Web上のライフサイクル確認を行い、評価書案を作成する。

## 設計のポイント

- 許容差判定はLLMでなくPythonの決定論コードで行い、同じ入力で同じ判定を再現できるようにする。
- エンジニアが最終判断者であり、システムは根拠収集とドラフト作成に徹して承認はしない。
- 図や表を含む資料はマルチモーダル埋め込みで検索し、テキストのみのパイプラインで落ちる情報を拾う。

## 使いどころ

- 安全性が重視される分野で、判断の根拠となる証跡をレビュー可能な形で残したい場合。
- 複数資料の突き合わせに時間を取られている設計・調達部門。
