---
type: opinion
title: 大規模コード移行のエージェントでは検証が主課題
title_original: When AI rewrites millions of lines of code, verification becomes the bottleneck
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- spec-driven-development
- human-in-the-loop
components:
- Rust
- formal verification
outcome:
  type: quality
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://commandline.microsoft.com/agentic-software-engineering-large-scale-code-migration-language-modernization-spec-driven-development/
published_at: '2026-10-26'
---

## 概要

Microsoftは、WindowsやAzureの巨大コードベースを変換するAIエージェントで、コード生成が容易になる一方、信頼できる検証が課題になると述べる。静的解析・テスト・形式検証をエージェントのツールとして提供し、人の注意を重要箇所に使う。

## 設計のポイント

- 固定ワークフローからエージェントが計画する方式へ移行し、検証ツールの整備に注力する。
- 形式検証をツール化して変更の正しさを確認する。
- 人の注意を希少資源として設計する。

## 使いどころ

- 大規模コード移行やRust化を検討する組織。
- AI生成コードを信頼する仕組みが必要なとき。
