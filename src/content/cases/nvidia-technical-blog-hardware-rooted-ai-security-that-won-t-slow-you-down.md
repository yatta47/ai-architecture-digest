---
type: case
title: Confidential Computingでほぼ性能劣化なしにAI推論を保護
title_original: Hardware-Rooted AI Security That Won't Slow You Down
industry: cross-industry
cloud:
- multi-cloud
patterns:
- confidential-computing
- inference-optimization
components:
- NVIDIA Confidential Computing
- NVIDIA HGX B300
- NVIDIA Remote Attestation Service
- FlashInfer
- SGLang
- Qwen3.5-397B-A17B-FP8
outcome:
  type: risk-compliance
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/hardware-rooted-ai-security-that-wont-slow-you-down/
published_at: '2026-07-09'
---

## 概要

NVIDIA Confidential Computingはシリコンに焼き込まれた署名鍵とリモートアテステーションでモデル・データの機密性を保ちながらAI推論を実行する。HGX B300上でQwen3.5-397B-A17B-FP8を用いた検証では、CC有効時のスループット・レイテンシ劣化は多くの構成で8%未満にとどまった。

## 設計のポイント

- GPU製造時に焼き込まれ外部に露出しない秘密鍵をルートとし、CVMの状態をNRASで一度だけアテステーションして以降は追加レイテンシを発生させない
- FlashInferのCCセーフなオートチューナー、SGLangの非同期D2Hコピーやピースワイズ CUDA Graphなど、暗号化に伴うオーバーヘッドをフレームワーク側で個別に緩和する
- 1回あたりの起動オーバーヘッドを相対的に薄めるため、GPU起動あたりの作業量を増やす設計にする

## 使いどころ

- データ主権やモデル重みの機密性が求められる規制業種でAI推論をアウトソースしたい組織
- マルチテナント環境でモデル資産と顧客データを相互に隔離しつつ推論性能を落としたくないプラットフォーム事業者
