---
type: announcement
title: Claude Codeのプロジェクトをフォルダから会話型オーケストレーションへ刷新
title_original: 'Projects redesigned: from folder to conversation'
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- memory-consolidation
components:
- Claude Code
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/projects-redesigned
published_at: '2026-09-17'
---

## 概要

Claude Codeのプロジェクトが刷新され、目標を伝えるとコーディネーターがスコープを決めてスレッドに作業を委譲し、並行して進む複数スレッドの出力をレビュー・統合するようになった。各スレッドはクラウド上の独立したClaude Codeセッションとしてブランチとリポジトリのコピー上で動作する。

## 設計のポイント

- コーディネーターが目標を各リポジトリ・各タスク向けのスレッドに委譲し進捗を横断的に管理する構成にした
- 各スレッドはクラウド上の独立したClaude Codeセッションとして自分のブランチとコピー上で作業する
- スレッド間で共有されるメモリが時間とともに蓄積されリリース日程や過去の意思決定を都度説明せずに済むようにした
- スレッド同士が同じコードに触れた場合は通常のPRと同じマージコンフリクトとして解消する設計にした

## 使いどころ

- 複数リポジトリにまたがる大きな移行作業（例: 非推奨APIの廃止）を並行スレッドに分割したいチーム
- セッションのハンドオフや結果の統合を手作業で行っていた複数セッション運用
- 外出先からでも進行中の複数スレッドを確認・指示したい場合
