---
type: case
title: SageMaker AIのマルチターンRLで小型モデルを検索エージェントに特化させる
title_original: Fine-tune a search agent with multi-turn RL on Amazon SageMaker AI
industry: cross-industry
cloud:
- aws
patterns:
- reinforcement-learning
- fine-tuning
- ai-agent
components:
- Amazon SageMaker AI
- Qwen3.6-27B
- Amazon S3
- MLflow
- Amazon Bedrock
- BM25
- vector search
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/fine-tune-a-search-agent-with-multi-turn-rl-on-amazon-sagemaker-ai/
published_at: '2026-10-02'
---

## 概要

Amazon SageMaker AIのマルチターン強化学習(MTRL)でQwen3.6-27Bを、BM25とベクトル検索を使う検索エージェントとしてファインチューニングした事例。小型モデルでフロンティアモデル並みの信頼性と、低レイテンシ・低コストの両立を狙う。

## 設計のポイント

- SFTの軌跡データやシングルターンRLでは捉えられない多段の依存を、軌跡全体への最終結果報酬で最適化する。
- ロールアウトと勾配更新を非同期に並列化し、サーバーレスでGPUクラスタ管理を不要にする。
- ターン数を制限して効率的な検索行動を促す。
- MLflowで軌跡と報酬を可視化し、評価後にSageMakerエンドポイントやBedrockへデプロイする。

## 使いどころ

- フロンティアモデルの遅延とコストを避けつつ、社内ツールに特化した検索エージェントを作りたい場面。
- 専門家の模範軌跡データが存在しない環境でエージェントを学習させたいチーム。
