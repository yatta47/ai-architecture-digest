---
type: guidance
title: Foundry Modelsを使うマルチテナントアプリの分離方式の選び方
title_original: Multitenancy and Foundry Models
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- multi-tenant-rag
- defense-in-depth
- cost-optimization
components:
- Microsoft Foundry
- Foundry Models
- Foundry Agent Service
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/service/foundry-models
published_at: '2026-10-13'
---

## 概要

SaaSでFoundry Modelsを使う際の分離方式を、テナント数、規制要件、モデルやバージョンの要求、テナント間の差異で選ぶためのガイド。サブスクリプション/リソースグループ境界やデプロイ種別で処理境界を分け、モデル数を抑えて運用を簡素化する。

## 設計のポイント

- 推論の処理境界(グローバル/データゾーン/地域)はデプロイ種別で決まり、専用サブスクリプションだけでは制約できない
- モデルをステートレスに使い、永続化に伴うテナント別データ分離を避ける
- テナント専用ファインチューニング等が要る場合のみデプロイを増やす

## 使いどころ

- AIを組み込むSaaSのマルチテナント設計者
- 規制要件の異なる顧客を同一基盤で扱う事業者
