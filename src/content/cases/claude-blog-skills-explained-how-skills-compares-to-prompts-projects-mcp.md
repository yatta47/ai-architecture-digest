---
type: guidance
title: Skills・プロンプト・Projects・サブエージェントの使い分けガイド
title_original: 'Skills explained: How Skills compares to prompts, Projects, MCP, and subagents'
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
components:
- Claude Skills
- Claude Projects
- MCP
- Claude Code
- Claude Agent SDK
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/skills-explained
published_at: '2026-03-05'
---

## 概要

Claudeのエージェント基盤を構成するSkills・プロンプト・Projects・サブエージェントの役割の違いを整理し、それぞれをどんな場面で使い分けるべきかを解説する記事。反復利用する指示はSkillsに、ドメイン固有の永続コンテキストはProjectsに、独立したタスクの切り出しはサブエージェントに担わせるという整理を提示する。

## 設計のポイント

- 反復的なプロンプトは都度書き直すのではなくSkillとして永続化し、progressive disclosureでメタデータのみ先に読み込ませてトークンを節約する
- Projectsは特定ドメインの永続コンテキスト保持に、Skillsは振る舞い方の教示にと役割を分離する
- サブエージェントは独立したツール権限とコンテキストウィンドウを持たせ、メインエージェントの文脈を汚染しない設計にする

## 使いどころ

- 同じ指示を複数の会話で繰り返し使っているチームが、指示をSkill化して再利用性と一貫性を高めたい場合
- 組織のブランドガイドラインやコンプライアンス手順のように、常に適用したいルールをエージェントに持たせたい場合
