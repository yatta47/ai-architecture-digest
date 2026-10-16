---
type: announcement
title: ローカルでコーディングエージェントを動かすRTX Spark開発PC
title_original: Code, Test, and Deploy on One Machine with NVIDIA RTX Spark
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- ai-agent
- inference-optimization
- fine-tuning
components:
- NVIDIA RTX Spark
- NVIDIA GB10
- Nemotron
- llama.cpp
- vLLM
- Ollama
- Unsloth
- PyTorch
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/code-test-and-deploy-on-one-machine-with-nvidia-rtx-spark/
published_at: '2026-10-16'
---

## 概要

NVIDIAはGB10と最大128GBの統合メモリを持つRTX Sparkで、ローカルのコーディングエージェント、ファインチューニング、コンパイルを1台で行えると紹介する。Microsoftと組んでWindows on ArmのPyTorch-CUDAなどの環境も整えた。

## 設計のポイント

- 推論・微調整・ビルドを1台に集約し、クラウドAPIやVMへの依存とトークン消費を減らす。
- ローカル向けに2ビット量子化したMoEモデルを用意し、既存の推論ランタイムで動かせるようにしている。
- WSLでクラウドと同じ環境を再現し、移行作業なしでデプロイできる。

## 使いどころ

- クラウドのトークンコストを抑えつつエージェント開発をしたい開発者。
- 機密コードを手元で扱いたいローカルAI開発の場面。
