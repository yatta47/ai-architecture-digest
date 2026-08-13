---
type: guidance
title: 2.4兆パラメータのQwen3.8-2.4T-A95BをGB300 NVL72で配信可能にする推論最適化
title_original: Serve Qwen3.8-2.4T-A95B, a 2.4T-Parameter Model, with Configurable Reasoning on NVIDIA GB300 NVL72
industry: cross-industry
cloud: []
patterns:
- inference-optimization
- reasoning-computation-separation
components:
- NVIDIA GB300 NVL72
- SGLang
- vLLM
- NVIDIA Dynamo
- NVIDIA NIM
- NVIDIA NeMo AutoModel
- Qwen3.8-2.4T-A95B
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/serve-qwen3-8-2-4t-a95b-a-2-4t-parameter-model-with-configurable-reasoning-on-nvidia-gb300-nvl72/
published_at: '2026-08-12'
---

## 概要

Alibabaが公開した2.4兆パラメータのオープンウェイトモデルQwen3.8-2.4T-A95Bを、NVIDIA GB300 NVL72上でFP8精度により1GPUあたり4,000トークン/秒超で配信する構成を解説。ハイブリッドなフル/線形アテンションとファイングレインMoEで100万トークンのコンテキストを実用的なコストで扱えるようにし、SGLang/vLLM/Dynamo/NIMなど複数の推論スタックから選択できる。

## 設計のポイント

- フルアテンション層と線形アテンション層を交互配置し、コンテキストが伸びてもKVキャッシュメモリと計算量を有界に保つ
- 少数の大きなエキスパートではなく多数の小さなエキスパートに容量を分散するファイングレインMoEで、活性化パラメータ相応のコストに抑える
- 推論の深さ（low/high/xhigh）をリクエスト単位で設定可能にし、タスクごとに計算コストと推論品質をトレードオフできるようにする

## 使いどころ

- コーディングや大規模文書解析など長時間・長コンテキストのエージェント的ワークロードを本番配信したいAIインフラチーム
- オープンウェイトのフロンティア級モデルをドメイン特化でファインチューニングして使いたい開発者
