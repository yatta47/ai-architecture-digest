---
type: announcement
title: Amazon Bedrock、インド国内リージョン限定ルーティングでOpenAIモデルのデータレジデンシーに対応
title_original: Introducing OpenAI models on Amazon Bedrock for in-country inferencing in India
industry: cross-industry
cloud:
- aws
patterns:
- data-residency-inference
- llm-gateway
components:
- Amazon Bedrock
- OpenAI GPT-5.6
- Amazon Bedrock Guardrails
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-openai-models-on-amazon-bedrock-for-in-country-inferencing-in-india/
published_at: '2026-08-27'
---

## 概要

Amazon Bedrockはインドのムンバイ・ハイデラバードの2リージョン間だけでリクエストをルーティングする『インド地理的クロスリージョン推論』を導入し、OpenAIのGPT-5.6 Terra/LunaモデルをインドData域内で処理できるようにした。OpenAI互換のResponses/Chat Completions APIやBedrock標準のConverse APIから同じ推論プロファイルを呼び出せ、金融・医療・公共部門などデータ処理をインド国内に留める必要があるワークロードに対応する。

## 設計のポイント

- 『in.』プレフィックスの地理限定推論プロファイルと『global.』プレフィックスの広域プロファイルを使い分け、データレジデンシー要件の有無で切り替える
- 課金・クォータはリクエスト送信元リージョンに紐づけ、実際に処理した先リージョンに関わらず監視ログを一箇所に集約する
- OpenAI SDKをそのままBedrockのOpenAI互換エンドポイントに向けられるようにし、既存のOpenAI依存コードの移行コストを下げる
- ゼロデータ保持（ZDR）をデフォルトとしつつ、不正利用検知にヒットしたコンテンツのみ例外的に保持するポリシーを明示する

## 使いどころ

- 金融・医療・公共部門など、法規制でデータ処理を国内に限定する必要があるインド向けAIアプリケーション
- 既存のOpenAI SDKベースのアプリケーションを、コード変更を最小限にBedrock経由へ移行したい場合
- 国内リージョン限定と広域キャパシティ利用を要件に応じて使い分けたいマルチリージョン展開
