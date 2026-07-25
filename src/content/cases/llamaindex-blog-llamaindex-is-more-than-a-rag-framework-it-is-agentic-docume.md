---
type: opinion
title: LlamaIndexはRAGフレームワークから『エージェント型文書処理基盤』企業へ舵を切った
title_original: LlamaIndex Is More Than a RAG Framework, It Is Agentic Document Infrastructure
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- document-processing
- ai-agent
- context-engineering
components:
- LlamaParse
- Claude Code
- MCP
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-is-more-than-a-rag-framework
published_at: '2026-07-19'
---

## 概要

LlamaIndexは2022年末にRAG向けオープンソースフレームワークとして立ち上がったが、Skills/MCPやコーディングエージェントの台頭でフレームワーク的抽象化の価値が薄れる一方、企業の知識の大半がPDF/PowerPoint/Word/Excelに閉じ込められたままである『文書理解』の課題は解決されていないと指摘し、自社の軸足をRAGフレームワークから高品質なOCR・抽出・ワークフローを提供する文書インフラ企業へ移したと説明する。

## 設計のポイント

- フロンティアVLMにページのスクリーンショットを渡すだけの一発解析は、密な表・手書きフォームの精度やコストの面で実運用には不十分と判断した
- エージェントのツール利用がSkills/MCPで標準化されたことで、フレームワーク統合よりも高品質な文書理解レイヤーの提供に価値が移ったと再定義した
- 『Files Are All You Need』の知見から、適切なファイルシステムツールを与えればエージェントの動的検索が従来のチャンク化・インデックス化より有効になり得ると位置づけた

## 使いどころ

- 汎用LLMフレームワークへの投資判断を見直したいプラットフォームチーム
- エージェントに企業文書を読ませる基盤を『フレームワーク』でなく『専用インフラ』として検討したい組織
