---
type: guidance
title: EKS上でRay LLM DLCによるprefill/decode分離のマルチノード推論
title_original: Run multi-node inference workloads using Ray LLM Deep Learning Containers
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- unified-runtime
- parallel-execution
components:
- Amazon EKS
- Ray Serve LLM
- KubeRay
- vLLM
- NIXL
- Elastic Fabric Adapter
- Amazon ECR
- AWS Deep Learning Containers
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/run-multi-node-inference-workloads-using-ray-llm-deep-learning-containers/
published_at: '2026-10-12'
---

## 概要

Ray LLM DLCを使い、Amazon EKS上の2つのGPUノードでprefillとdecodeを分離して1つのOpenAI互換エンドポイントの背後に配備する手順。vLLM、NIXL、EFAを同梱し、YAMLだけでサービングアプリを定義できる。

## 設計のポイント

- 計算律速のprefillとメモリ帯域律速のdecodeを別ノードに置き、長文プロンプトがトークン生成を阻害するのを防ぎ、個別にスケールできるようにする。
- KVキャッシュはNIXLでEFA経由で転送し、転送が利点を打ち消さないようノード間接続を重視する。EFAはAZを跨げないためGPUノードグループは単一AZに固定する。
- build_pd_openai_appにprefill/decode設定を渡すだけで、ハンドラやカスタムイメージ無しに構成できる。
- Ray headはCPUノードに置き、KubeRayのRayServiceでワーカー結合を自動化する。

## 使いどころ

- RAG、文書要約、エージェント用途など長いプロンプトが多いLLM推論を高スループットで運用したい場合。
- 単一GPUに載らない大規模モデルをEKSで配信するプラットフォームチーム。
