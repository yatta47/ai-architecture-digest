---
type: announcement
title: MCP経由のリモート連携基盤『Integrations』とAdvanced Research
title_original: Claude can now connect to your world
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llm-gateway
components:
- Model Context Protocol (MCP)
- Jira
- Confluence
- Zapier
- Cloudflare
- Intercom
- Google Workspace
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/integrations
published_at: '2025-05-01'
---

## 概要

Anthropicは、ClaudeがリモートMCPサーバー経由で外部アプリ・ツールに接続できる「Integrations」を発表した。あわせてResearch機能を強化し、Web検索・Google Workspace・接続済みIntegrationsを横断して最大45分かけて深く調査し、引用付きの包括的なレポートを生成できるようにした。Jira/Confluence/Zapier/Cloudflareなど10のサービスから提供を開始し、開発者は独自のMCPサーバーも最短30分で構築できる。

## 設計のポイント

- オープン標準のMCP（Model Context Protocol）をローカルのDesktop専用からリモートサーバー対応へ拡張し、Web上のツールをそのまま接続可能にした。
- Researchはリクエストをサブタスクに分解し、各領域を深掘りしてから統合レポートを生成するエージェント型の調査フローを採用している。
- 取り込んだ情報には出典への引用リンクを必ず添付し、回答の検証可能性を担保している。
- Cloudflareのようなホスティングサービスを使うことでOAuth認証やトランスポート処理を作り込まずに独自Integrationsを最短30分で構築できる。

## 使いどころ

- Jira/ConfluenceやZapierなど業務ツールをまたいだタスク管理・自動化をチャット越しに行いたいチーム。
- 営業・マーケティングチームが商談準備や競合調査など数時間かかる調査作業を数分〜数十分に圧縮したい場合。
- Intercomのようなカスタマーサポートツールと連携し、ユーザーフィードバックからバグ起票までを一つの会話で完結させたい運用チーム。
