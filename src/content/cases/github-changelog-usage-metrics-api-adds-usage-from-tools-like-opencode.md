---
type: announcement
title: Copilot利用メトリクスAPIにクライアント別（OpenCode等）集計を追加
title_original: Usage metrics API adds usage from tools like OpenCode
company: GitHub
industry: cross-industry
cloud: []
patterns:
- llmops
components:
- GitHub Copilot
- Copilot usage metrics API
- OpenCode
- Claude Code
- Codex
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-23-usage-metrics-api-adds-usage-from-tools-like-opencode
published_at: '2026-10-23'
---

## 概要

GitHubのCopilot利用メトリクスAPIに、totals_by_clientが追加された。OpenCodeなどIDE外のツールからのモデルリクエスト数・セッション数・トークン量・モデル別内訳をサーバー側で計測できる。ツール別の利用実態に基づく支援やガバナンスの判断に使える。

## 設計のポイント

- IDEテレメトリに頼らず、サーバー側でリクエストを数えてIDE外ツールの利用の抜けを解消する。
- クライアントは送信された統合IDで識別するため、ベストエフォートの分類として扱う。
- request_countはプロンプト数ではなくモデル呼び出し数である点に注意し、既存フィールドを変えない追加的変更にする。

## 使いどころ

- Copilotを複数のコーディングエージェントのモデル提供元として使う企業のガバナンス担当者。
- ツール別のトークン消費を比較してコストや支援方針を決めたい管理者。
