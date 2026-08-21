---
type: case
title: NVIDIA DSX MaxLPS、動的電力配分でAIファクトリーのワット当たり性能を最大1.5倍に
title_original: Maximizing AI Factory Performance per Watt with NVIDIA DSX MaxLPS
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- gpu-fleet-reliability
- cost-optimization
components:
- NVIDIA DSX MaxLPS
- NVIDIA Vera Rubin NVL72
- NVIDIA GB200 NVL72
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/maximizing-ai-factory-performance-per-watt-with-nvidia-dsx-maxlps/
published_at: '2026-08-20'
---

## 概要

AIファクトリーは電力制約下の産業システムであり、GPU台数よりも利用可能なメガワット当たりの出力が問われる。NVIDIA DSX MaxLPSは動的電力配分ソフトウェアと45℃対応の熱設計により、固定電力予算内でラック当たり最大40%多いGPU容量を実現し、ワット当たり性能を1.3〜1.5倍に高める。

## 設計のポイント

- ラック単位の静的な電力割り当てではなく、テレメトリとポリシーに基づくリアルタイムの動的電力再配分でGPU間の稼働率を最適化する
- 45℃の液冷を前提とした熱設計を早期のサイト設計段階から組み込み、電力予算内でのGPU密度を引き上げる
- ワット当たり性能を『GPU台数』に代わるAIファクトリーの主要評価指標として位置づける

## 使いどころ

- データセンターの電力予算が拡張のボトルネックになっているAIインフラ運用チーム
- 既存施設の電力容量内でGPU密度を引き上げたい大規模GPUクラスタ運用者
- サイト設計段階から液冷・電力設計を最適化したい新設AIファクトリー
