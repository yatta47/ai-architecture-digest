---
type: case
title: VLMと勾配ブースティングで商品ページの品質を総合評価
title_original: How Amazon Marketplace evaluates content quality with Amazon SageMaker AI
company: Amazon
industry: retail
cloud:
- aws
patterns:
- eval
- fine-tuning
components:
- Amazon SageMaker AI
- Vision-Language Model
- CatBoost
- SHAP
- OCR
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-amazon-marketplace-evaluates-content-quality-with-amazon-sagemaker-ai/
published_at: '2026-11-05'
---

## 概要

Amazon MarketplaceがA+ Contentの品質を、ページ全体を1枚のスナップショットとしてVLMに評価させ、OCRの可読性指標と合わせてCatBoostで判定する手法を紹介した事例。SHAPで説明可能にして改善提案を生成し、SageMaker AI上で運用する。

## 設計のポイント

- 素材ごとではなく、レンダリングしたページ全体をVLMで評価し、要素間の整合を捉える。
- VLMの意味スコアとOCR可読性をCatBoostで融合し、専門家アノテーションで学習する。
- SHAPで判定理由を示し、数値だけでなく改善提案に変換する。
- データ取り込みから監視までSageMaker AI上でエンドツーエンドに実装する。

## 使いどころ

- 自由度の高いコンテンツの品質を大規模に評価したいECプラットフォーム。
- スコアに加えて改善提案を出したい出品者支援。
