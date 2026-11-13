---
type: guidance
title: Bedrock推論コストを左右する4つのリクエスト設定
title_original: Four Amazon Bedrock inference choices that affect cost
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- cost-optimization
- inference-optimization
components:
- Amazon Bedrock
- Converse API
- Prompt caching
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/four-amazon-bedrock-inference-choices-that-affect-cost/
published_at: '2026-11-12'
---

## 概要

キャッシュ期間、サービスティア、推論エフォート、maxTokensの4つが、モデルやプロンプトを変えずにBedrockの推論コストへ影響することを検証し、レスポンスのメタデータやログ、請求データで効果を確認する方法を示す。

## 設計のポイント

- キャッシュTTLは長いほど安いとは限らず、書き込みと読み出しの単価で判断する。
- 効果はレスポンスのusageメタデータと請求データで検証する。
- 設定の効果はモデルとワークロードに依存するため個別に測る。

## 使いどころ

- プロンプト調整後もBedrock費用が下がらないチーム。
- FinOps担当者が推論パラメータ単位の削減策を探すとき。
