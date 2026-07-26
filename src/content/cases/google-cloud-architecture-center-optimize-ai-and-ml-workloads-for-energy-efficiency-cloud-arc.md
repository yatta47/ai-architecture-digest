---
type: guidance
title: AI/MLワークロードのエネルギー効率を最適化するGoogle Cloud設計原則
title_original: Optimize AI and ML workloads for energy efficiency
industry: cross-industry
cloud:
- gcp
patterns:
- cost-optimization
- inference-optimization
components:
- TPU
- DistilBERT
outcome:
  type: cost
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/framework/sustainability/ai-ml-energy-efficiency
published_at: '2026-07-19'
---

## 概要

Google CloudのWell-Architected Frameworkサステナビリティ領域より、AI/MLワークロードの省エネ設計原則。TPU活用、モデル・マシン・クラウド化・立地選定の『4Ms』ベストプラクティス、蒸留・枝刈り・量子化などのモデル圧縮技術によって、トレーニング/推論のエネルギー消費とカーボンフットプリントを削減する方法をまとめている。

## 設計のポイント

- 汎用CPU/GPUではなく行列演算に特化したTPUを使うことで、同じ計算量あたりのエネルギー消費を大幅に下げる
- モデル・マシン・クラウド化・立地選定の『4Ms』の観点で、最大のものではなく要件を満たす最小のモデル・ハードウェア・リージョンを選ぶ
- 枝刈り・量子化・知識蒸留などのモデル圧縮技術で、精度を大きく落とさずに推論時の計算資源を削減する

## 使いどころ

- 大規模な学習・推論ジョブのコストとカーボンフットプリントを同時に抑えたいMLプラットフォームチーム
- サステナビリティ目標をAI基盤の設計基準に組み込みたい企業
