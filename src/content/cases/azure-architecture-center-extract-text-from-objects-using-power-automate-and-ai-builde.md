---
type: guidance
title: 画像内オブジェクトのテキスト抽出とSharePoint検索連携（AI Builder×Document Intelligence）
title_original: Extract text from objects using Power Automate and AI Builder
industry: manufacturing
cloud:
- azure
patterns:
- document-processing
- event-driven
components:
- AI Builder
- Azure AI Document Intelligence
- Power Automate
- Azure Functions
- SharePoint
- PnP Modern Search
- Azure Logic Apps
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/ai/extract-object-text
published_at: '2026-06-11'
---

## 概要

AI Builderのオブジェクト検出モデルとAzure AI Document IntelligenceのOCRを組み合わせ、画像内の図形やオブジェクトに埋め込まれたテキストを自動抽出してSharePointの検索インデックスに登録するPower Automateワークフローを紹介する。Azure Functionsでオブジェクトの座標とOCRテキストの座標を突き合わせ、どのテキストがどのオブジェクトに属するかを判定する。これにより、複雑な設計図や産業用ダイアグラム内の部品名などのテキストを手作業なしで検索可能にする。

## 設計のポイント

- AI Builderのオブジェクト検出結果とDocument IntelligenceのOCR結果を独立して取得し、ピクセル座標の重なりで両者を突き合わせることで、画像内の特定オブジェクトに紐づくテキストだけを抽出する
- ノーコード/ローコードのPower Automateでトリガーと連携を担い、座標マッチングのようなカスタムロジックだけをAzure Functionsに切り出すことで開発コストを抑える
- 抽出したメタデータをSharePoint検索インデックスに投入し、PnP Modern Search Web Partsで検索体験を提供することで既存のSharePoint基盤を活用する
- 処理量が多い場合はAzure Logic Appsへの切り替えを代替案として提示し、消費量の制約とコストのバランスを取れる設計にしている

## 使いどころ

- 配管や電気系統など多数の部品を含む複雑なエンジニアリング図面から特定コンポーネントを素早く検索したい設計・保守部門
- 製造ラインの機器図面からポンプやバルブなどの部品を自動識別し、予防保全やリスク管理の可視性を高めたい製造業
- リコールや故障通知の調査のために大量の図面や画像に埋め込まれたテキストを横断検索したい品質管理チーム
