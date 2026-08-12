---
type: guidance
title: 3階層KVキャッシュでLLM推論を高速化(SageMaker HyperPod + Curvine)
title_original: Tiered KV cache for large LLMs on Amazon SageMaker HyperPod with Curvine
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- llmops
- cost-optimization
components:
- Amazon SageMaker HyperPod
- Curvine
- vLLM
- LMCache
- Amazon EKS
- Amazon EBS
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/tiered-kv-cache-for-large-llms-on-amazon-sagemaker-hyperpod-with-curvine/
published_at: '2026-08-12'
---

## 概要

Amazon SageMaker HyperPod上で、GPU・CPU・共有NVMe(Curvine)の3階層KVキャッシュとキャッシュ対応ルーティングを組み合わせるアーキテクチャを解説する。検証環境ではクロスPodキャッシュヒット率100%、TTFT最大2.7倍改善を達成し、より低コストなG6eインスタンスでの運用を可能にした。

## 設計のポイント

- GPU(L0)→CPUオフロード(L1、LMCache)→共有NVMe(L2、Curvine)の3階層キャッシュにし、レプリカ間でKVブロックを再利用可能にした。
- Curvineの共有名前空間をReadWriteMany PVCとして全Podにマウントし、あるレプリカが書いたKVブロックを他レプリカが即座に読めるようにした。
- prefix-aware/kv-awareのルーティング戦略でリクエストをキャッシュ保有レプリカへ誘導し、クライアント側の変更なしにヒット率を高めた。
- CRDが未対応のCurvine統合は、LMCACHE_REMOTE_URL環境変数をfs://パスにパッチして実現した。

## 使いどころ

- 複数の基盤モデルを部門別エンドポイントで大量配信し、GPUコストを抑えたい基盤運用チーム。
- 長い共通システムプロンプトやマルチターン対話を扱い、TTFT短縮が体験に直結するRAG・対話アプリ。
- 水平スケールしたvLLMレプリカ間でキャッシュが分断され、コールドスタートに悩むプラットフォームエンジニア。
