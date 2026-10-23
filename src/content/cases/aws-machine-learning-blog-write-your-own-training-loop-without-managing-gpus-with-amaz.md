---
type: guidance
title: GPU運用なしで学習ループを書くSageMakerトレーニングセッションAPI
title_original: Write your own training loop without managing GPUs with Amazon SageMaker training session APIs
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
- forward_backward
- optim_step
- sample
- GSM8K
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/write-your-own-training-loop-without-managing-gpus-with-amazon-sagemaker-training-sessions/
published_at: '2026-10-22'
---

## 概要

forward_backward()、optim_step()、sample()をAPI呼び出しとして組み合わせ、ステートフルなGPUセッション上で任意の学習手順を実装できる。SFT・選好最適化・RLに使え、GSM8K向けRLループと、ユニットテストで採点する競技プログラミングのRL例を解説する。

## 設計のポイント

- 抽象化の境界をアルゴリズムでなく計算資源に引く。
- モデルをGPU上に保持するセッションを使い、ステップ間でロードし直さない。
- コード生成の報酬を、生成コードのユニットテスト実行結果で計算する。

## 使いどころ

- 独自の損失関数やカリキュラムでLLMを学習したい研究・開発チーム。
- 最新のアラインメント手法をすぐ試したい場面。
