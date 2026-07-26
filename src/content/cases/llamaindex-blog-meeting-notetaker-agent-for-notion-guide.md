---
type: case
title: Zoom RTMSとLlamaIndexで作る議事録自動作成エージェント
title_original: Create a Meeting Notetaker Agent for Notion with LlamaIndex and Zoom RTMS
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- ai-agent
- event-driven
- realtime-transcription
components:
- Zoom RTMS
- LlamaIndex Workflows
- Notion API
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/create-a-meeting-notetaker-agent-for-notion-with-llamaindex-and-zoom-rtms
published_at: '2026-07-19'
---

## 概要

Zoomの新機能RTMSが配信するリアルタイム会議データ（発話トランスクリプト・参加者の入退室・終了イベント）を、LlamaIndexのイベント駆動エージェントワークフローで受け取り、Notion上に会議メモページを自動作成・ToDo追記・終了時要約までを行うエージェントの実装例を紹介する。

## 設計のポイント

- Zoom RTMSの各イベント（開始・発話チャンク・終了）をLlamaIndex Workflowsのカスタムイベントにマッピングし、イベントごとに専用ステップを割り当てる
- 発話を一定量チャンク化してからLLMにアクションアイテム抽出をさせることで、逐次LLM呼び出しのコストと精度のバランスを取る
- 会議終了イベントで全トランスクリプトをまとめて要約するステップを分離し、リアルタイム処理と事後要約を役割分担する

## 使いどころ

- Web会議の議事録作成やToDo抽出を自動化したい社内ツール担当者
- リアルタイムイベントストリームを受けてマルチステップのAIエージェントを組みたい開発者
