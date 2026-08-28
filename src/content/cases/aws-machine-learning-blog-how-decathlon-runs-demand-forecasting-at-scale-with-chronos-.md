---
type: case
title: Decathlon、時系列基盤モデルChronos-2で全世界の需要予測を刷新
title_original: How Decathlon runs demand forecasting at scale with Chronos-2
company: Decathlon
industry: retail
cloud:
- aws
patterns:
- fine-tuning
- llmops
- inference-optimization
components:
- Amazon SageMaker AI
- Amazon EC2
- Chronos-2
- AutoGluon
- MLflow
- Databricks
- Apache Airflow
- PySpark
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-decathlon-runs-demand-forecasting-at-scale-with-chronos-2/
published_at: '2026-08-28'
---

## 概要

Decathlonは80以上のスポーツ・数万点の商品を対象に週次で需要予測を行うシステムを、DeepARやTFTのような個別学習モデルから時系列基盤モデルChronos-2へ刷新した。101回のローリング評価によるベンチマークでゼロショットでも既存本番モデルに匹敵し、6か月おきのLoRAファインチューニングでさらに精度を高めた。EC2上のCPU/GPUバッチ推論とMLflowによるモデル管理で、複数の供給地域に運用負荷を抑えて展開している。

## 設計のポイント

- 時系列基盤モデルをゼロショットでまず評価し、既存本番モデルとのWAPE比較でtraining不要の実用性を検証する
- LoRAによる低頻度（半年ごと）ファインチューニングで、フル再学習なしに精度改善とコストのバランスを取る
- 推論はCPUインスタンス(m6i.8xlarge)、ファインチューニングはGPUインスタンス(g5.4xlarge)と用途別にコンピュートを使い分ける
- 地域ごとにモデルをMLflowでバージョン管理し、供給地域拡大に耐えるパイプライン構成にする

## 使いどころ

- 多数の商品・地域で個別モデル運用の維持コストが高くなっている小売企業の需要予測刷新
- 毎週の再学習が必要な旧来モデルからの移行で運用負荷を下げたい場合
- 12週間の補充計画や52週間の戦略計画など複数ホライズンの予測を一つの基盤モデルで賄いたい場合
