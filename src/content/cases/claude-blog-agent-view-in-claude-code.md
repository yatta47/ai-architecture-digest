---
type: announcement
title: Claude Codeの並列エージェント管理UI『Agent View』
title_original: Agent view in Claude Code
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- parallel-execution
- human-in-the-loop
components:
- Claude Code
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/agent-view-in-claude-code
published_at: '2026-05-11'
---

## 概要

Claude Codeに、複数の実行中セッションを一箇所で管理できるAgent Viewが導入された。各セッションが入力待ちか実行中か完了かを一覧表示し、対応が必要なセッションだけをピークして返信でき、フルトランスクリプトへのアタッチやバックグラウンド実行の切り替えも可能。

## 設計のポイント

- セッション一覧に入力待ち/実行中/完了の状態と最新応答を表示し、対応が必要なものだけへ注意を向けられるようにする。
- /bgコマンドや--bgフラグで既存・新規セッションをバックグラウンド化し、ターミナルタブやtmuxグリッドの手動管理を不要にする。
- ピーク機能で最後のターンだけを覗いて即座に返信でき、フルセッションへのアタッチは必要な場合のみ行う設計にする。

## 使いどころ

- 複数のコーディングタスクを並列にエージェントへ投げ、レビュー可能なPRの束として回収したい開発者。
- PRの見守りやダッシュボード更新など長時間ループするエージェントの次回実行タイミングを把握したい運用担当。
- 作業中のセッションから離れず関連タスクや簡単な質問を別セッションで並行処理したい開発者。
