---
type: guidance
title: GPT-4oからGPT-4o-miniへのモデル蒸留によるファインチューニング
title_original: Leveraging model distillation to fine-tune a model
industry: cross-industry
cloud: []
patterns:
- fine-tuning
- cost-optimization
components:
- gpt-4o
- gpt-4o-mini
- OpenAI Structured Outputs
outcome:
  type: cost
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/cookbook/examples/leveraging_model_distillation_to_fine-tune_a_model/
published_at: '2024-10-16'
---

## 概要

gpt-4oの出力を教師データとしてgpt-4o-miniを蒸留・ファインチューニングし、非蒸留のgpt-4o-miniと性能を比較するレシピ。ワインレビューデータからブドウ品種を分類するタスクを題材に、Structured Outputsを使った分類でも蒸留の効果を検証する。

## 設計のポイント

- 大規模モデルの出力を教師データとして小規模モデルをファインチューニングし精度を引き上げる
- enumによるStructured Outputsを併用し分類タスクの出力形式を安定させる

## 使いどころ

- 推論コストとレイテンシを抑えつつ特定タスクの精度を大規模モデル並みに引き上げたい場合
- 分類のように出力範囲が限定される既知タスクを低コストモデルに移行したい場合
