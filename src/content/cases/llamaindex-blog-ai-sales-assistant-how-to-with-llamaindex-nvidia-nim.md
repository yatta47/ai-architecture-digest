---
type: case
title: LlamaIndexとNVIDIA NIMで作る営業向け社内AIアシスタント
title_original: Building an AI Sales Assistant with LlamaIndex and NVIDIA NIM
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- rag
- ai-agent
- inference-optimization
components:
- LlamaIndex
- LlamaIndex Workflows
- NVIDIA NIM
- Chainlit
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/case-study-building-an-ai-sales-assistant-with-llamaindex-and-nvidia-nim
published_at: '2024-10-25'
---

## 概要

NVIDIAが自社の営業担当向けに、LlamaIndex Workflowsと推論マイクロサービスのNVIDIA NIMでAIアシスタントを構築した事例。RAGによる社内情報の検索に加え、翻訳やメール草案などRAGを使わない依頼も同じパイプラインで扱い、UIはChainlitで作った。

## 設計のポイント

- RAGの質問とそれ以外の依頼を同一のパイプラインで処理し、用途ごとに別アプリにしない。
- 取得と応答の処理をLlamaIndex Workflowsで制御し、機能追加をしやすくしている。
- LLM推論をNIMのマイクロサービスとして切り出し、低遅延でスケールできるようにしている。

## 使いどころ

- 社内文書や製品情報を素早く引きたい営業・サポート組織。
- 検索と文章生成を一つの対話窓口にまとめたい場合。
