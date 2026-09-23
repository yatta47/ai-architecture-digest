---
type: guidance
title: Claude Codeでの1タスク当たりコストをターン数・キャッシュ・出力で見積もる手引き
title_original: What a task costs on Opus 5.5
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- cost-optimization
- context-engineering
- ai-agent
components:
- Claude Opus 5.5
- Claude Code
outcome:
  type: cost
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/what-a-task-costs-on-opus-5-5
published_at: '2026-09-22'
---

## 概要

Opus 5.5はトークン単価がOpus 5より低いが、タスクの費用はターン数、キャッシュ読み取り、出力トークン(思考を含む)、モデル選択で決まると解説する。努力度やモデルを下げてもリトライが増えれば逆に高くなり得るとする。

## 設計のポイント

- 各ターンが会話全体を再送するため、ターン数の削減が入力コストに直結する。
- テストやビルドなど自己検証手段を与えてターン数とリトライを減らす。
- キャッシュ読み取りは入力単価の一部で、思考は出力として5倍で課金される。

## 使いどころ

- エージェント利用の予算を見積もる開発チーム。
- 効率とコストのトレードオフを設定する管理者。
- 自分のセッション使用量を確認したい個人開発者。
