---
type: guidance
title: SageMaker HyperPodとvLLMで2.4兆パラメータQwen3.8を配信
title_original: Deploying Qwen3.8-2.4T-A95B on Amazon SageMaker HyperPod with vLLM
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- llmops
components:
- Amazon SageMaker HyperPod
- vLLM
- Qwen3.8-2.4T-A95B
- NVIDIA B300
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/deploying-qwen3-8-2-4t-a95b-on-amazon-sagemaker-hyperpod-with-vllm/
published_at: '2026-09-09'
---

## 概要

総パラメータ2.4兆・トークンあたり活性化950億のオープンウェイトMoEモデルQwen3.8-2.4T-A95Bを、Amazon SageMaker HyperPod上の8×NVIDIA B300インスタンスとvLLMでNVFP4量子化・投機的デコードとともに配信する構成を解説する。オープンウェイトによりデータを自社環境に留め、トークン課金なしで運用できる。

## 設計のポイント

- 線形アテンション（Gated DeltaNet）とフルアテンションを3:1で組み合わせ、100万トークン級の長文脈でも計算・メモリを一定に保つ
- 512の細粒度MoEエキスパートのうち約950億パラメータのみを活性化させ、サービングコストをモデル全体サイズではなく活性化分で抑える
- reasoning_effortパラメータで推論の深さと計算コストをリクエスト単位でトレードオフできるようにする

## 使いどころ

- 推論挙動のカスタマイズやデータ主権が必要で、トークン課金APIを避けたいエージェント型ワークロード
- 長期のツール利用・推論トレースを蓄積する複数ステップのコーディング・リサーチタスク
