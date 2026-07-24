---
type: guidance
title: 強化学習ファインチューニング(RFT)のためのモデルグレーダー設計
title_original: Exploring Model Graders for Reinforcement Fine-Tuning
industry: healthcare
cloud: []
patterns:
- reinforcement-learning
- fine-tuning
- eval
components:
- o4-mini
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/cookbook/examples/reinforcement_fine_tuning/
published_at: '2025-05-23'
---

## 概要

医療分野の会話データを題材に、OpenAIのo4-miniモデルへ強化学習ファインチューニング(RFT)を適用し推論精度を高める手順を解説する。グレーダー（報酬関数）の設計と、報酬ハッキングを避けるための注意点に焦点を当てている。

## 設計のポイント

- 少量のデータでも軌跡サンプリングとフィードバックループにより着実な性能向上を得られるRFTの特性を活用する
- 厳密一致とトークン類似度ベースの2種類のグレーダーを併用し、モデルの学習信号の質を検証する

## 使いどころ

- 医療記録の要約や分類など、専門用語の正確さが求められるドメイン特化タスクの精度改善
- 少量の検証済みデータしかない状況で推論モデルの挙動を狙った方向に調整したいケース
