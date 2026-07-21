---
type: case
title: 金融LLM推論ベンチマークSTAC-AI LANG6でNVIDIA Blackwellが記録更新
title_original: NVIDIA Blackwell Sets STAC-AI Record for LLM Inference in Finance
industry: financial-services
cloud:
- multi-cloud
patterns:
- inference-optimization
- rag
- document-processing
components:
- NVIDIA HGX B200
- Llama 3.1 8B Instruct
- Llama 3.1 70B Instruct
- NVIDIA TensorRT-LLM
- NVIDIA GH200
- RTX PRO 6000 Blackwell
- TensorRT Model Optimizer
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/nvidia-blackwell-sets-stac-ai-record-for-llm-inference-in-finance/
published_at: '2026-06-11'
---

## 概要

金融業界向けRAG/LLM推論ベンチマークSTAC-AI LANG6において、NVIDIA HGX B200(Blackwell)がEDGAR 10-Kファイリングの中長文要約タスクでLlama 3.1 8B/70B Instructモデルを用いたバッチ・インタラクティブ両モードで従来アーキテクチャ比最大2.8倍の性能を記録した。HPE・Supermicro・Lambdaの各プラットフォームでTensorRT-LLMとNVFP4/FP8量子化を用いて監査を実施し、Red Hat OpenShift上のコンテナ化環境でも計測可能なオーバーヘッドが生じないことを確認した。

## 設計のポイント

- リクエストのトークナイズやチャットテンプレート適用をサーバー側で行い、システムプロンプトを保護しつつCPU負荷も含めて計測する現実的なベンチマーク設計にする
- HopperにはFP8、BlackwellにはNVFP4量子化をそれぞれ適用し、各アーキテクチャで最も性能の出るカーネル構成を選ぶ
- バッチ(オフライン)とインタラクティブ(オンライン)の2モードを分けて計測し、スループットだけでなく到達時間や出力レートも評価する

## 使いどころ

- 決算報告書や有価証券報告書の要約・分析にLLMを使う金融機関のインフラ選定担当者
- オンプレ/クラウド複数ベンダーのGPU基盤を横断して推論性能を比較したい調達・ベンチマーク担当者
