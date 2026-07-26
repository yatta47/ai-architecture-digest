---
type: guidance
title: ユーザーデータからパーソナライズ広告素材を自動生成するマーケティングコンテンツ基盤
title_original: 'Generative AI use case: Generate content for personalized marketing campaigns'
industry: media
cloud:
- gcp
patterns:
- document-processing
- human-in-the-loop
components:
- BigQuery
- Dataflow
- Eventarc
- Cloud Run
- Gemini API
- Cloud Storage
outcome:
  type: productivity
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/genai-marketing-campaigns
published_at: '2026-07-19'
---

## 概要

BigQueryに集約したユーザーデータをDataflowで分析してマーケティングインサイトを抽出し、Gemini APIでユーザーごとに音声・動画・テキストのパーソナライズ広告素材を自動生成するアーキテクチャ。生成物はWebポータルで各ユーザーに配信される。

## 設計のポイント

- Eventarcでデータ処理完了をトリガーにCloud Runサービスを起動し、生成フローをイベント駆動で自動化する
- 生成コンテンツをCloud Storageに公開する前に人間によるブランド・安全性チェックを挟む設計を推奨している
- キャンペーンの効果をモデルにフィードバックするループを構築し、生成品質を継続的に改善する余地を持たせている

## 使いどころ

- 大量の顧客セグメントごとに個別化した広告クリエイティブを効率的に量産したいマーケティングチーム
- デモグラフィック・購買履歴に基づくパーソナライズマーケティングをAIで自動化したいメディア・小売企業
