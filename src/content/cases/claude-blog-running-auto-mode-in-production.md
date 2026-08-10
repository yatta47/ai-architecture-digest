---
type: case
title: Nuro・Gusto・Garner HealthにみるClaude Code Auto modeの本番運用
title_original: Running auto mode in production
company: Nuro, Gusto, Garner Health
industry: cross-industry
cloud: []
patterns:
- ai-agent
- defense-in-depth
- guardrails
- human-in-the-loop
components:
- Claude Code
- MCP
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/auto-mode-in-production
published_at: '2026-08-07'
---

## 概要

Nuro・Gusto・Garner Healthの3社が、Claude CodeのAuto modeを本番ワークフローの標準として運用する事例。Nuroは夜通し動く評価指標改善エージェントに、Gustoは連続作業と20分程度の短時間タスクの双方に、Garner Healthは全社的なSDLC高速化にAuto modeを活用し、いずれも手動承認による中断を減らしつつ安全性を担保している。

## 設計のポイント

- Nuroは危険なコマンド（再帰的削除など）を設定ファイルで明示的に拒否した上で、その内側でAuto modeの分類器に判断を委ねる多層防御を採用
- 明確な評価指標がある作業（false negative調査、バイナリのメモリ削減など）はAuto modeで夜間も自律実行させ、他チームに影響するPRレビューなど機微な作業だけ対話モードに切り替える
- GustoはMCPトラフィックをガバナンス済みプロキシ層（ツールガード・プロンプト検査）に通したうえでAuto modeを適用する多層防御構成をとる
- 本番インフラ（Terraform・AWS・実APIへの直接POSTなど）に触れるセッションでは、被害の大きさとのトレードオフを判断してAuto modeから手動承認へ意図的に切り替える

## 使いどころ

- 夜間や並列セッションなど、人が張り付かずに長時間の自律的なエージェント実行をさせたい開発チーム
- MCPサーバー群をまたぐ短時間の定型調査・監査タスクを高頻度に自動化したい運用チーム
- 全社導入したエージェントコーディングツールで、安全性を保ちながら許可プロンプト疲れを解消したい組織
