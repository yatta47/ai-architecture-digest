---
type: case
title: Claude Marketplaceの既存コミットでSnowflake/Vercelを拡張した3社の事例
title_original: How CodeRabbit, Power Digital, and ThoughtSpot scale with Snowflake and Vercel on Claude Marketplace
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-tenant-analytics
- parallel-execution
components:
- Claude Marketplace
- Snowflake
- Snowflake Cortex AI
- Vercel Sandbox
- Vercel Workflows
- Claude
- Spotter
outcome:
  type: speed
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-coderabbit-power-digital-and-thoughtspot-scale-with-snowflake-and-vercel-on-claude-marketplace
published_at: '2026-09-23'
---

## 概要

Claude Marketplaceでは、Anthropicとの利用コミットの一部をSnowflakeやVercelなどの購入に充てられる。Power DigitalとThoughtSpotはSnowflake上でClaudeをデータの近くで動かし、CodeRabbitはVercel SandboxとmicroVM上でエージェントのコードを隔離実行する構成で、承認済み予算により調達を短縮した。この購入方式は限定プレビューである。

## 設計のポイント

- ClaudeをSnowflake内（Cortex AI/推論API）で実行し、データ・ガバナンス・アクセス制御・AIを一つの環境に保つ。
- エージェントが生成・実行するコードはVercel Sandboxの分離されたLinux microVMで動かし、他ジョブや自社システムから切り離す。
- Vercel Workflowsで長時間ジョブの一時停止、再開、完了を管理し、時間制限を回避する。

## 使いどころ

- Anthropicとのコミットを持ち、周辺のデータ基盤や実行基盤を新規予算なしで拡張したい企業。
- 顧客データをSnowflake内に置いたままAI分析を提供したいSaaS事業者。
- AI生成コードを安全な隔離環境で検証・実行したい開発ツール事業者。
