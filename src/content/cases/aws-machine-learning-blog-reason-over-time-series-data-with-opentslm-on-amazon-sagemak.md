---
type: announcement
title: 時系列言語モデルOpenTSLMがSageMaker JumpStartで利用可能に
title_original: Reason over time-series data with OpenTSLM on Amazon SageMaker JumpStart
company: Aionic Labs
industry: cross-industry
cloud:
- aws
patterns:
- fine-tuning
- inference-optimization
components:
- OpenTSLM
- TimeNet
- Amazon SageMaker JumpStart
- Nexthink
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/reason-over-time-series-data-with-opentslm-on-amazon-sagemaker-jumpstart/
published_at: '2026-11-17'
---

## 概要

Aionic Labsの時系列言語モデルOpenTSLMがSageMaker JumpStartで提供開始された。センサー値等の数値と保守記録などの文脈を併せて解釈し、NexthinkのプロアクティブなIT支援の例も紹介している。TimeNetを使って自社データへ適応する手順も示す。

## 設計のポイント

- 数値時系列を汎用LLMにテキスト化して渡さず専用モデルで扱いトークンを抑える。
- TimeNetで学習・評価データの形式とAPIを統一する。

## 使いどころ

- 設備や運用メトリクスの異常を早期に解釈したい産業・IT運用チーム。
