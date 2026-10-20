---
type: guidance
title: オープンウェイトモデルのエンタープライズ向けリスク管理
title_original: Managing open-weight model risk in enterprise deployments
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- guardrails
- policy-as-code
components:
- Azure
- NVIDIA
outcome:
  type: risk-compliance
source_id: azure-blog
source_name: Azure Blog
source_url: https://azure.microsoft.com/en-us/blog/managing-open-weight-model-risk-in-enterprise-deployments/
published_at: '2026-10-16'
---

## 概要

MicrosoftとNVIDIAは、ISOやNIST AI RMFに基づくリスク分類と管理手法を示す白書を公開した。重みの公開有無だけではリスクは決まらず、モデル、用途、展開、安全対策によって決まるという考え方である。

## 設計のポイント

- オープンかクローズドかではなく、用途と起こり得る問題から必要な証拠と統制を決める。
- ISOやNISTなど既存の標準にリスク分類を合わせる。

## 使いどころ

- オープンウェイトモデルの採用可否を評価する企業のリスク部門。
- モデル導入時の安全対策の責任範囲を整理したい場面。
