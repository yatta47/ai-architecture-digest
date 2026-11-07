---
type: announcement
title: Copilotコードレビューの設定API管理とレビュー概要の刷新
title_original: 'Copilot code review: API management and review overview updates'
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- guardrails
- human-in-the-loop
components:
- GitHub Copilot code review
- REST API
- GraphQL API
- MCP
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-11-06-copilot-code-review-api-management-and-review-overview-updates
published_at: '2026-11-07'
---

## 概要

Copilotコードレビューの設定をエンタープライズ/組織/リポジトリ単位でREST・GraphQL APIから管理できるようになった。レビュー概要コメントの簡潔化、👎フィードバック理由の収集、Balancedレビューでの3モデル併用と結果統合なども追加された。

## 設計のポイント

- 設定をエンタープライズ→組織→リポジトリの階層で管理し、上位が管理する設定は下位で上書きできない。
- レビューにeffortレベルと根拠(skills/MCP/カスタム指示)の属性情報を付け、AI出力を識別・追跡可能にする。
- 複数のレビュアーモデルの指摘を別モデルで統合し、失敗時は一度再試行し別モデルへフォールバックする。

## 使いどころ

- 組織全体のAIコードレビュー方針を一括で統制したいプラットフォーム管理者。
- レビュー品質の低下をフィードバックで改善したい開発チーム。
