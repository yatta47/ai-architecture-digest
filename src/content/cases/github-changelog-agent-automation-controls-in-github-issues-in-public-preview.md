---
type: announcement
title: GitHub Issuesにエージェント自動化の承認・信頼度・根拠表示機能が追加
title_original: Agent automation controls in GitHub Issues in public preview
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
- guardrails
components:
- GitHub Issues
- GitHub Agentic Workflows
- Copilot cloud agent
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-07-23-agent-automation-controls-in-github-issues-in-public-preview
published_at: '2026-07-23'
---

## 概要

GitHub Issuesのエージェント自動化に、変更理由の表示・信頼度に応じた自動適用/レビュー保留・承認ワークフローの3機能が追加された。高信頼度の変更は自動適用され、中〜低信頼度の変更はレビュー待ちの提案として保持される。

## 設計のポイント

- エージェントの提案アクションに高/中/低の信頼度を付与し、高信頼度のみ自動適用、それ以外はレビュー待ちにすることで人手の確認範囲を絞る
- ラベル付けやアサインなど各操作に理由(rationale)を記録し、自動適用・保留いずれの場合も監査証跡として残す
- リポジトリ管理者が自動化レベル(信頼度しきい値)を設定でき、少人数で高速に回すか公開リポジトリで慎重にレビューするかを選べる

## 使いどころ

- 公開リポジトリなど誤操作のリスクが高い環境でエージェント自動化を安全に導入したい場合
- IssueのトリアージやメタデータバックフィルをAIに任せつつ監査可能性を確保したいチーム
