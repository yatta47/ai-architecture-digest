---
type: announcement
title: Claudeに専門タスクの手順を持たせるAgent Skills
title_original: Introducing Agent Skills
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
components:
- Claude
- Agent Skills
- Code Execution Tool
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/skills
published_at: '2025-10-16'
---

## 概要

Claudeが必要な時だけ読み込む「Skills」フォルダ（指示・スクリプト・リソース一式）を使って特定タスクに特化できる新機能の発表。Claude apps、Claude Code、APIの全製品で共通のポータブルな形式として利用でき、Box・Canva・Notionなどのパートナーが早期活用を進めている。

## 設計のポイント

- タスクに関連するSkillだけを動的にロードしコンテキストを最小限に保つ
- Skills同士を組み合わせ可能（composable）にし、複数の専門知識を自動的に協調させる
- Code Execution Toolの安全な実行環境上でスキルのコードを動かす

## 使いどころ

- Excelやスプレッドシート操作など特定フォーマットの定型タスクを自動化したい場合
- 組織のブランドガイドラインや業務手順をAIに継続的に守らせたい場合
- 複数プロダクト間でエージェントの振る舞いを再利用・共有したい開発チーム
