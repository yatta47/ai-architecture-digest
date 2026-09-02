---
type: guidance
title: 本番AIエージェント運用を体系化するAgentOpsの実践ガイド
title_original: Announcing the Databricks Big Book of AgentOps
industry: cross-industry
cloud:
- multi-cloud
patterns:
- llmops
- ai-agent
- eval
- guardrails
components:
- Unity Catalog
- Unity Gateway
- MLflow
outcome:
  type: reliability
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/announcing-databricks-big-book-agentops
published_at: '2026-09-02'
---

## 概要

「The Big Book of AgentOps」は、ツール呼び出しやマルチステップ実行を行うAIエージェントを本番で信頼性高く運用するための実践ガイド。アーキテクチャ設計、デプロイパターン、評価・フィードバックループ、コスト管理、ステークホルダー調整までを6章にわたり体系化し、Unity Catalog・Unity Gateway・MLflowを中核とした運用の型を提示する。

## 設計のポイント

- 4つのエージェントアーキテクチャと4つのデプロイメントパターンを整理し、要件の複雑さに応じてどう選定・進化させるかの指針を示す
- チーム編成からユースケース選定、データ基盤整備、評価ループ、ガバナンスまでを7フェーズのプロジェクトライフサイクルとして定義する
- 本番トレースからゴールデン評価データセットを構築し、自動判定器(LLMジャッジ)をSMEのフィードバックで較正するDevOps的な継続改善ループを適用する
- サブエージェント呼び出しやリトライ、ガードレールチェックを含めたコストを可視化し、利用量の帰属と上限設定・アカウンタビリティを運用に組み込む

## 使いどころ

- パイロット段階から本番移行できずに停滞しているAIエージェント導入チーム
- ツールの過剰な権限やコスト急増などのリスクを事前に統制したいエンジニアリング・セキュリティ・コンプライアンス部門
- エグゼクティブスポンサーからSME・財務まで多くの関係者の合意形成が必要な大規模エージェントプロジェクト
- 顧客データへのきめ細かなアクセス制御が求められるカスタマーサポート等の業務エージェントを構築するチーム
