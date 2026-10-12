---
type: guidance
title: llama.cpp on SageMakerで選択肢スコアを返す決定モデルを配信する
title_original: Deploy decision models with llama.cpp on Amazon SageMaker AI
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- decision-execution
- cost-optimization
components:
- Amazon SageMaker AI
- AWS Deep Learning Containers
- llama.cpp
- SemIf
- AWS CodeBuild
- Amazon ECR
- Amazon S3
- Qwen3.5-4B
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/deploy-decision-models-with-llama-cpp-on-amazon-sagemaker-ai/
published_at: '2026-10-12'
---

## 概要

llama.cpp用AWS DLCでOpenAI互換のチャット補完を配信し、さらに子イメージでSemIfアダプタに差し替えて、回答トークンを生成せず宣言済み選択肢の確率を返す決定モデルを構築する手引き。231タスクのベンチでは、GPU(ml.g6e.xlarge)がCPUよりp50で4.9倍、p95で32.2倍高速だった。

## 設計のポイント

- 標準パスは model.tar.gz とDLCをそのまま使い、logits/状態へのアクセスが要る場合だけCodeBuildで子イメージを作ってエントリポイントを差し替える。
- 選択肢IDを固定し確率を返すことで、閾値・フォールバック・ポリシーチェックを生成文のパース無しで適用できる。
- 認可や決定的な業務ルールはモデルの外に置き、確率は運用上の信頼度として使う前に検証する。
- SageMakerのインスタンスプールで優先順にGPU型を指定し、容量不足時に代替型へ自動で切り替える。

## 使いどころ

- ルーティング、インシデント優先度付け、ポリシー判定、エージェントのアクション選択など、固定選択肢への分類を低コストに行いたい場面。
- バックグラウンド処理ならCPU、対話的・長文プロンプト・テイルレイテンシ厳守ならGPUと使い分けたいとき。
