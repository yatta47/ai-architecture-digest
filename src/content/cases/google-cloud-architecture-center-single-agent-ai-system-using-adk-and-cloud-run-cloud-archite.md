---
type: guidance
title: ADKとCloud Runで構築する単一エージェントAIシステム
title_original: Single-agent AI system using ADK and Cloud Run
industry: cross-industry
cloud:
- gcp
patterns:
- ai-agent
components:
- Agent Development Kit (ADK)
- Cloud Run
- Gemini
- Gemini Enterprise Agent Platform
- Model Context Protocol (MCP)
- MCP Toolbox for Databases
- Google Cloud Observability
outcome:
  type: productivity
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/single-agent-ai-system-adk-cloud-run
published_at: '2026-07-19'
---

## 概要

Google Cloudは、ADKで構築しCloud Run上にデプロイする単一エージェントAIシステムのリファレンスアーキテクチャを示す。MCP Toolbox for Databasesなどのツールでコンテキストを取得し、バグ報告のトリアージ自動化やカスタマーサービスのユースケースに適用する例を紹介する。

## 設計のポイント

- エージェントはADKで構築しCloud Runにサーバーレスでデプロイし、Agent RuntimeやGKEも代替ランタイムとして選択できる
- MCPでツールとのやり取りを標準化し、MCP Toolbox for Databasesでコネクションプーリングや認証などデータベース接続の複雑さを吸収する
- Cloud Monitoring・Logging・Traceでエージェントの挙動・健全性・性能を継続的に可視化する

## 使いどころ

- 重複調査や技術的コンテキスト収集などバグ報告の初期トリアージを自動化したい開発チーム
- 注文管理やアップセル提案など、パーソナライズされたカスタマーサービスを提供したい小売事業者
