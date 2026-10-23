---
type: announcement
title: SageMakerのサーバーレスモデルカスタマイズにトレーニングセッションが一般提供
title_original: Announcing new ways to customize models with SageMaker AI, without managing GPUs
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- fine-tuning
- reinforcement-learning
- llmops
components:
- Amazon SageMaker AI
- SageMaker Studio
- Kiro
- Claude Code
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/announcing-new-ways-to-customize-models-with-sagemaker-ai-without-managing-gpus/
published_at: '2026-10-22'
---

## 概要

SageMaker AIのサーバーレスモデルカスタマイズにトレーニングセッションが加わった。損失関数や報酬を含む学習ループは自分で書き、GPU割り当て、分散実行、障害復旧、チェックポイントはSageMakerが担う。SFT、DPO、RLVR、RLAIF、マルチターンRLに対応する。

## 設計のポイント

- アルゴリズムは利用者、計算基盤はサービスという境界で責務を分ける。
- 手法選択からデプロイまでを担うモデルカスタマイズ用エージェントスキルを提供する。
- LoRAと全パラメータ更新を選べ、手法を連鎖させる継続的カスタマイズができる。

## 使いどころ

- オープンウェイトモデルをポストトレーニングしたいが、GPU運用は避けたいチーム。
- エージェント向け強化学習環境を構築する開発者。
