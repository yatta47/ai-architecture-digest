---
type: guidance
title: Azure Content Understanding によるサーバーレス画像分類パイプライン
title_original: Image classification on Azure
industry: cross-industry
cloud:
- azure
patterns:
- event-driven
- document-processing
components:
- Azure Content Understanding
- Azure Functions
- Azure Blob Storage
- Azure Event Grid
- Azure Cosmos DB
- Azure AI Search
- Azure Machine Learning AutoML
outcome:
  type: cost
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/idea/intelligent-apps-image-processing
published_at: '2026-07-07'
---

## 概要

画像アップロードをEvent Gridでトリガーし、Azure FunctionsからContent Understanding(生成AI)を呼び出して構造化されたタグ・メタデータを抽出、Cosmos DBに保存するサーバーレスの画像分類アーキテクチャ。独自モデルの学習・運用を必要とせずに画像分類・タグ付けを実現する。

## 設計のポイント

- Blob StorageへのアップロードをEvent Gridでイベント化し、Functionsが期限付きSASでContent Understandingに画像アクセス権を渡すことで最小権限を保つ
- プリビルドアナライザーでカテゴリ・属性・ラベルを定義し、出力をそのままアプリのデータモデルにマッピングできるJSONとして受け取る
- ラベル済み学習データがあり決定的なモデルが必要な場合はAutoMLへ、プロンプト制御や視覚的QAが必要な場合はマルチモーダルモデル直接呼び出しへ切り替える判断軸を示す

## 使いどころ

- ファッションECサイトの商品画像タグ付けなど、独自モデルを持たずに画像分類を導入したい事業者
- 保険金請求の写真解析やゲームスクリーンショットからのコンテキスト抽出など高頻度の画像処理
