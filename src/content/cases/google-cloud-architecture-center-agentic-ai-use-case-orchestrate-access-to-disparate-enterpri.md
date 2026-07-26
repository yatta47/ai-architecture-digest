---
type: guidance
title: オーケストレーターエージェントで社内外システムへのアクセスを統合するアーキテクチャ
title_original: 'Agentic AI use case: Orchestrate access to disparate enterprise systems'
industry: cross-industry
cloud:
- gcp
patterns:
- ai-agent
- event-driven
- llm-gateway
components:
- Agent Development Kit (ADK)
- Cloud Run
- Gemini Enterprise
- Pub/Sub
- Cloud SQL
- MCP Toolbox for Databases
- Gemini Enterprise Agent Platform Sessions
- Cloud Storage
outcome:
  type: productivity
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/agenticai-orchestrate-access-disparate-systems
published_at: '2026-07-19'
---

## 概要

Google Cloudは、複数の社内外システムを個別統合せず、オーケストレーターエージェントとMCPサーバー群による腐敗防止層を介して統一的な会話インターフェースからアクセスできるようにするアーキテクチャを示す。Webアプリ・Gemini Enterpriseのチャット・Pub/Subによるシステム間イベントという複数チャネルからの入力を単一のエージェントコアで処理する。

## 設計のポイント

- バックエンドシステムごとにMCPサーバーを立て、各システムのAPIを標準化されたツール群として公開する腐敗防止層とすることで、エージェント本体をバックエンドの変更から疎結合に保つ
- Webアプリ・Gemini Enterpriseチャット・Pub/Subイベントという複数チャネルからの入力を単一のオーケストレーターエージェントに集約し、多段タスクの状態はSessionsやCloud Storageに永続化する
- Cloud Run上でIAMベースのアクセス制御を行い、最小権限のサービスアカウントとingress制御でエージェントAPIを保護する
- コールドスタートを避けるため最小インスタンス数を設定するなど、レイテンシに敏感な用途向けにCloud Runのスケーリングを調整する

## 使いどころ

- 複数のレガシーシステムを大規模移行なしに統一インターフェースで扱いたい業務部門
- オペレーターの『スイベルチェア作業』（システム間の頻繁な切り替え）を削減したいコールセンターやバックオフィス
