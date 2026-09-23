---
type: announcement
title: Amazon BedrockでGPT-6 SolとGPT-6 Lunaが利用可能に
title_original: Bring more intelligence to everyday work with GPT-6 Sol and GPT-6 Luna on Amazon Bedrock
company: OpenAI
industry: cross-industry
cloud:
- aws
patterns:
- multi-model-routing
- cost-optimization
- ai-agent
components:
- Amazon Bedrock
- GPT-6 Sol
- GPT-6 Luna
- GPT-6 Astra
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/bring-more-intelligence-to-everyday-work-with-gpt-6-sol-and-gpt-6-luna-on-amazon-bedrock/
published_at: '2026-09-22'
---

## 概要

GPT-6 SolとGPT-6 LunaがAmazon Bedrockで一般提供となった。Solは日常的な複雑なコーディングや多段処理向け、Lunaは大量の抽出・要約・分類向けで、どちらもGPT-5.6より低いAPI価格とされる。

## 設計のポイント

- 用途ごとにAstra、Sol、Lunaを使い分け、知能と効率のバランスを調整する。
- 評価指標を単価ではなく、品質・トークン・リトライ・遅延を含む成果に至る総コストとしている。
- 大量処理では軽量モデルを使い、1呼び出しの差が積み上がる費用を抑える。

## 使いどころ

- Bedrock上で用途別にモデルを切り替えたい開発チーム。
- 文書パイプラインで抽出・分類を大量に回す担当者。
- コーディングエージェントのコストと品質を両立させたい組織。
