---
type: guidance
title: Maia 300の構成：ソフトウェア定義データフローによる推論最適化
title_original: Deep dive into Azure Maia 300 architecture
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- inference-optimization
- cost-optimization
components:
- Azure Maia 300
- Azure Maia 200
- Microsoft Foundry
- GitHub Copilot
outcome:
  type: cost
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://azure.microsoft.com/en-us/blog/deep-dive-into-azure-maia-300-architecture/
published_at: '2026-10-13'
---

## 概要

Maia 300は長コンテキスト推論・デコード中心の処理に合わせ、メモリをチップレット間でNUMA化し、狭精度形式でトークンあたりの移動データを減らし、ラックを96アクセラレータへ倍増した。有用トークン/ワットと/ドルの最大化を狙う。

## 設計のポイント

- 制御パスとデータパスを分け、データ配置・移動・変換をソフトウェアで明示的に制御する
- 狭精度形式とハードウェア変換で移動バイト数を削減する
- アクセラレータだけでなくネットワークやラック、データセンターまで同時設計する

## 使いどころ

- LLM推論基盤のハードウェア動向を把握したい設計者
- エージェント負荷に合うインフラ要件を検討する担当者
