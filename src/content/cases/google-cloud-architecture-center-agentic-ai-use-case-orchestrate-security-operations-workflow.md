---
type: guidance
title: SOCの調査・トリアージを自動化するマルチエージェント・セキュリティオペレーション
title_original: 'Agentic AI use case: Orchestrate security operations workflows'
industry: cross-industry
cloud:
- gcp
patterns:
- multi-agent-orchestration
- root-cause-analysis
- human-in-the-loop
- defense-in-depth
components:
- Cloud Run
- Cloud Load Balancing
- Google Cloud Armor
- Identity-Aware Proxy (IAP)
- Model Armor
- Agent Development Kit (ADK)
- Gemini Enterprise Agent Platform
- Google Security Operations
- Google Threat Intelligence
- Model Context Protocol (MCP)
- Gemini Enterprise
- Gemini
outcome:
  type: risk-compliance
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/agentic-ai-orchestrate-security-ops-workflows
published_at: '2026-07-19'
---

## 概要

Google Cloudは、SIEM・脅威インテリジェンス・CSPM・EDRなど分散したセキュリティツール群を、マルチエージェントAIシステムで横断的にオーケストレーションしSOCの調査・トリアージを効率化するアーキテクチャを示す。Google SecOps MCPサーバーや脅威インテリジェンスMCPサーバー、サードパーティMCPコネクタで既存ツールをエージェントから利用可能にする。

## 設計のポイント

- Google SecOps・Google Threat Intelligence・サードパーティCSPM/EDRツールをそれぞれ専用のMCPサーバー経由でエージェントに接続し、単一インターフェースからの複数段階の調査を可能にする
- Cloud Armor・IAP・Model Armorによる多層防御を、Cloud Run上のエージェントAPI自体にも適用しゼロトラストを徹底する
- 重要な対応アクションにはヒューマン・イン・ザ・ループの承認を組み込み、SOCアナリストのコンテキストスイッチングを減らしつつ最終判断は人に残す
- Cloud RunとAgent Runtime on Gemini Enterprise Agent Platformの2つのデプロイモデルを提示し、運用負荷とカスタマイズ性のトレードオフに応じて選べるようにする

## 使いどころ

- 重大アラートのエンリッチメントから資産の設定不備確認、エンドポイント調査までを単一インターフェースで行いたいSOCアナリスト
- 既存のSIEM・EDR・CSPMツールを個別に開発せずAIエージェントから横断利用したいセキュリティ運用チーム
