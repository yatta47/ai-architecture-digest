---
type: case
title: 海洋整備士向けRAGチャットボット「OilyRAGs」
title_original: 'OilyRAGs: Building a RAG-powered mechanic assistant'
industry: other
cloud: []
patterns:
- rag
- ai-agent
- multi-agent-orchestration
components:
- LlamaIndex
- Pinecone
- OpenAI
- Arize Phoenix
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/oilyrags-building-a-rag-powered-mechanic-assistant-with-ai
published_at: '2026-07-27'
---

## 概要

ボート整備士向けに、エンジン型式番号から部品情報を検索できるRAGチャットボットをLlamaIndexとPineconeで構築したハッカソン発プロトタイプ。整備士がボートを降りずスマートフォンから質問でき、作業内容がデジタルフォームとして記録される。

## 設計のポイント

- LlamaIndexのRAGパイプラインとワークフローを用い、検索エージェントが結果をレポート生成エージェントに引き渡す2段構成にする
- 整備士が現場でハンズフリーに使えるよう、スマートフォンからの入力に対応するマルチモーダルなインターフェースを想定する
- Arize Phoenix(LlamaTrace)で本番運用を見据えたトレース・可観測性を組み込む

## 使いどころ

- 型式番号や仕様書の照合作業に時間がかかる現場整備・保守業務の効率化
- 紙の手順書やPDFマニュアルをRAG化し、ハンズフリーで参照したい現場作業者向けアプリ
