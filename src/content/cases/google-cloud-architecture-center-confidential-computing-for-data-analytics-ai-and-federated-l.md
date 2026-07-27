---
type: guidance
title: 機密コンピューティングで実現するAIモデル学習と連合学習のデータ保護
title_original: Confidential computing for data analytics, AI, and federated learning
industry: cross-industry
cloud:
- gcp
patterns:
- confidential-computing
components:
- Confidential VM
outcome:
  type: risk-compliance
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/security/confidential-computing-analytics-ai
published_at: '2026-07-19'
---

## 概要

ハードウェアベースのTEE(信頼実行環境)により処理中のデータも暗号化して保護する機密コンピューティングの概要と、AIモデル学習・連合学習・複数組織間のデータ協業への応用をまとめたガイド。医療・金融分野でのGDPR/HIPAA準拠や複数病院間の連合学習など具体的なユースケースを紹介する。

## 設計のポイント

- TEEはメモリ上のデータを常に暗号化し、ハードウェア攻撃者からもデータを保護する
- アテステーションにより計算が意図した安全な環境で実行されたことを暗号学的に検証できる
- Confidential VMや機密GPUを使うことで生データを他組織に開示せずに共同でモデル学習できる

## 使いどころ

- 複数の病院間で患者データを共有せずに画像診断の連合学習モデルを構築したい医療機関
- 金融機関同士が個々のデータを開示せずに不正検知モデルを共同開発したい場合
