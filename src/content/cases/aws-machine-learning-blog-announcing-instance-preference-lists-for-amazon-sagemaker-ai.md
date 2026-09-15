---
type: announcement
title: SageMakerの学習ジョブがGPUインスタンス優先順位リストで自動フォールバック起動
title_original: Announcing instance preference lists for Amazon SageMaker AI training jobs
industry: cross-industry
cloud:
- aws
patterns:
- gpu-fleet-reliability
- cost-optimization
components:
- Amazon SageMaker AI
- Flexible Training Plans
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/announcing-instance-preference-lists-for-amazon-sagemaker-ai-training-jobs/
published_at: '2026-09-15'
---

## 概要

SageMakerのトレーニング/処理ジョブに最大5つのインスタンスタイプを優先順位付きで指定でき、プラットフォームが1回のAPI呼び出しで空き容量を持つタイプを自動選択して起動するInstance Preference Listsを発表。手動リトライスクリプトを不要にする。

## 設計のポイント

- ジョブ作成時に優先順位付きインスタンスリストを渡し、容量取得の自動フォールバックを実現する
- Flexible Training Planの予約容量を優先評価してからon-demandにフォールバックする
- MaxPendingTimeInSecondsでリスト全体の待機時間を上限設定する

## 使いどころ

- 複数のGPUインスタンスファミリーで同等に動くジョブを持つチームが容量不足による待ち時間を減らしたい場合
- 夜間の再学習パイプラインなど時間に厳しいワークロードでInsufficientCapacityErrorによる失敗を避けたい場合
