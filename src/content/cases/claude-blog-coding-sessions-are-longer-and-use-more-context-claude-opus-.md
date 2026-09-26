---
type: announcement
title: Claude Opus 5.5のキャッシュ料金と長時間コーディングセッションの最適化
title_original: Coding sessions are longer and use more context. Claude Opus 5.5 is built with that in mind.
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- context-engineering
- cost-optimization
- ai-agent
components:
- Claude Opus 5.5
- Claude Code
- Fable 5.1
outcome:
  type: cost
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-opus-5-5-built-for-coding-sessions-that-use-more-context
published_at: '2026-09-24'
---

## 概要

Anthropicは、Opus 5.5が典型的なトークン課金の作業でOpus 5より約40%安いと推定する。入出力トークン20%減、キャッシュ読み取り60%減に加え、Claude Codeのキャッシュ効率改善や少ないターン数が効く。長く文脈の大きいセッションほど効果が大きい。

## 設計のポイント

- エージェント作業のコストの大半はキャッシュ読み取りのため、コンテキストを絞りキャッシュヒットを最大化する。
- セッション中の指示追加やツールのオンデマンド読み込み等でキャッシュを壊さない設計にする。
- フォークしたサブエージェントが親のキャッシュを引き継ぎ、同じ文脈を再課金しない。

## 使いどころ

- 長時間・大コンテキストのコーディングエージェントを運用するチーム。
- トークンコストを見積もり最適化したい開発組織。
