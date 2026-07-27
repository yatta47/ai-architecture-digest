---
type: guidance
title: GKEで構築するクロスサイロ/クロスデバイス連合学習基盤
title_original: Cross-silo and cross-device federated learning on Google Cloud
industry: cross-industry
cloud:
- gcp
patterns:
- federated-learning
- confidential-computing
components:
- GKE
- TensorFlow Federated
- Cloud Storage
- Vertex AI TensorBoard
- Cloud Run
- Certificate Authority Service
outcome:
  type: risk-compliance
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/cross-silo-cross-device-federated-learning-google-cloud
published_at: '2026-07-19'
---

## 概要

GKE上にクロスサイロ型とクロスデバイス型の2種類の連合学習基盤を構築するリファレンスアーキテクチャ。プライベートGKEクラスタとテナント専用ノードプールでコンソーシアム参加組織のデータを分離し、TensorFlow FederatedベースのFederated Compute Platformでモデル集約を行う。

## 設計のポイント

- テナント専用ノードプールとTaint/VPCファイアウォールで参加組織ごとにワークロードを隔離する
- クロスデバイス構成ではDifferential Privacyを使ったAggregatorジョブで端末勾配を集約しプライバシーを担保する
- 機密GKEノードを使い使用中データも暗号化することでクロスデバイス構成のセキュリティを強化する

## 使いどころ

- 複数のGoogle Cloud組織/プロジェクトにまたがるコンソーシアムでモデルを共同学習したい場合
- スマートフォンなど大量デバイスからプライバシーを保ったまま学習したいモバイルサービス事業者
