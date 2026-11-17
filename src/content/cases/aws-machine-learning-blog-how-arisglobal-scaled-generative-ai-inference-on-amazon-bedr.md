---
type: case
title: 共有プロンプト接頭辞のキャッシュで生成AI推論コストを抑えた事例
title_original: How ArisGlobal scaled generative AI inference on Amazon Bedrock
company: ArisGlobal
industry: healthcare
cloud:
- aws
patterns:
- inference-optimization
- cost-optimization
- document-processing
- guardrails
components:
- Amazon Bedrock
- Amazon Bedrock Guardrails
- Claude
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-arisglobal-scaled-generative-ai-inference-on-amazon-bedrock/
published_at: '2026-11-17'
---

## 概要

ArisGlobalは有害事象報告PDFから約130項目を抽出するNavaXをBedrock上で運用している。顧客ごとの要件追加で共有プロンプト接頭辞が肥大化しコストが増えたため、文書ではなく共有接頭辞をキャッシュする順序に変更して実効入力コストを下げた。

## 設計のポイント

- リクエスト内の順序を見直し、再利用率の高い共有接頭辞をキャッシュ対象にした。
- マルチテナントでプロンプトが増えてもコストが比例しない構成にした。
- Guardrailsとスキーマ検証・原文根拠確認でPHIを扱う抽出精度と安全性を担保している。

## 使いどころ

- テナントごとに指示が増えるマルチテナントSaaSのLLM推論コスト最適化。
- 長い共通プロンプトを持つ文書抽出ワークロード。
