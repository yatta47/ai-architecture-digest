---
type: guidance
title: Azure Stream Analyticsによるタクシー配車データのリアルタイムストリーム処理
title_original: Stream processing with Azure Stream Analytics
ai_relevant: false
industry: logistics
cloud:
- azure
patterns: []
components: []
outcome:
  type: speed
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/data/stream-processing-stream-analytics
published_at: '2026-05-30'
---

## 概要

2系統のイベントストリーム（乗車データと運賃データ）をEvent Hubsで受け取り、Stream Analyticsで時間窓内に相関させてマイルあたりチップ額の移動平均を計算し、Cosmos DBに書き込んでPower BIで可視化するエンドツーエンドのストリーム処理参照アーキテクチャ。
