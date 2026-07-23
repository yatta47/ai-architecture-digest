---
type: guidance
title: 大規模並列計算(Big Compute)を支えるアーキテクチャスタイル
title_original: Big compute architecture style
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: speed
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/big-compute
published_at: '2025-09-05'
---

## 概要

Big Computeは画像レンダリングや流体力学、金融リスクモデリングなど、数百〜数千コア規模の並列処理を要するワークロードを指すアーキテクチャスタイルである。タスクは独立して並列実行できる場合と、InfiniBandなどの高速ネットワークで密結合させる必要がある場合に分かれる。AzureではAzure Batchによるマネージドスケジューリングや、HPC Packを使ったVMクラスタ構築・オンプレミスからのバースト展開といった複数の実現手段が示されている。
