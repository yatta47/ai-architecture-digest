---
type: case
title: 'AI-Native RAN: NVIDIA AI Aerialでスペクトル効率を最大化'
title_original: Maximize Spectral Efficiency with AI-Native RAN and NVIDIA AI Aerial
industry: telecom
cloud:
- on-prem
patterns:
- reinforcement-learning
- inference-optimization
components:
- NVIDIA AI Aerial
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/maximize-spectral-efficiency-with-ai-native-ran-and-nvidia-ai-aerial/
published_at: '2026-07-09'
---

## 概要

従来のRANはCPU性能に制約され、Massive MIMOの理論性能を発揮できていなかった。NVIDIA AI AerialはGPUによる並列計算でL1/L2アルゴリズムを刷新し、AIベースのビームフォーミングで最大1.62倍、DRLベースのリンクアダプテーションで1.3倍のスループット向上をフィールドトライアルで実証した。

## 設計のポイント

- 計算をCPU予算に合わせて簡略化するのではなく、GPUの並列性を前提にアルゴリズムそのものを再設計する『アルゴリズムファースト』の発想を取る
- UEペアリングやビームフォーミングなど組合せ爆発を伴う処理をGPUでバッチ化・並列化しリアルタイムAI推論を可能にする
- Nokiaなど業界パートナーと連携し、ソフトウェア定義RANとしてモデルの動的成長やセル間協調を段階的に拡張できるようにする

## 使いどころ

- 既存スペクトルから追加投資なしに容量を引き出したい通信事業者
- 5G-Advancedや6Gに向けてAIネイティブなRANアーキテクチャへ移行を検討する事業者
