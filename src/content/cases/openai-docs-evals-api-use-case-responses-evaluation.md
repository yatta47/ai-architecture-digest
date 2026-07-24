---
type: guidance
title: Evals APIで本番ログを使い新旧モデルの回答品質を比較する
title_original: Evals API Use-case - Responses Evaluation
industry: cross-industry
cloud: []
patterns:
- eval
components:
- Evals API
- gpt-4.1-mini
- gpt-4o-mini
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/cookbook/examples/evaluation/use-cases/responses-evaluation/
published_at: '2025-05-13'
---

## 概要

本番トラフィックのログをそのままデータソースとして使い、gpt-4o-miniとgpt-4.1-miniの応答品質をOpenAI Evals APIで比較する手順を解説する。独自の評価データセットを新たに用意することなく、既存ログからモデル移行の妥当性を検証できる。

## 設計のポイント

- 本番ログ(logsデータソース)をそのまま評価データとして再利用し、評価用データセット構築の手間を省く
- 採点基準を明文化したgraderプロンプトをモデルベースの評価者に渡し、1〜7の定量スコアで品質を比較する

## 使いどころ

- 新モデルへの切り替え前に既存の本番トラフィックで品質差を定量評価したい場合
- 評価データセットをゼロから作る余裕がないチームがモデル移行の意思決定を行う場面
