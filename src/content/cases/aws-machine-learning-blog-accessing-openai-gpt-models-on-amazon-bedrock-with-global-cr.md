---
type: guidance
title: アジア太平洋5地域からBedrockでGPT-6にグローバルCRISでアクセス
title_original: Accessing OpenAI GPT models on Amazon Bedrock with global cross-Region inference
industry: cross-industry
cloud:
- aws
patterns:
- llm-gateway
components:
- Amazon Bedrock
- OpenAI GPT-6
- AWS IAM
- CloudWatch
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/accessing-openai-gpt-models-on-amazon-bedrock-with-global-cross-region-inference-in-thailand-malaysia-singapore-indonesia-and-taiwan/
published_at: '2026-10-12'
---

## 概要

タイ・マレーシア・シンガポール・インドネシア・台湾から、グローバルなクロスリージョン推論プロファイルでGPT-6系にアクセスする手順を、Converse API、IAM/SCP設定、クォータ、監視まで説明する。

## 設計のポイント

- プロファイルIDをモデルIDの代わりに渡して容量を確保する。
- 課金・クォータ・CloudTrailは送信元リージョンに残る。
- IAMとSCPで利用可能なプロファイルを制御する。

## 使いどころ

- 単一リージョンのスロットリングを避けたいチーム。
