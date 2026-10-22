---
type: guidance
title: TTS推論エンドポイントのオートスケール目標を実測2値から算出する手法
title_original: Stop guessing auto scaling targets for TTS on Amazon SageMaker AI
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- cost-optimization
components:
- Amazon SageMaker AI
- Kokoro-82M
- AWS CDK
- Amazon CloudWatch
- Amazon ECR
- Amazon S3
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/stop-guessing-auto-scaling-targets-for-tts-on-amazon-sagemaker-ai/
published_at: '2026-10-22'
---

## 概要

自社ホストのTTS（Kokoro-82M）をSageMakerリアルタイムエンドポイントで動かし、オートスケールの目標値を勘ではなく実測から導く方法を示す。1インスタンスがSLO内で捌ける最大同時実行数Q_maxとスケールアウト所要時間T_totalを計測し、閾値とクールダウンを算術で導出する。

## 設計のポイント

- スケール指標にSageMakerが自前で発行するConcurrentRequestsPerModelを使い、カスタムメトリクス未送信という失敗を避ける。
- クライアント計測の平均同時数とCloudWatchのMaximum統計の比を各負荷段で測り、閾値を換算してから設定に反映する。
- 実測プランが存在するときだけオートスケール資源を生成するゲート（scaling_enabled）をCDKに置き、未検証の設定が本番に出ないようにする。

## 使いどころ

- TTSなど長時間接続を保持する非自己回帰モデルの配信でスケール設計をする場面。
- GPUの遊休コストとSLO違反リスクの両方を抑えたい推論基盤の運用担当。
