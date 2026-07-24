---
type: announcement
title: 非同期バッチ処理向けMessage Batches API
title_original: Introducing the Message Batches API
company: Anthropic
industry: cross-industry
cloud:
- aws
- gcp
patterns:
- llmops
- cost-optimization
components:
- Anthropic Message Batches API
- Claude 3.5 Sonnet
- Claude 3 Opus
- Claude 3 Haiku
- Amazon Bedrock
- Google Cloud Vertex AI
outcome:
  type: cost
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/message-batches-api
published_at: '2024-10-08'
---

## 概要

リアルタイム性を要しない大量クエリを非同期に処理するMessage Batches APIを提供開始。1バッチ最大1万件のクエリを24時間以内に処理し、標準APIコールに比べ50%低コストで、レート制限を気にせず大規模データ処理を可能にする。

## 設計のポイント

- 同期APIとは別のレート制限枠を設け、大量リクエストでも通常トラフィックに影響を与えない設計にする
- 入出力トークンとも50%割引にすることで、大規模データセット分析のような非リアルタイム処理のコストを構造的に下げる

## 使いどころ

- 顧客フィードバックの分析や大量文書の翻訳・分類など即時応答が不要なバッチ処理
- 数百万ファイル規模の企業文書リポジトリを分析するような大規模データ処理
