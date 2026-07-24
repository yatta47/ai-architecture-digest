---
type: case
title: AT&TとMicrosoftがMicrosoft FoundryとAMDで兆トークン規模のワークロードを処理
title_original: AT&T and Microsoft scale trillion-token workloads with Microsoft Foundry and AMD
company: AT&T
industry: telecom
cloud:
- azure
patterns:
- multi-model-routing
- cost-optimization
- fine-tuning
components:
- Microsoft Foundry
- Microsoft Foundry Managed Compute
- Phi-4
- OSS-120B
- Gemma-4
- AMD Instinct MI300X
outcome:
  type: cost
source_id: azure-blog
source_name: Azure Blog
source_url: https://azure.microsoft.com/en-us/blog/att-and-microsoft-scale-trillion-token-workloads-with-microsoft-foundry-and-amd/
published_at: '2026-07-23'
---

## 概要

AT&Tは通信特化モデル群OTel2.0の開発のため、Microsoft Foundry Managed Compute上でPhi-4・OSS-120B・Gemma-4など複数のオープンモデルを約530基のAMD/NVIDIA GPUで使い分けた。約1兆トークンを処理し、フロンティアモデル利用と比べて数千万ドル規模のコストを削減した。

## 設計のポイント

- 単一モデルに標準化せず、データ準備・推論負荷の高いタスク・広範なモデル開発といった開発段階ごとに異なるオープンモデルを使い分けるマルチモデル戦略を採用する
- AMDとNVIDIAのGPUを混在させたヘテロジニアスな計算基盤により、要件変化に応じたデプロイの柔軟性を確保する
- フロンティアモデルではなくPhi-4などオープンモデルで合成データ生成を行うことで、大規模データ準備のコストを大幅に抑える

## 使いどころ

- 通信業界など専門ドメイン知識が必要なLLMをゼロから育てたい企業
- 複数のGPUアーキテクチャとオープンモデルを組み合わせて数千億〜兆トークン規模の学習・データ準備を行いたい場合
