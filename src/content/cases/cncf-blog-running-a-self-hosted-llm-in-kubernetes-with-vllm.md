---
type: guidance
title: Kubernetes上でvLLM＋LINSTORによるセルフホストLLM推論基盤を構築する手引き
title_original: Running a Self-Hosted LLM in Kubernetes with vLLM
industry: cross-industry
cloud:
- on-prem
patterns:
- inference-optimization
- llmops
components:
- vLLM
- LINSTOR
- DRBD
- Kubernetes
- Piraeus Operator
- LINSTOR CSI driver
- Hugging Face
- Llama-3.2-1B-Instruct
data_sources:
- モデルの重み
- 推論リクエスト
outcome:
  type: risk-compliance
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/07/16/running-a-self-hosted-llm-in-kubernetes-with-vllm/
published_at: '2026-07-16'
---

## 概要

マネージドAPIの補完策として、LLM推論をKubernetes上で自前運用するラボ構成を解説した手引き。推論エンジンにvLLM、永続ストレージにDRBDベースのLINSTOR（CSIドライバ）を使い、GPUなしのCPU環境でMetaのLlama-3.2-1B-Instructを提供する。PVC・Hugging Faceトークン用Secret・Deployment/Serviceの3リソースで構成される。

## 設計のポイント

- モデル重みのキャッシュパス(/root/.cache/huggingface)を2レプリカのLINSTOR永続ストレージで裏打ちし、ダウンロードを初回のみに抑えてPod再起動・ノード障害を跨いで重みを保持する
- vLLMがOpenAI互換RESTを公開するため、既存のOpenAI/LangChain/LlamaIndexコードをURL変更だけで切り替えでき、機微・大量処理は自前／それ以外はマネージドAPIというハイブリッド構成が成立する
- CPU専用では--gpu-memory-utilizationを0.80に設定する（既定92%のままだと起動時にメモリ不足になる）

## 使いどころ

- コスト予測性・レイテンシ制御・データ所在地（規制対応）を理由にLLMを自前運用したいチーム
- マネージドAPIと自前推論を使い分けるハイブリッド基盤をKubernetesで組みたい場面
