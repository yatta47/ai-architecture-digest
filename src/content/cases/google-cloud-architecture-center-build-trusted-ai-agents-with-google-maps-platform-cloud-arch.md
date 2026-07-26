---
type: guidance
title: Google MapsとGoogleカレンダーでグラウンディングした旅程作成マルチエージェント
title_original: Build trusted AI agents with Google Maps Platform
industry: cross-industry
cloud:
- gcp
patterns:
- multi-agent-orchestration
- parallel-execution
components:
- Gemini Enterprise
- Agent Development Kit (ADK)
- Google Maps Platform
- Google Calendar
- Cloud Logging
- Firestore
- Cloud Run
outcome:
  type: quality
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/agentic-ai-system-with-grounding-using-maps
published_at: '2026-07-19'
---

## 概要

Google Cloudは、Google Maps PlatformとGoogleカレンダーの実世界データでグラウンディングした旅程プランニング用マルチエージェントシステムを示す。オーケストレーターエージェントが場所・ルート・スケジュールの専門エージェントを調整し、営業時間や移動時間、予定の重複を踏まえた1日の計画を生成する。

## 設計のポイント

- オーケストレーターがPlaces・Routes・Scheduleの専門エージェントを調整し、場所検索とスケジュール確認を並列実行することで性能を向上させる
- 各エージェントに最小権限のツールとデータのみを与え（例：Scheduleエージェントは特定カレンダーのみ読み書き可）、ゼロトラストの原則を徹底する
- 非払い戻しチケットの予約など重要タスクにはヒューマン・イン・ザ・ループの検証を組み込み、エージェントの判断過程をCloud LoggingとFirestoreで監査可能にする
- 頻出ルートや人気スポットのデータをキャッシュしてAPI呼び出し回数を抑え、エージェントのタスク範囲を厳密にスコープしてコストを管理する

## 使いどころ

- 出張の航空券・ホテル手配から会議日程調整までを自動化したい法人向け出張管理
- 現場担当者の位置とスケジュールから最適な技術者を割り当てたいフィールドサービス事業者
- 天候による配送ルート変更と顧客通知を自動化したい物流企業
