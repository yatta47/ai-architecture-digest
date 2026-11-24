---
type: case
title: 'NetchexのAskHR: LlamaIndexによるRAG型HR問い合わせ支援'
title_original: 'Case Study: Netchex''s AskHR + Netchex AI with LlamaIndex'
company: Netchex
industry: other
cloud:
- azure
patterns:
- rag
- document-processing
components:
- LlamaIndex
- Azure OpenAI
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/case-study-netchex-more-efficient-hr-operations-with-llamaindex-powered-askhr-netchex-ai
published_at: '2024-09-04'
---

## 概要

給与・人事ソフトのNetchexは、LlamaIndexで従業員ハンドブックや福利厚生資料を取り込み、Azure OpenAIの埋め込みとRAGで回答するAskHR + Netchex AIを構築した。HR部門への問い合わせ負荷を減らし、従業員が自分で答えを得られるようにした。

## 設計のポイント

- MS OfficeやPDFを取り込みパイプラインで処理し、長い規程類をチャンク分割する。
- 検索対象の社内文書に回答を根拠づけ、リトリーバをカスタマイズして関連度を調整する。
- Azure OpenAIの埋め込みをLlamaIndexの統合機能で利用する。

## 使いどころ

- HR担当が少ない中小企業の従業員向け問い合わせ窓口。
- 規程や手引きが多く、検索しにくい社内文書の活用。
