---
type: announcement
title: 'LlamaIndexニュースレター(2026-07): Retrieval HarnessとMCP分割'
title_original: LlamaIndex Newsletter 2026-07-08 (Parse, Extract, Classify, now each with its own MCP)
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- ai-agent
- cost-optimization
components:
- LlamaParse
- LiteParse
- LanceDB
- n8n
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-26-07-08
published_at: '2026-07-08'
---

## 概要

LlamaIndexの月次ニュースレター。LlamaParseがエージェントにlist/grep/read/hybrid retrieveのファイルシステム的ツールを渡すRetrieval Harness、LiteParse v2.1のMarkdown対応、MCPエンドポイントのProduct別分割、Cost Optimizer改善、利用タグによる課金分解などを紹介している。

## 設計のポイント

- エージェントに検索ツールを粒度の細かい操作として渡し、コーパスを辿って検証させる。
- MCPエンドポイントを機能別に分けてツール面を絞り、並列ワークフローを可能にする。
- タグ付きリクエストでチーム別・顧客別のコスト可視化を行う。

## 使いどころ

- 文書エージェントの検索精度を引用付きで上げたいチーム。
- 大量文書処理のコストを部門別に配賦したい企業。
