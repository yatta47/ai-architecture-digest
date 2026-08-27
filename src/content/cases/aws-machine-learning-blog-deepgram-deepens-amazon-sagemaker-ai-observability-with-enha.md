---
type: announcement
title: Deepgram音声AIのSageMaker課金・エンジン可視化を強化
title_original: Deepgram deepens Amazon SageMaker AI observability with Enhanced Metrics
company: Deepgram
industry: cross-industry
cloud:
- aws
patterns:
- llmops
- cost-optimization
components:
- Amazon SageMaker AI
- Amazon CloudWatch
- AWS Marketplace
- Prometheus
- OpenTelemetry
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/deepgram-deepens-amazon-sagemaker-ai-observability-with-enhanced-metrics/
published_at: '2026-08-27'
---

## 概要

Amazon SageMaker AI上で動くDeepgramの音声認識/音声合成モデルが、課金・利用状況メトリクスをCloudWatchへ直接publishするEnhanced Metricsと、GPUごとのエンジン内部指標を取得できるPrometheus/OpenTelemetry対応を追加した。いずれもAWS Marketplaceのネットワーク分離制約下で、サイドカーや追加IAM権限なしに動作する。

## 設計のポイント

- CloudWatch Embedded Metric Format（EMF）でコンテナstdoutログをそのままメトリクス化し、ネットワーク分離下でも追加の送信経路なしに指標を取得
- 課金用のDeepgram/SageMakerInference名前空間と、機能利用実態用のDeepgram/SelfHosted名前空間を分離し、コストと利用パターンを別軸で追跡
- 集約された課金メトリクスとは別に、Prometheus/OpenTelemetryでper-endpoint・per-GPUの詳細なエンジン指標を取得できるようにし用途に応じて使い分け

## 使いどころ

- AWS Marketplaceのネットワーク分離下でベンダーコンテナの課金・利用実態を可視化したいプラットフォームチーム
- 音声AIのGPU利用状況やコストをモデル・トランスポート単位で分析したいFinOps/SRE担当
