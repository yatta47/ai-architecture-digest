---
type: opinion
title: 意思決定モデル8種のベンチマーク（幻覚検出・LLM評価・エージェントルーティング）
title_original: 'Decision model benchmark: Jev, Kev, Liquid d1, and more'
company: Arize
industry: cross-industry
cloud: []
patterns:
- eval
- multi-model-routing
- guardrails
components:
- Arize AX
- Arize Phoenix
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/decision-model-benchmark/
published_at: '2026-10-07'
---

## 概要

選択肢ごとの確率を返し、テキストを生成しない「意思決定モデル」8種を、幻覚検出・LLM評価・エージェントルーティングで比較した。精度は上位モデル間で拮抗し、遅延・コスト・提供形態・質問文への感度に差が出た。

## 設計のポイント

- エージェント内のツール選択や継続判断を、生成なしの確率出力で低コスト・低遅延にする
- トレース評価のジャッジとしてLLMの代わりに用いる
- 精度が近い場合は遅延、コスト、デプロイ方式、プロンプト感度で選定する

## 使いどころ

- エージェントの評価基盤やガードレールを低コストにしたい場面
- ルーティング判断のレイテンシを抑えたい場面
