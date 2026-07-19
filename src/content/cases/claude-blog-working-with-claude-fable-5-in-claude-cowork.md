---
type: guidance
title: Claude CoworkでのClaude Fable 5活用ガイド
title_original: Working with Claude Fable 5 in Claude Cowork
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- context-engineering
- prompt-optimization
components:
- Claude Fable 5
- Claude Cowork
- Claude Opus
- Claude Sonnet 5
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/working-with-claude-fable-5-in-claude-cowork
published_at: '2026-07-16'
---

## 概要

Claude Cowork上でClaude Fable 5を使いこなすための指針を解説。長時間・複雑・曖昧なタスクほどFable 5が向いており、effort設定でコストと計画の深さを調整できる。

## 設計のポイント

- タスクの明確さと複雑さに応じてSonnet(日常業務)/Opus(明確な深い作業)/Fable 5(曖昧で複雑な作業)を使い分ける。
- 大きなジョブは複数のサブエージェントに分割して並行実行し、最初に立てた計画と結果を照合しながら誤りを早期修正する。
- effortを上げるほど計画とチェックの頻度が増し、下げると低コストで高速な応答が得られる。
- サイバーセキュリティやバイオ関連の誤用検知分類器が作動するとOpus 4.8に自動フォールバックし、ユーザーに通知される。

## 使いどころ

- 予算策定やデューデリジェンスなど数十ステップにわたる複雑な業務をエージェントに任せたいナレッジワーカー。
- 曖昧なアイデア出しの段階からブレインストーミングして実行計画に落とし込みたいチーム。
