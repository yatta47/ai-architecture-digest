---
type: announcement
title: ツール呼び出しごとにリスク分類器が判断するClaude Codeの自動権限モード
title_original: Auto mode for Claude Code
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- guardrails
- human-in-the-loop
components:
- Claude Code
- Claude Sonnet 4.6
- Claude Opus 4.6
- Claude Desktop
- VS Code拡張
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/auto-mode
published_at: '2026-03-24'
---

## 概要

Claude Codeに、人間の承認を都度求める従来モードと危険な--dangerously-skip-permissionsの中間となる「auto mode」を追加した。各ツール呼び出しの実行前に分類器がファイル大量削除や機密データ持ち出しなど破壊的行為の兆候を審査し、安全と判断した操作のみ自動実行、危険な操作はブロックしてClaudeに別アプローチを取らせる。ブロックが繰り返されると最終的に人間への確認プロンプトへエスカレーションする。

## 設計のポイント

- 承認を完全にスキップするのではなく、実行前に軽量な分類器がツール呼び出しごとにリスクを審査するプリフライトチェックを挟む
- 安全と判定された操作は自動実行し、リスクありと判定された操作はブロックしてエージェントに別の実行経路を取らせる
- ブロックが繰り返されて行き詰まった場合は人間への確認プロンプトにエスカレーションし、人間参加型のフォールバックを残す
- 組織側は管理設定でauto modeの有効・無効を制御でき、デフォルト無効の面（デスクトップアプリ）と有効化が必要な面を分けて段階的に展開する

## 使いどころ

- 長時間の自律的なコーディングタスクを、逐次承認による中断なしに任せたいチーム
- --dangerously-skip-permissionsほどのリスクは取れないが、承認待ちの頻度を減らして開発速度を上げたい現場
- 組織のセキュリティ方針上、破壊的操作やデータ持ち出しに対するガードレールを維持しつつエージェントの自律度を上げたい管理者
- Team/Enterprise/APIなど複数プランにまたがってエージェント運用の一貫したリスク管理を行いたい組織
