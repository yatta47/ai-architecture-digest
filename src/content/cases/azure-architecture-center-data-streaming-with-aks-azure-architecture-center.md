---
type: guidance
title: AKSによるIoTセンサーのリアルタイムデータストリーミング基盤
title_original: Data streaming with AKS
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: speed
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/data-streaming-scenario
published_at: '2026-06-03'
---

## 概要

IoTセンサーや車両などから送られる大量のストリーミングデータを、AKS上のコンテナ化マイクロサービスで取り込み・処理・可視化するソリューションを解説する。取り込んだデータはCosmos DBに保存しつつApache KafkaとHDInsight(Spark)で非同期に分析し、処理結果はPostgreSQLとRedisを経てApp Service上のWebアプリで可視化する。自動車・リテール・医療・金融など大量データの即時分析が求められる領域に向く構成である。
