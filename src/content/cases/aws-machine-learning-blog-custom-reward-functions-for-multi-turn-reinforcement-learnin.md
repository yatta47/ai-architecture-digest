---
type: guidance
title: Amazon Nova Forgeでマルチターン強化学習の報酬関数を設計する
title_original: Custom reward functions for multi-turn reinforcement learning with Amazon Nova Forge
industry: cross-industry
cloud:
- aws
patterns:
- reinforcement-learning
- llmops
- eval
components:
- Amazon Nova Forge
- Amazon SageMaker HyperPod
- Amazon ECS
- Amazon S3
- AWS Lambda
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/custom-reward-functions-for-multi-turn-reinforcement-learning-with-amazon-nova-forge/
published_at: '2026-08-14'
---

## 概要

Amazon Nova ForgeのBring Your Own Orchestration機能を使い、ツール呼び出しやコード実行を含むマルチターンのエージェントタスクに対してGRPOで学習させるための複合報酬関数の設計手法を解説する。単一ターンはLambdaで完結するがマルチターンは自前のコンテナ環境でロールアウトと採点を実行し、集約報酬とコンポーネント別メトリクスをNova Forgeに返す構成を取る。報酬が実際に何を学習させているかを可視化する重要性も強調している。

## 設計のポイント

- 報酬コンポーネントはグループ内で値にばらつきが無いと勾配に寄与しないため、各項目の分散を監視して学習に効いているか検証する
- 15分のLambda実行時間制限を超えるマルチターンタスクはBYOO（Bring Your Own Orchestration）でECSなどの自前コンテナに委譲する
- 報酬はルールベースの検証とLLM-as-Judgeを組み合わせ、タスク正解性・中間行動シグナル・ペナルティなど複数コンポーネントのスコアをmetrics_listとして返す
- モデル生成コードを報酬計算内で安全に実行する仕組みを用意し、実行結果を検証可能な報酬に変換する

## 使いどころ

- ツール呼び出しやコード実行を伴うエージェントをRFT(強化学習ファインチューニング)で改善したいチーム
- SFTでは学習しきれない長期的な意思決定やエラー復旧行動を獲得させたい場合
- 報酬設計のバグによって学習曲線は健全に見えるのに実際は誤った行動を学習してしまうリスクを避けたいMLエンジニア
