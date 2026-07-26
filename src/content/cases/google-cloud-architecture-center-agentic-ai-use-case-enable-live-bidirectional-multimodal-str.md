---
type: guidance
title: リアルタイム映像・音声ストリームで技術支援と安全監視を同時に行うマルチエージェント
title_original: 'Agentic AI use case: Enable live bidirectional multimodal streaming'
industry: manufacturing
cloud:
- gcp
patterns:
- realtime-transcription
- multi-agent-orchestration
- video-intelligence
components:
- Gemini Live
- Agent Development Kit (ADK)
- Memorystore for Redis Cluster
- Compute Engine
- Cloud Run
outcome:
  type: quality
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/agentic-ai-bidirectional-multimodal-streaming
published_at: '2026-07-19'
---

## 概要

Google Cloudは、WebSocketで受信した映像・音声のライブストリームをGemini Liveで解析し、技術的な質問への回答と危険検知を同時に行うマルチエージェントシステムを示す。ディスパッチャーエージェントが必要に応じてアーキテクトエージェントから製品情報を取得し、リアルタイムに音声・字幕で応答を返す。

## 設計のポイント

- ADKのLiveRequestQueueでWebSocket経由の映像・音声をBlobとして継続的にストリームし、ディスパッチャーエージェントに渡す
- Gemini Liveがジェスチャーやフィラーワードなど無関係なイベントを除外し、関連するイベントのみをアーキテクトエージェントへの問い合わせにエスカレーションする
- 製品情報はMemorystore for Redis Clusterにキャッシュし、キャッシュミス時のみCompute Engine上のナレッジDBへ問い合わせてレイテンシを抑える
- 技術支援ワークフローと並行して、常時稼働の安全監視ワークフローがGeminiで映像フレームを監視し危険を検知した場合のみ警告を生成する

## 使いどころ

- 複雑な部品組み立てや修理手順をハンズフリーで支援したい製造・保守現場
- 作業中の閃光や蒸気など危険兆候をリアルタイムに検知し警告したい現場安全管理
