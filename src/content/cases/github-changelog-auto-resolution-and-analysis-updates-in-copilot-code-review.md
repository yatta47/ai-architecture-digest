---
type: announcement
title: Copilotコードレビューがコメント自動解決とエージェントアンサンブルでレビュー精度向上
title_original: Auto-resolution and analysis updates in Copilot code review
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- ci-cd
components:
- GitHub Copilot
- Copilot SDK
outcome:
  type: quality
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-11-auto-resolution-and-analysis-updates-in-copilot-code-review
published_at: '2026-09-11'
---

## 概要

GitHub Copilotのコードレビューが、修正コミットを検知して自動でコメントを解決し、提案適用時にはコミットメッセージも自動生成するようになった。レビュー内部ではCopilot SDKのシェルツール群でビルドやテストを実行して検証し、Liteレベルのレビューは複数エージェントのアンサンブルで実施することでコストを抑えながら重大な指摘の検出率を高めている。

## 設計のポイント

- レビューエージェントに実際のビルド・テスト実行権限を与え、静的な差分読み取りだけでなく実行結果で指摘を裏付ける
- 軽量（Lite）レビューでも単一エージェントではなく複数エージェントのアンサンブルにし、各視点の指摘を統合することで精度とコストを両立する

## 使いどころ

- 大量のPRレビュー負荷を減らしつつ重大な指摘の見逃しを防ぎたい開発チーム
