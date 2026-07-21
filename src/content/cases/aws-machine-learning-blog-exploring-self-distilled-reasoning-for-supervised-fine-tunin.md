---
type: guidance
title: Amazon Novaの自己蒸留で失われた推論能力を取り戻すSFT手法
title_original: Exploring self-distilled reasoning for supervised fine-tuning with Amazon Nova
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- fine-tuning
- llmops
components:
- Amazon Nova 2
- Amazon Nova 2 Lite
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/exploring-self-distilled-reasoning-for-supervised-fine-tuning-with-amazon-nova/
published_at: '2026-07-21'
---

## 概要

AWSは、推論トレースを含まないデータでSFTを行うとモデルの推論能力が失われる「reasoning suppression」問題を分析し、ベースモデル自身のCoTを再利用してデータを補強するSelf-Distilled Reasoning(SDR)を提案した。3つのベンチマークで、モデルマージと同等以上に数学性能を回復しつつ、目的タスクの性能もSFT単体より6.5%以上向上させた。

## 設計のポイント

- 推論トレースを含まないSFTデータでも、reasoning-onで学習・推論を統一しないと精度が伸びない。
- ベースモデル自身の推論トレースをSFTデータに混ぜ込むことで、教師モデルや人手アノテーションなしに壊滅的忘却を抑制できる。
- モデルマージによる能力回復よりも、目的タスク性能と汎化性能の両立で優位性がある。

## 使いどころ

- 推論トレース付きデータの収集コストが高く、既存のinput-outputのみのSFTデータセットを使い続けたいチーム。
- ドメイン特化のSFT後に数学・コーディングなど汎用能力の劣化(catastrophic forgetting)を防ぎたい場合。
