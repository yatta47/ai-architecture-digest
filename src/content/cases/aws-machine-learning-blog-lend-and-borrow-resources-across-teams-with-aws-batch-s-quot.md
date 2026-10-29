---
type: announcement
title: AWS BatchのクォータシェアでGPU学習ジョブをチーム間融通
title_original: Lend and borrow resources across teams with AWS Batch's quota management for SageMaker Training jobs
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- cost-optimization
- gpu-fleet-reliability
components:
- AWS Batch
- Amazon SageMaker AI
- SageMaker Python SDK
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/lend-and-borrow-resources-across-teams-with-aws-batchs-quota-management-for-sagemaker-training-jobs/
published_at: '2026-10-29'
---

## 概要

AWS BatchにSageMaker Trainingジョブ向けのクォータ管理が追加された。チームやプロジェクト単位のクォータシェアを定義し、余剰GPUを貸し借りしつつ優先度に応じてプリエンプションできる。

## 設計のポイント

- クォータシェアごとにRESERVE/LEND/LEND_AND_BORROWの共有戦略を選び、割当の保証と稼働率向上を両立する。
- 貸出中の容量はクロスシェア・プリエンプションで自動回収され、管理者が借用ジョブを探して止める必要がない。
- シェア内プリエンプションを有効にすれば高優先度ジョブを先に開始でき、チェックポイント前提のバックグラウンドジョブに向く。

## 使いどころ

- 複数チームでGPUを共有する学習基盤の管理者が、割当と稼働率を両立したい場面。
- チェックポイント付きの長時間学習と、即時開始が必要なジョブが混在する環境。
