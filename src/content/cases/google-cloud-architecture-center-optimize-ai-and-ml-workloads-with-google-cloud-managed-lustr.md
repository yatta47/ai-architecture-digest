---
type: guidance
title: Google Cloud Managed LustreでAI学習・チェックポイント処理を高速化する構成
title_original: Optimize AI and ML workloads with Google Cloud Managed Lustre
industry: cross-industry
cloud:
- gcp
patterns:
- ml-storage-optimization
components:
- Managed Lustre
- GKE
- Cloud Storage
- Cloud Storage FUSE
outcome:
  type: speed
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/optimize-ai-ml-workloads-managed-lustre
published_at: '2026-07-19'
---

## 概要

PiB級・サブミリ秒レイテンシの並列ファイルシステムであるGoogle Cloud Managed LustreをGKE上のAI学習・推論ワークロードに使うリファレンスアーキテクチャ。学習用に転送したデータをそのままLustre上でチェックポイントにも使い、同一インスタンスを推論配信にも再利用することでリソース効率を高める。

## 設計のポイント

- Cloud Storageを長期保存のソースオブトゥルースとし、学習時はManaged Lustreにデータをインポートして高速化する
- 学習で使ったManaged Lustreインスタンスを同じゾーンのままサービング(推論配信)にも再利用しリソース効率を高める
- チェックポイントを高頻度でManaged Lustreに保存し、必要な世代だけCloud Storageへエクスポートして長期保管する

## 使いどころ

- 大規模データセット・大規模モデルでI/Oがボトルネックになっている学習ワークロード
- 高頻度チェックポイントとPiB級ストレージが必要な基盤モデル開発チーム
