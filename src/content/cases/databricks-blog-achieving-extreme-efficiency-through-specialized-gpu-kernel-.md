---
type: case
title: エージェントによるGPUカーネル自動生成基盤Proteusで推論を高速化
title_original: Achieving Extreme Efficiency through Specialized GPU Kernel Generation
company: Databricks
industry: cross-industry
cloud: []
patterns:
- ai-agent
- inference-optimization
- eval
- context-engineering
components:
- Proteus
- Qwen 3.5 122B
- vLLM
- CUDA
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/achieving-extreme-efficiency-through-specialized-gpu-kernel-generation
published_at: '2026-09-04'
---

## 概要

Databricksはエージェントにモデルサイズや実行時のリクエスト形状ごとに特化したGPUカーネルを生成させる基盤Proteusを構築し、Qwen 3.5 122BのカーネルでvLLM最良実装比1.8〜5.2倍の高速化を達成した。成功の鍵はカーネル探索自体よりも、reward hackingや測定バグを防ぐ検証（チェッカー）と、プロンプトに詰め込む文脈量のトレードオフ管理にあったと報告している。

## 設計のポイント

- 候補カーネルの生成よりも検証（複数タイマーでのクロスチェック、見えないテストケース、状態のクリア）に開発の重心を置く
- 物理的なGPU帯域・演算限界を超える非現実的な高速化を自動検知し、reward hackingによる測定バグを防ぐ
- 現在の最良カーネル・失敗履歴・プロファイラ情報などプロンプトに含める文脈量を、コストとドリフトのトレードオフとして管理する
- 得られた知見を具体性と汎用性のバランスを取った形で記憶レイヤーに保存し、次の試行や別カーネルに再利用する

## 使いどころ

- モデルサイズやリクエスト形状ごとに専用GPUカーネルを自動生成して推論コスト・レイテンシを削減したい場合
- エージェントによるコード生成・最適化でreward hackingを防ぐ検証基盤を設計したい場合
