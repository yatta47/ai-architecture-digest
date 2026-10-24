---
type: case
title: SageMakerのマルチターン強化学習でエージェントを訓練する手引き（Wordle例）
title_original: 'Multi-Turn Reinforcement Learning on Amazon SageMaker AI: A hands-on guide'
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- reinforcement-learning
- ai-agent
- fine-tuning
- eval
components:
- Amazon SageMaker AI
- Amazon Bedrock AgentCore
- Strands Agents
- AWS Lambda
- MLflow
- GPT-OSS-20B
- Amazon S3
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/multi-turn-reinforcement-learning-on-amazon-sagemaker-ai-a-hands-on-guide/
published_at: '2026-10-23'
---

## 概要

SageMaker AIのMulti-Turn Reinforcement Learning（MTRL）は、AgentCore上のエージェントが複数ターン行動した末の1つの報酬だけでポリシーモデルをGRPO+LoRAで訓練する。Wordleを題材に、gpt-oss-20bの正解率が既定の推論強度で61→84%、低強度で15→69%に向上し、学習トークン費用は約$339だった。

## 設計のポイント

- エージェント・環境・報酬関数を1つのPythonファイルにまとめてAgentCoreへデプロイし、データセットには正解語のみを持たせる。
- 報酬は成功を主体（速さで1.05〜1.55、失敗-0.5、有効な推測なし-1.5）とし、各階層内に小さな戦略シェーピング項を足す。
- 学習はサーバーレスで、プレフィル/サンプル/学習トークンの従量課金。学習トークンが支配的で軌跡長に比例するため、短いゲームと冗長でない推論がコスト削減につながる。
- 評価は学習時と同じ推論強度だけでなく、本番の提供設定で行う。

## 使いどころ

- 自社業務固有の多段ステップタスクで、小型で低コストなモデルを高精度化したいチーム。
- 模倣すべき正解手順がなく、成否だけが評価信号になるエージェント業務（経費申請、サポートチケット対応など）。
- 既存のAgentCoreやEKS/EC2/Fargate上のエージェントを再利用して強化学習を試したい場合。
