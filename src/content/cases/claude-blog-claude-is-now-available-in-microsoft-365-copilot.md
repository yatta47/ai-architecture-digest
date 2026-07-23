---
type: announcement
title: Microsoft 365 CopilotへのClaudeモデル統合によるマルチモデル選択
title_original: Claude is now available in Microsoft 365 Copilot
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- multi-model-routing
- ai-agent
- multi-agent-orchestration
components:
- Microsoft 365 Copilot
- Copilot Studio
- Researcher
- Claude Sonnet 4
- Claude Opus 4.1
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-now-available-in-microsoft-365-copilot
published_at: '2025-09-24'
---

## 概要

MicrosoftはMicrosoft 365 CopilotのResearcherエージェントおよびCopilot Studioにおいて、Claude Sonnet 4とClaude Opus 4.1を選択可能なモデルとして追加した。企業ユーザーは既存モデルに加えてClaudeを選び、複雑な多段階リサーチやカスタムエージェント構築に活用できるようになる。AnthropicのモデルはMicrosoft管理外の環境でホストされ、管理者が管理センターで有効化しFrontier Programを通じてオプトインする形で提供される。

## 設計のポイント

- 既存モデルと並列にClaudeを選択肢として追加し、単一ベンダー依存を避けるマルチモデル構成を採用している
- Anthropicモデルは Microsoft管理環境の外でホストし、Anthropic独自の利用規約下で提供することで責任分界を明確化している
- 管理者によるオプトイン(Frontier Program・管理センターでの有効化)を介した段階的ロールアウトにより、企業のガバナンス統制を維持している
- Researcher(推論エージェント)とCopilot Studio(エージェント構築基盤)という2つの利用面にモデル選択を組み込み、用途ごとに最適なモデルを選べるようにしている

## 使いどころ

- 複雑な多段階のリサーチや市場分析・レポート作成を行うビジネスユーザーが、より深い推論力を持つモデルを選んで作業を任せたい場面
- Copilot Studioでエンタープライズ向けのカスタムエージェントやマルチエージェントワークフローを構築する開発者・業務部門
- 特定タスク(深い推論、ワークフロー自動化など)に応じて複数ベンダーのモデルを使い分けたい企業のAI基盤担当者
