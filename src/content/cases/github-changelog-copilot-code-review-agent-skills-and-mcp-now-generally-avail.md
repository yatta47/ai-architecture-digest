---
type: announcement
title: GitHub CopilotのコードレビューがエージェントスキルとMCPサーバー連携を正式提供
title_original: 'Copilot code review: Agent skills and MCP now generally available'
industry: cross-industry
cloud: []
patterns:
- ai-agent
- guardrails
components:
- GitHub Copilot
- MCP
outcome:
  type: quality
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-07-29-copilot-code-review-agent-skills-and-mcp-now-generally-available
published_at: '2026-07-29'
---

## 概要

GitHub Copilotのコードレビューが、チーム独自のツールや規約を読み込むエージェントスキル（SKILL.md）と、外部システムからコンテキストを取得するMCPサーバー連携を正式提供した。MCP経由のツール呼び出しは読み取り専用に制限され、どのコメントがスキルやMCPの情報で生成されたか出典が示される。

## 設計のポイント

- レビュー時にMCP経由で行うツール呼び出しを読み取り専用に制限し外部システムへの副作用を防ぐ
- スキルやMCPコンテキストで生成されたレビューコメントに出典を明示しレビューの説明可能性を確保する
- Copilot cloud agent向けに既に設定済みのMCP構成をコードレビュー側にも自動で流用する

## 使いどころ

- 社内のコーディング規約やIssueトラッカーの情報をレビューに反映させたい開発組織
- レビューコメントの根拠を追跡可能にしたいチーム
- 既存のMCP接続資産をコードレビューにも再利用したい組織
