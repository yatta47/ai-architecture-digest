---
type: guidance
title: NeMo GymとNeMo RLでNemotronを科学ドメインに強化学習で後訓練する手順
title_original: Post-training NVIDIA Nemotron to increase accuracy in your scientific domain
company: NVIDIA
industry: healthcare
cloud:
- multi-cloud
patterns:
- reinforcement-learning
- fine-tuning
- eval
components:
- Nemotron 3.5 Super VL
- NeMo Gym
- NeMo RL
- Nemotron Litmus-Bench V2.0
- Claude Sonnet 5.5
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/post-training-nvidia-nemotron-to-increase-accuracy-in-your-scientific-domain/
published_at: '2026-11-13'
---

## 概要

実験データからNeMo Gymでカスタム強化学習環境を作り、NeMo RLでNemotron 3.5 Super VLを後訓練する手順を、薬物代謝予測で示す。SFTで12%、RLでさらに17%精度が向上した。

## 設計のポイント

- 実験データから検証可能な報酬(分子類似度)を持つRL環境を作る
- SFTのあとにRLを重ねる
- 強い教師モデルの推論トレースでウォームスタートし、収束を早める
- 出力トークン予算を揃えて精度を比較する

## 使いどころ

- 創薬・化学の専門タスク向けモデルのカスタマイズ
- 検証可能な報酬を設計できる領域でのRL後訓練
