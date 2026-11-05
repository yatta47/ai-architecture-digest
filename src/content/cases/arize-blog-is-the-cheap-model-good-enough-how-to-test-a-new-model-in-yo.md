---
type: guidance
title: 安価モデルへ切り替える前の検証手順：トレース・評価・実験でエージェントを比較
title_original: Is the cheap model good enough? How to test a new model in your agent
company: Arize
industry: cross-industry
cloud: []
patterns:
- eval
- llmops
- cost-optimization
- multi-model-routing
components:
- Arize AX
- Arize Phoenix
- OpenRouter
- Anthropic SDK
- LiveCodeBench
outcome:
  type: cost
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/how-to-test-a-new-model-in-your-agent/
published_at: '2026-11-05'
---

## 概要

安価なQwen3.8 Flashをmanager/workerループ（GVS5H）やRalphループで包めば高価なOpus 5.5の代わりになるかを、Arizeのトレース、評価、データセット、実験で検証した手順の記事。合格率、解決1件あたりのコスト、レイテンシを事前に定義した基準で比較する。

## 設計のポイント

- 先に『安く、遅くならず、同等以上に正しい』という判断基準を定義してから評価を設計する。
- 本番トレースから合格・失敗の両方を含むデータセットを作り、同じ評価器で複数モデルや構成を実験する。
- 単発呼び出しの基準とループ有りを比較し、改善がループ由来かモデル由来かを切り分ける。
- 集計値だけでなく差の出たトレースを読み、数字の誤解を防ぐ。

## 使いどころ

- モデル切り替えのコスト削減効果を検証するエージェント開発チーム
- エージェントのCI的な回帰評価基盤を整えたい担当
