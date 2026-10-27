---
type: case
title: 評価ラベルの偏りを正し、プロンプト進化最適化でBedrockの画像分類を低コスト化
title_original: Fix evaluation bias to unlock better models on Amazon Bedrock
company: Property Finder
industry: other
cloud:
- aws
patterns:
- eval
- prompt-optimization
- multi-model-routing
components:
- Amazon Bedrock
- Micro F1
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/fix-evaluation-bias-to-unlock-better-models-on-amazon-bedrock/
published_at: '2026-10-27'
---

## 概要

Property Finderは不動産画像の品質判定VLMの評価ラベルの96.8%が現行モデルの出力由来だと発見し、専門家が独立に注釈した正解データを作り直した。その上で進化的プロンプト最適化を回し、Bedrock上の別モデルで精度を上げつつコストを86%削減した。

## 設計のポイント

- 現行モデルの出力を正解に流用すると代替モデルが構造的に不利になるため、既存出力を見せずに専門家が独立注釈する。
- 単一ラベルを複数ラベルへ変更し、扉越しの部屋など人工的な曖昧さを評価から除く。
- 注釈済みの開発セットに対しMicro F1で採点しエラー分析を繰り返すプロンプト最適化ループを組む（v0〜v27）。

## 使いどころ

- モデル移行やコスト削減のためにVLM/LLMを比較したいチーム。
- 本番出力をそのまま評価データにしている分類ワークロードの評価見直し。
