---
type: case
title: llama-agentsで組んだビジュアルドキュメント処理ワークフローParse-Flow
title_original: Designing a Visual Document Intelligence Workflow with LlamaParse
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- ai-agent
- event-driven
- document-processing
components:
- LlamaParse Platform
- Redis
- PostgreSQL
- llama-agents
outcome:
  type: reliability
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/designing-a-visual-document-intelligence-workflow-with-llamaparse
published_at: '2026-07-18'
---

## 概要

Parse-FlowはParse・Extract・Classify・Splitの4つのドキュメント処理プリミティブをビジュアルワークフローとして組み立てられるOSSで、Reactのキャンバス・BunサーバーとPythonワーカー・Redis/Postgresで構成される。バックエンドは単一のllama-agents Workflowが「許可される遷移グラフ」を実行時に解釈し、任意の長さのフローを1つの状態機械で処理する。

## 設計のポイント

- イベントをRedisのライブストリームとPostgresの永続ストアの二重に記録し、リロード後も実行履歴を再現できるようにする
- 遅くなりうるワーカー処理をHTTP層から切り離し、非同期ジョブキュー(Redis)経由で疎結合にする
- parse→extractのように前段の結果（parse_job_id）を後段が再利用し、無駄な再パースを避けてレイテンシとコストを削減する
- フロントエンドとバックエンドの双方で「許可される遷移グラフ」を検証し、不正な組み合わせのワークフロー投入を防ぐ

## 使いどころ

- 分類→ルーティング→抽出のような複数段階のドキュメント処理を可視化して構築したい開発者
- イベント駆動ワークフローエンジンの設計パターンを探しているエージェント基盤開発チーム
