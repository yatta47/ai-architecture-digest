---
type: announcement
title: 'LlamaIndexニュースレター: FlowMakerビジュアルエージェントビルダーやS3ベクトルストア統合など'
title_original: LlamaIndex Newsletter 2025-07-29
company: LlamaIndex
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- document-processing
- voice-agent
components:
- FlowMaker
- LlamaParse
- S3VectorStore
- Gemini Live
- n8n
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-07-29
published_at: '2026-07-19'
---

## 概要

LlamaIndexの週次ニュースレターで、ノーコードでエージェントを構築できるビジュアルビルダー「FlowMaker」、AWS S3と統合したベクトルストア「S3VectorStore」、Gemini Liveによる音声エージェント統合、型安全なワークフロー状態管理などの新機能をまとめて紹介する。

## 設計のポイント

- ノーコードのドラッグ&ドロップでエージェントを構築できるFlowMakerにより、条件分岐やループバックを持つワークフローを組めるようにする
- S3VectorStoreによりAWS S3のスケーラビリティとベクトル検索を統合し、大規模文書コレクションに接続するエージェントワークフローに対応する
- Context/Typed Stateサポートによりワークフローの状態管理をPydanticモデルで型安全に扱う

## 使いどころ

- コードを書かずにエージェントのワークフローをプロトタイピングしたいチーム
- 音声アシスタントやマルチモーダルレポート生成など新しいエージェントUXを試したい開発者
