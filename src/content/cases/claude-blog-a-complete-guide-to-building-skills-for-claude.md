---
type: guidance
title: Claudeにワークフローを再利用可能な形で教えるSkills構築ガイド
title_original: A complete guide to building skills for Claude
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- context-engineering
- ai-agent
components:
- Claude
- Claude Code
- MCP
- skill-creator
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/complete-guide-to-building-skills-for-claude
published_at: '2026-01-29'
---

## 概要

AnthropicはClaudeに特定のワークフローを一貫して実行させる「Skills」の構築・テスト・配布方法をまとめたガイドを公開した。単体のSkillだけでなくMCP連携を強化するSkillの設計パターンも扱い、上位2〜3個の自動化したいワークフローが明確であれば15〜30分程度で最初のSkillを作成・検証できるとしている。

## 設計のポイント

- 自動化したい上位2〜3個のワークフローを先に特定してからSkill構造を設計する
- スタンドアロンSkillとMCP連携強化型Skillを用途に応じて使い分ける
- skill-creatorを使って構築からテストまでを短時間で反復する

## 使いどころ

- 特定ワークフローをClaudeに一貫して実行させたい開発者
- MCPコネクタにワークフロー知識を組み込みたいビルダー
- 組織全体でClaudeの操作方法を標準化したいチーム
