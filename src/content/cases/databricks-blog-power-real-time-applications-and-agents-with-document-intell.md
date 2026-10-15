---
type: announcement
title: 文書到着時に即時処理するDocument IntelligenceのリアルタイムAPI
title_original: Power real-time applications and agents with Document Intelligence
company: Databricks
industry: cross-industry
cloud: []
patterns:
- document-processing
- ai-agent
- human-in-the-loop
components:
- Databricks Apps
- ai_parse_document
- ai_classify
- ai_extract
- ai_decide
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/power-real-time-applications-and-agents-document-intelligence
published_at: '2026-10-14'
---

## 概要

DatabricksはDocument Intelligenceの同期REST API（解析・分類・抽出はGA、判断はベータ）を公開した。文書到着時にアプリやエージェントから呼び、構造化して担当者やエージェントに回せる。

## 設計のポイント

- バッチではなく同期APIで到着直後に処理する
- 解析・分類・抽出・判断を分離して必要に応じ組み合わせる
- アプリやエージェントから呼び出し、次工程へのルーティングに使う

## 使いどころ

- 契約書・請求書・保険請求などを受け取ってすぐ振り分けたい業務部門
