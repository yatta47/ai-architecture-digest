---
type: announcement
title: Claude Managed Agentsのセルフホスト型サンドボックスとMCPトンネル機能
title_original: 'Code w/ Claude London 2026: Rethinking how we build'
company: Anthropic
industry: cross-industry
cloud:
- multi-cloud
patterns:
- ai-agent
- llm-gateway
- guardrails
components:
- Claude Managed Agents
- Model Context Protocol
- Claude Platform
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/code-w-claude-london-2026-rethinking-how-we-build
published_at: '2026-05-26'
---

## 概要

Anthropicのカンファレンス「Code w/ Claude London 2026」で発表された、Claude Managed Agentsの新機能を紹介するレポート。セルフホスト型サンドボックス（パブリックベータ）でツール実行環境を自社インフラに置けるようになり、MCPトンネル（リサーチプレビュー）でプライベートMCPサーバーへ公開エンドポイントなしに接続できるようになった。

## 設計のポイント

- エージェントのオーケストレーション・コンテキスト管理はAnthropicのインフラに残しつつ、ツール実行のみを自社管理のサンドボックス（Cloudflare/Daytona/Modal/Vercel等）に分離し、コード・リポジトリを境界の外に出さない
- MCPトンネルは自社側にデプロイした軽量ゲートウェイからのアウトバウンド接続のみで完結させ、インバウンドのファイアウォールルールや公開エンドポイントを不要にする

## 使いどころ

- コード・リポジトリなどの機密データを自社ネットワーク境界の外に出せない企業がエージェント実行環境を導入したい場合
- 社内プライベートネットワークのMCPサーバーに、公開エンドポイントを作らずAIエージェントを接続したい場合
