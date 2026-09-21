---
type: case
title: 14,000クラウドアカウントの日次コスト異常検知基盤
title_original: How BMW Group detects cost anomalies across 14,000 cloud accounts
company: BMW Group
industry: manufacturing
cloud:
- aws
patterns:
- cost-optimization
- event-driven
components:
- AWS Step Functions
- AWS Lambda
- Amazon S3
- Amazon QuickSight
- Prophet
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-bmw-group-detects-cost-anomalies-across-14000-cloud-accounts/
published_at: '2026-09-21'
---

## 概要

BMW GroupはData Replyと構築したFinOpsシステムCLEAで、14,000超のクラウドアカウントの日次コストをProphetで予測し、実績との乖離が閾値を超えたときだけアカウント所有者にメール通知する。Step FunctionsとLambdaのDistributed Mapで数十万件のアカウント×サービスの予測を約20分・月額50ドル程度の計算コストで処理する。

## 設計のポイント

- 固定の金額しきい値ではなく、アカウント・サービスごとに365日分の履歴からProphetでベースラインを学習し、正当な成長や新サービス導入を異常と誤検知しないようにする
- 予測モジュールを入力(アカウント別日次コスト)と出力(信頼区間付き予測値)のインターフェースで疎結合にし、検知・通知ロジックに触れずに予測エンジンを差し替え可能にする
- トレーリング3か月平均コストでアカウントを4クラスタに分け、クラスタごとに最小影響額(ドル)の閾値を変えることで、小規模アカウントの相対的な大幅スパイクを誤報にしない
- AWS Glue・Athena・EC2など元々分散が大きいサービスには標準の40%より高い60%の乖離率閾値を個別設定し、サービス特性に応じて検知感度を調整する

## 使いどころ

- 多数のクラウドアカウントを抱える大企業のFinOpsチームが、ダッシュボードの受動的な監視から能動的なアラート通知へ移行したい場合
- アカウントごとの正当な成長パターンを異常として誤検知しない、規模に応じた異常検知の閾値設計が必要な場面
- サーバーレス構成で低コスト・短時間に大規模な時系列コスト異常検知パイプラインを毎日運用したい場合
