---
type: guidance
title: Google Cloud上でマルチエージェントAIシステムを構築するリファレンスアーキテクチャ
title_original: Multi-agent AI system in Google Cloud
industry: cross-industry
cloud:
- gcp
patterns:
- multi-agent-orchestration
- human-in-the-loop
components:
- Cloud Run
- Gemini Enterprise Agent Platform
- Google Kubernetes Engine (GKE)
- Model Armor
- Agent Development Kit (ADK)
- Agent2Agent (A2A) protocol
- Model Context Protocol (MCP)
outcome:
  type: quality
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/multiagent-ai-system
published_at: '2026-07-19'
---

## 概要

Google Cloudは、コーディネーターエージェントが複数のサブエージェントへタスクを振り分けるマルチエージェントAIシステムのリファレンスアーキテクチャを示す。逐次実行パターンと反復改善パターンを例に、A2AプロトコルやMCP、Model Armorを組み合わせた構成と、株式トレード推奨・リサーチアシスタントといったユースケースを解説する。

## 設計のポイント

- コーディネーターエージェントがユーザー意図に応じて逐次実行パターンや反復改善パターンなど適切なエージェントフローを選択する
- 反復改善パターンでは品質評価エージェントが出力を評価し、不十分な場合はプロンプト改善エージェントを介して再実行するループを、最大反復回数を設けて構成する
- エージェント間通信はA2Aプロトコルで言語・ランタイムに依存せず相互運用可能にし、ツールへのアクセスはMCPで標準化する
- Model Armorでプロンプトインジェクションや機微情報漏えいからエージェント基盤を保護し、重要な判断にはヒューマン・イン・ザ・ループの経路を用意する

## 使いどころ

- リスクプロファイルに応じた株式売買推奨と自動発注を行いたい金融サービス
- 調査計画の立案から情報収集・レポート作成までを自動化したいリサーチアシスタント用途
