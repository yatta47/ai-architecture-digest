---
type: guidance
title: AIエージェントでSpark UDFをGPU向けに書き換える手法
title_original: How to Rewrite Apache Spark UDFs for GPU Acceleration with AI Agents
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- ai-agent
- parallel-execution
- eval
components:
- NVIDIA cuDF
- Apache Spark
- RapidsUDF
- cuDF skills for Apache Spark
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/rewrite-apache-spark-udfs-gpu-acceleration-ai-agents/
published_at: '2026-10-13'
---

## 概要

Spark UDFがGPU実行のCPUフォールバックを招く問題に対し、cuDF skillsを使うエージェントがテスト・変換・ベンチマーク・最適化を検証付きで進める手法。大手消費者向けテクノロジー企業が30以上のUDFを変換し、6000億行処理で演算時間が274.55時間から12.78時間になった。

## 設計のポイント

- SQL式、RapidsUDF、CUDAカーネルの順で書き換え方を選ぶ
- 検証駆動のフィードバックループでエージェントに変換の正しさと性能を確認させる

## 使いどころ

- UDFが多いSparkバッチをGPU化したいデータ基盤チーム
- コード移行にエージェントを使う場面
