---
type: guidance
title: GPU付き常駐インスタンス上で3エージェントが協調する音楽制作パイプライン
title_original: Build a multi-agent music production pipeline on Amazon Bedrock AgentCore Runtime Instances
industry: media
cloud:
- aws
patterns:
- multi-agent-orchestration
- ai-agent
- unified-runtime
components:
- Amazon Bedrock AgentCore Runtime Instances
- Amazon Bedrock AgentCore
- Claude Sonnet 4.6
- ACE-Step
- Amazon ECR
- Amazon S3
- Amazon EBS
- Amazon EC2
- NVIDIA L4
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-a-multi-agent-music-production-pipeline-on-amazon-bedrock-agentcore-runtime-instances/
published_at: '2026-09-30'
---

## 概要

Amazon Bedrock AgentCoreの新しいRuntime Instances（AWS管理のEC2基盤）上で、作曲・マスタリング・コンプライアンスの3エージェントが1台のGPUインスタンスと共有ボリュームを使って協調し、再生可能な.wavを生成する手順を解説する。作曲エージェントはClaude Sonnet 4.6でブリーフを作りACE-StepをNVIDIA L4上で実行、配信エージェントは計測値に基づく処理チェーンを適用、コンプライアンスエージェントは再計測と既存カタログとの類似スクリーニングを行い、問題があれば作曲エージェントに差し戻す。最大14日のセッションと永続ボリュームにより複数日にまたがるワークフローを継続できる。

## 設計のポイント

- 同じキャパシティプロバイダー上で同一runtimeSessionIdを使い複数エージェントを同じインスタンスに同居させ、ファイルシステム経由で成果物を受け渡す。
- 生成モデルと依存関係を永続ボリュームに置き、セッション内の全呼び出しや夜間停止後の再開で再利用する。
- エージェントごとに別ランタイム・別アーティファクト（ECRコンテナとS3のzip）にして、各チームが独立してデプロイできるようにする。
- LLMには音声そのものではなく計測値を渡して処理チェーンを決めさせ、適用後に再計測して目標達成を検証する。

## 使いどころ

- 数時間のサーバーレスセッション上限を超える複数日の創作・制作ワークフローを運用したいチーム。
- GPUで自前の生成モデルを動かしつつLLMエージェントと組み合わせたいメディア制作現場。
- 複数チームがそれぞれのエージェントを独立したリリースサイクルで更新したい組織。
