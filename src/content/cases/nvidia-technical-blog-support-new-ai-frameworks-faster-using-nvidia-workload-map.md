---
type: guidance
title: NVIDIA Workload MapでKubernetes上の分散AIワークロードを共通記述する
title_original: Support New AI Frameworks Faster Using NVIDIA Workload Map
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- unified-runtime
components:
- NVIDIA Workload Map
- KAI Scheduler
- NVIDIA Run:ai
- JobSet
- KServe
- NVIDIA Dynamo
- Ray
outcome:
  type: productivity
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/support-new-ai-frameworks-faster-using-nvidia-workload-map/
published_at: '2026-10-28'
---

## 概要

Kubernetes上のAIワークロードの構造を共通形式で記述するWorkload Mapを紹介する。JobSetなどの定義を一度書けば、検査、ギャングスケジューリング、プラットフォーム表示に再利用でき、フレームワーク固有のパーサーが不要になる。ElotlのNovaでも活用されている。

## 設計のポイント

- フレームワークごとの独自リソースを共通記述に写し、スケジューラやコントローラが個別アダプタなしに解釈できるようにする。
- JobSetやRayなど主要フレームワークの定義カタログを用意し、既存の定義を流用できる。
- 1つの定義をCLI検査、KAI Schedulerのギャングスケジューリング、Run:aiの管理に共用する。

## 使いどころ

- 複数のAIフレームワークを混在運用するAIファクトリーの運用者。
- 新しいフレームワーク対応のたびにスケジューラの解析コードを書いている基盤チーム。
