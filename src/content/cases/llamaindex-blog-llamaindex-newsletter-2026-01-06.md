---
type: announcement
title: ACP連携のエージェントワークフローと文書エージェントテンプレート（LlamaIndexニュースレター 2026-01-06）
title_original: LlamaIndex Newsletter 2026-01-06
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- ai-agent
- document-processing
components:
- LlamaAgents
- Agent Client Protocol
- llamactl
- LlamaParse
- LlamaSheets
- LlamaSplit
- MCP
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2026-01-06
published_at: '2026-01-06'
---

## 概要

Agent Client Protocol統合によりファイルシステム/bashツール、MCPサーバー、永続メモリ、TODO管理を備えたカスタムエージェントを構築できると紹介している。Q&Aから請求書処理までの文書エージェントテンプレートをllamactlでワンコマンドデプロイできる。LlamaSheetsベータとLlamaSplitも告知された。

## 設計のポイント

- ACPでエージェントをエディタ等のクライアントと接続し、ツール・メモリ・TODO追跡を標準構成にする。
- 用途別テンプレート（UI込み）から始め、ワンコマンドでデプロイして立ち上げを短縮する。
- 束ね文書をページ内容で分類・分割してから後続処理に渡す。

## 使いどころ

- 文書処理エージェントを短期間で本番投入したいチーム。
- 請求書処理などの定型文書ワークフローを自動化したい業務部門。
