---
type: announcement
title: コーディングエージェントを全社で一元管理するUnity Gateway CLI
title_original: Deploy and Manage Coding Agents at Scale with the Unity Gateway CLI
company: Databricks
industry: cross-industry
cloud: []
patterns:
- llm-gateway
- multi-model-routing
- cost-optimization
- policy-as-code
components:
- Unity Gateway
- Unity Gateway CLI
- Smart Routing
- Genie
- MCP
- Claude Code
- Codex
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/deploy-and-manage-coding-agents-scale-unity-gateway-cli
published_at: '2026-09-24'
---

## 概要

DatabricksはUnity Gateway CLI（ug）を発表した。管理者が承認済みモデル・MCPサーバー・スキル・予算ポリシーを一か所で公開し、開発者はug claudeやug codexで任意のコーディングエージェントを認証込みで起動できる。Smart Routingにより社内ベンチマークで35%のコスト削減、トレース分析でMCPツールの不具合7件を修正し年間約120万ドルの無駄を削減したとしている。

## 設計のポイント

- エージェント設定（既定モデル、MCP、スキル、予算）をゲートウェイで集中管理し、CLI起動時に自動同期することでモデル入替を全エージェントへ一括展開する。
- Smart Routingでタスクの難度に応じて安価なモデルと高性能モデルを使い分け、サブエージェントには別のモデル選択も行う。
- 予算しきい値に達したら低コストのエージェント/モデルを新規起動の既定に切り替え、進行中の作業は止めない。
- エージェントのトレース（ローカルのツール呼び出しやスキル実行）をレイクハウスに集約し、繰り返し失敗や過大な応答などの無駄なトークン消費を特定する。

## 使いどころ

- 複数のコーディングエージェントとモデルプロバイダを併用する大規模開発組織のプラットフォームチーム。
- モデルの入れ替わりが速く、コスト性能比の変化に追従したい企業。
- エージェント利用の予算管理と、アイデンティティ単位の利用帰属・監査が必要な組織。
