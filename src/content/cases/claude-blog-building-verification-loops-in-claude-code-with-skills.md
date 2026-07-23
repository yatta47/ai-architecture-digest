---
type: guidance
title: Claude CodeのSkillsで検証ループを自作する方法
title_original: Building verification loops in Claude Code with skills
industry: cross-industry
cloud: []
patterns:
- ai-agent
- eval
- ci-cd
- spec-driven-development
components:
- Claude Code
- Claude Skills
- GitHub Actions
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/building-verification-loops-in-claude-code-with-skills
published_at: '2026-07-22'
---

## 概要

Claude Codeにおける検証ループは、Claudeが自身の変更をビルド・テスト・観察して修正するイテレーティブな仕組みである。手作業で行っているチェックをSkillとして書き起こし、standalone/embedded/chained/PR連携のいずれかの形でループに組み込むことで、Claudeが自律的にフィードバックループを閉じられるようになる。

## 設計のポイント

- 毎回同じ手直しをしている作業は「新しいチームメイトへの説明」として平易な英語で書き出し、そのままSkillの本文にする
- 定性的でなく決定論的なルール(例: バックフィルなしのカラム削除を拒否する)もSkillとして有効な検証対象になる
- 検証の発火タイミングをstandalone/embedded/chained/PR連携から選び、頻度に応じて常用スキルを埋め込みに昇格させる
- CLAUDE.mdに正確なビルド・テストコマンドを明記し、Claudeが推測せずに済むようにする

## 使いどころ

- 同じ修正指摘を毎回手作業で繰り返しているコードレビュー担当者
- CI/CDパイプラインにClaudeによる自動検証を組み込みたい開発チーム
- プロジェクト固有の暗黙ルールを明文化し新メンバーやAIエージェントに伝えたい場合
