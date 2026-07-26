---
type: guidance
title: AI/MLのパフォーマンス最適化：現実的なKPI設定とモニタリング
title_original: 'AI and ML perspective: Performance optimization'
industry: cross-industry
cloud:
- gcp
patterns:
- inference-optimization
- eval
components:
- TensorBoard
- Vertex AI
- Cloud Monitoring
outcome:
  type: speed
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/performance-optimization
published_at: '2026-07-19'
---

## 概要

AI/MLシステムのパフォーマンスを事業KPIに翻訳し、品質指標と速度指標を区別した現実的な目標設定、実験・学習・本番稼働の各段階でのモニタリング、モデルアーキテクチャや設計選択と性能指標の紐づけ方についての原則をまとめている。不正検知システムを例に非現実的な目標設定の落とし穴も指摘する。

## 設計のポイント

- 『品質』（精度・再現率）と『性能』（レイテンシ・スループット）を明確に区別し、それぞれに現実的な目標値を設定する
- 実験段階ではTensorBoard等でモデル品質と学習効率を可視化し、無駄な学習継続を早期に打ち切れるようにする
- 本番稼働後も継続的にKPIをモニタリングし、モデル劣化やコスト・市場投入時間への影響を判断材料にする

## 使いどころ

- 不正検知やリアルタイム推論などレイテンシ要件が厳しいAIシステムの目標設定
- 学習実験を多数並行して回し、リソースを無駄にせず収束させたいMLエンジニアリングチーム
