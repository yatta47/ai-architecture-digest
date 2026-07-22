---
type: guidance
title: Azure AIサービス選定ガイド：エージェント・RAG・言語処理から独自モデル構築まで
title_original: Choose an AI services technology
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- rag
- document-processing
- multi-model-routing
components:
- Foundry Agent Service
- Foundry Models
- Azure AI Search
- Azure Document Intelligence
- Azure Content Understanding
- Azure OpenAI
- Azure Language
- Azure Translator
- Azure Speech
- Azure Vision
- Microsoft Azure AI Video Indexer
- Microsoft Azure AI Custom Vision
- Azure Machine Learning
- Foundry Local
- Content Safety
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/data-guide/technology-choices/ai-services
published_at: '2026-03-24'
---

## 概要

この記事はAzureが提供するAIサービス群を、エージェント・RAG・言語処理・音声・画像/動画処理などの機能カテゴリごとに整理し、要件に応じて適切な技術を選ぶための指針を示すガイダンスである。プリビルドのAIサービスで足りない場合にAzure Machine Learningで独自モデルを構築する使い分けや、オンデバイス推論向けのFoundry Localも紹介している。

## 設計のポイント

- まずプリビルドのAIサービス(SaaS型モデル)で要件を満たせないか検討し、独自モデル構築はAzure Machine Learningを使う最終手段として位置づける
- エージェント・RAG・言語処理・音声・画像/動画処理という機能カテゴリで技術を分類し、用途に応じたサービス選定をしやすくする
- コンテンツモデレーションにはContent Safetyを組み合わせ、有害コンテンツ検知をアーキテクチャに組み込む
- プライバシーやコストの制約がある場合はFoundry Localによるオンデバイス推論を選択肢に加える

## 使いどころ

- AI専門知識が少ないスタートアップや中小企業が、既存サービスの組み合わせで知的機能を素早く組み込みたい場合
- プリビルドモデルでは対応できない独自データ・独自要件があり、カスタムモデル構築が必要な場合
- エージェント構築・RAG・多言語処理・音声認識・画像/動画解析など、目的別に最適なAzureサービスを選定したいアーキテクト
- オンデバイス推論やコンテンツセーフティなど、プライバシーやガバナンス要件が強いユースケース
