---
type: guidance
title: 0〜1のスコアでモデル出力を評価するGradersの設計パターン
title_original: Graders
industry: cross-industry
cloud: []
patterns:
- eval
- fine-tuning
components:
- Evals API
- Graders
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/graders
published_at: '2025-07-21'
---

## 概要

Gradersはモデルの生成結果を参照回答と比較し0から1のスコアを返す仕組みで、文字列一致・テキスト類似度・スコアモデルによる採点・Pythonコード実行という複数のグレーダー種別を提供する。強化学習ファインチューニング（RFT）ではmultigradersとして複数のグレーダーを入れ子・組み合わせできる。

## 設計のポイント

- 二値の正誤ではなく0〜1の部分点を与えることで、評価やRFTの報酬設計をより細かく調整できる。
- 用途に応じて文字列一致・類似度・モデル採点・コード実行という異なる種別のグレーダーを使い分ける。

## 使いどころ

- 強化学習ファインチューニングの報酬関数を設計するチーム。
- eval結果を単純な正誤ではなく段階的な品質スコアとして可視化したい場合。
