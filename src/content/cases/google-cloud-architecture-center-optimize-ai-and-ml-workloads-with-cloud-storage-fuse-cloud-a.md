---
type: guidance
title: Cloud Storage FUSEでAI/ML学習・推論のストレージ性能を最適化する構成
title_original: Optimize AI and ML workloads with Cloud Storage FUSE
industry: cross-industry
cloud:
- gcp
patterns:
- ml-storage-optimization
components:
- Cloud Storage FUSE
- GKE
- Cloud Storage
- Cloud Load Balancing
outcome:
  type: speed
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/optimize-ai-ml-workloads-cloud-storage-fuse
published_at: '2026-07-19'
---

## 概要

GKE上のAI/ML学習・推論ワークロード向けに、Cloud StorageバケットをローカルファイルシステムとしてマウントできるCloud Storage FUSEを使ったリージョナル/マルチリージョナル2種類のリファレンスアーキテクチャを示す。マルチリージョナル構成ではRapid Cacheを併用し、レイテンシ低減とデータ転送費用の削減を図る。

## 設計のポイント

- 可用性・DR要件に応じてリージョナル構成とマルチリージョナル構成のどちらかを選ぶ
- Cloud Storage FUSEのファイルキャッシュでよく使うファイルをローカルにキャッシュし学習・推論のI/Oを高速化する
- マルチリージョン構成ではRapid Cacheでゾーンキャッシュヒットを高速化しつつマルチリージョンバケットのデータ転送費用を回避する

## 使いどころ

- GKE上で大規模モデルの学習・推論を行いCloud Storageの性能を底上げしたいチーム
- リージョン障害への耐性が必要なミッションクリティカルなAIワークロード
