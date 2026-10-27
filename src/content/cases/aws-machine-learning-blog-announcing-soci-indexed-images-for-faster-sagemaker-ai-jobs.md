---
type: announcement
title: SageMaker学習ジョブのコンテナ起動をSOCI遅延ロードで秒単位に短縮
title_original: Announcing SOCI-indexed images for faster SageMaker AI jobs
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- cost-optimization
components:
- Amazon SageMaker AI
- Amazon ECR
- Seekable OCI (SOCI)
- AWS Deep Learning Containers
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/announcing-soci-indexed-images-for-faster-sagemaker-ai-jobs/
published_at: '2026-10-27'
---

## 概要

SageMaker AIの学習・処理ジョブでSOCIインデックスによるコンテナイメージの遅延ロードが使えるようになった。起動に必要なファイルだけ先に取得し残りはバックグラウンドで読み込むため、数GB〜数十GBのイメージでも起動が数秒になり、ベンチマークでは画像プル中のGPUアイドル時間が最大90%減った。

## 設計のポイント

- SOCIインデックスは元イメージとは別のOCIアーティファクトとしてECRに置くため、イメージダイジェストや既存署名を壊さない。
- インデックスが無い・読めない場合は通常ダウンロードにフォールバックし、導入しても既存ジョブが壊れない設計にしている。
- ジョブ定義やエントリポイントの変更が不要で、事前インデックス済みDLCを指定するだけで採用できる。

## 使いどころ

- ハイパーパラメータ探索のように大量の短いジョブを回すチーム。
- 10GB超のDLCを使う学習・処理ジョブの起動待ちコストを下げたい場面。
