---
type: announcement
title: OpenCostとllm-dの統合によるKubernetes上のLLM推論コスト可視化
title_original: 'OpenCost 1.121.0: First-of-a-Kind Kubernetes Inference Cost Tracking'
industry: cross-industry
cloud: []
patterns:
- cost-optimization
- llmops
- inference-optimization
components:
- OpenCost
- llm-d
- vLLM
- Prometheus
outcome:
  type: cost
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/08/05/opencost-1-121-0-first-of-a-kind-kubernetes-inference-cost-tracking/
published_at: '2026-08-05'
---

## 概要

CNCFのコスト可視化プロジェクトOpenCostが、分散LLM推論基盤llm-d（vLLMベース）と統合し、Kubernetes上のモデル単位・トークン単位のコストをPrometheus経由で計測できるようにした。GPUの確保コストを含む「配分ベース」と実処理分のみの「使用量ベース」の2種類のコスト指標を分けて出すことで、稼働率を定量化しセルフホストとSaaS APIの損益分岐点を判断できるようにする。

## 設計のポイント

- 配分ベース（モデル保持の全コスト）と使用量ベース（実処理分のみ）の2種類のコスト指標を分離して算出する
- 両指標の比率からGPU稼働率を別メトリクスなしに導出できるようにする
- vLLMのトークンスループットメトリクスとOpenCostの既存GPU配分エンジンを組み合わせて実装する
- セルフホストとSaaS APIの比較には使用量ベースでなく配分ベースのコストを使うべきと明示する

## 使いどころ

- プラットフォームチームがモデル単位・トークン単位でAI基盤のROIを説明したい場面
- 自社ホスティングとSaaS API利用のどちらが安いか、稼働率を踏まえて判断したい場面
- 低稼働率で待機中のモデルを特定してコスト最適化したい場面
