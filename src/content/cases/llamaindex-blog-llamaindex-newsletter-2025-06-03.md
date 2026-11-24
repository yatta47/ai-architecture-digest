---
type: announcement
title: 'LlamaIndex: エージェント型検索とGradio MCPハッカソン'
title_original: LlamaIndex Newsletter 2025-06-03
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- ai-agent
- document-processing
components:
- LlamaParse
- OpenAI Responses API
- Claude Sonnet 4
- AWS Titan Multimodal
- Gemini
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-06-03
published_at: '2025-06-03'
---

## 概要

ナイーブなRAGからエージェント型リトルーバルへの進化、OpenAI Responses APIの新機能対応、LlamaParseのSonnet 4対応、12 Factor Agentsガイドを紹介するニュースレター。

## 設計のポイント

- 複数ナレッジベースへのクエリをエージェントが選択するエージェント型検索に移行する
- 構造化出力（配列・enum・文字列制約）を活用して抽出の信頼性を上げる
- マルチモーダル埋め込みを自作して画像とテキストのクエリを統合する

## 使いどころ

- 単純なRAGで精度が頭打ちになった場面
- 複数のデータソースを横断検索したい場面
