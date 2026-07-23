---
type: case
title: Azure MLとVision AIによる動画フレーム解析の自動化パイプライン
title_original: Automate video analysis by using Azure Machine Learning and Azure Vision in Foundry Tools
industry: media
cloud:
- azure
patterns:
- video-intelligence
- event-driven
components:
- Blob Storage
- Azure Machine Learning
- Data Lake Storage
- Azure Vision
- Azure Custom Vision
- Azure Logic Apps
- Microsoft Fabric
- Power BI
outcome:
  type: quality
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/analyze-video-computer-vision-machine-learning
published_at: '2026-03-06'
---

## 概要

動画をフレームへ分解し、Custom VisionとComputer Vision（OCR含む）で物体・テキストを自動抽出、Fabricで構造化してPower BIへ可視化するアーキテクチャ。手動での動画レビューを機械学習ベースの自動処理に置き換え、精度と再現性を高める。

## 設計のポイント

- FFmpegでのフレーム抽出パラメータ（fps・画質・形式）を分離設定し、下流の推論コストと精度をチューニング可能にする
- Logic AppsでBlob/Data Lakeへのアップロードをトリガーにし、推論からJSON整形までをイベント駆動で連結する
- 抽出結果はACID対応のFabric Data Warehouseに格納し、BI基盤とガバナンスされたアナリティクスを両立する

## 使いどころ

- 大量の監視・現場動画から特定オブジェクトやテキストを人手レビューなしで棚卸ししたいチーム
- Custom Visionでドメイン固有の物体検出を行いたいが、パイプライン全体は使い捨てで作りたくない場合
