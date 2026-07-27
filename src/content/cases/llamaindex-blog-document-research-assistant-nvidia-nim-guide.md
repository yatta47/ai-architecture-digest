---
type: case
title: NVIDIA NIMとLlamaIndexで構築するブログ執筆マルチエージェント
title_original: Document Research Assistant for Blog Creation with NVIDIA NIM Microservices
company: NVIDIA
industry: media
cloud: []
patterns:
- multi-agent-orchestration
- rag
- ai-agent
components:
- NVIDIA NIM
- NVIDIA NeMo Retriever
- Llama 3.3 70B Instruct
- LlamaParse
- LlamaIndex Workflows
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/document-research-assistant-for-blog-creation-with-nvidia-nim-microservices
published_at: '2026-07-19'
---

## 概要

NVIDIAとLlamaIndexが共同設計したAIブループリントで、アウトライン作成・質問生成・RAG検索・執筆・レビューを担う5つのエージェントをLlamaIndex Workflowで連携させ、任意のトピックについてブログ記事を自動調査・執筆・推敲するマルチエージェントシステム。NVIDIA NIM上のNeMo RetrieverとLlama3.3-70Bで構成される。

## 設計のポイント

- アウトライン作成→質問生成→RAG検索→執筆→レビューの5エージェントをパイプライン化する
- レビューエージェントが品質不十分と判断した場合、追加質問を生成し最大3回まで書き直しループを回す
- 埋め込み・生成モデルをNVIDIA NIMマイクロサービスとして分離し、ワークステーション/データセンター/クラウドいずれにも配置可能にする

## 使いどころ

- 特定トピックに関する調査レポートやブログ記事を継続的に量産したいメディア/マーケティング用途
- オンプレGPU環境でLLM推論を完結させたいセキュリティ要件の厳しい組織
