---
type: guidance
title: 画像・動画処理タスクに応じたAzure AIサービスの選定指針
title_original: Choose an Azure AI image and video processing and generation technology
industry: cross-industry
cloud:
- azure
patterns:
- video-intelligence
- document-processing
- multi-model-routing
components:
- Azure OpenAI
- GPT-4o
- DALL-E
- GPT-image
- Whisper
- Azure Vision
- Azure AI Custom Vision
- Azure Content Understanding
- Azure AI Video Indexer
- Azure Document Intelligence
- Content Safety
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/data-guide/ai-services/image-video-processing
published_at: '2026-03-24'
---

## 概要

本記事は、Azure Foundry Toolsが提供する画像・動画処理系AIサービス群(Azure OpenAI、Azure Vision、Custom Vision、Content Understanding、Video Indexer)の使い分けを整理したガイドである。自然言語からの画像生成や広範な視覚解析にはAzure OpenAI、OCRや顔検出などの特化タスクにはAzure Vision、スキーマ定義抽出やRAG向け動画処理にはContent Understanding、動画・音声からの深い洞察抽出にはVideo Indexerを使うべきと整理している。

## 設計のポイント

- 用途を『生成・広範な多モーダル解析』と『特化型の視覚/顔検出タスク』に分け、前者はGPT-4oやDALL-EなどAzure OpenAI系モデル、後者はAzure Visionの専用APIに振り分ける
- スキーマ駆動の構造化フィールド抽出やRAG向け動画出力が必要な場合はAzure Content Understandingを選び、汎用モデルでの代替を避ける
- 高度なカスタマイズ(話者分離・カスタム語彙)を伴う大量音声文字起こしはAzure Speechなど専用サービスに委譲し、Azure OpenAIの音声APIとは適用範囲を分離する
- コンテンツモデレーションは専用のContent Safetyに任せ、Azure Visionの画像解析機能と責務を混同しない

## 使いどころ

- 特定業界に依存せず、社内文書のOCR化やアクセシビリティ用alt text自動生成を行いたい開発者
- スキーマに沿った構造化データを画像・動画から抽出しRAGパイプラインに投入したいシステム設計者
- ライブ配信や大量アーカイブ動画から人物・トピック・場面を横断的に検索可能にしたい運用チーム
- リアルタイム音声対話やナレーション生成など低遅延の音声AI機能を組み込みたいプロダクトチーム
