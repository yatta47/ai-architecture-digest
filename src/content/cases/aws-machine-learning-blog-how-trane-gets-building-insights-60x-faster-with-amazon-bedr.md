---
type: case
title: HVAC運用データへの問い合わせをロール別マルチエージェントで60倍高速化
title_original: How Trane gets building insights 60x faster with Amazon Bedrock AgentCore
company: Trane Technologies
industry: manufacturing
cloud:
- aws
patterns:
- multi-agent-orchestration
- ai-agent
- root-cause-analysis
components:
- Amazon Bedrock AgentCore
- Strands Agents
- AWS CDK
- Amazon Bedrock AgentCore Gateway
- Trane Cloud
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-trane-gets-building-insights-60x-faster-with-amazon-bedrock-agentcore/
published_at: '2026-09-22'
---

## 概要

数百万台の接続HVAC機器を運用するTrane Technologiesは、複数ダッシュボードを20分以上かけて横断する必要があった診断作業を、Amazon Bedrock AgentCoreとStrandsによる会話型エージェントで20秒に短縮した。技術者・アカウントマネージャー・オーナーといった異なるロールのニーズに応じ、単一の対話インターフェースから回答を出す。

## 設計のポイント

- エージェントロジックをStrandsに、実行基盤・メモリ・ツールゲートウェイをAgentCoreに分離しレイヤーごとに責務を明確化した
- Resources/Knowledge/Analytics Insights/Expert Advisor/Navigationの5つの専門アシスタントに分割しモノリシックな単一プロンプトを避けた
- ロールベースアクセス制御でユーザーの権限とニーズに応じて回答内容を調整した
- AgentCore GatewayとMCPで追加のエージェントやツール（作業指示システムやCRM）を疎結合に拡張できる構成にした

## 使いどころ

- 現場技術者からエグゼクティブまで異なる粒度の質問に同じデータ基盤で答えたい設備管理
- 複数ダッシュボードを横断する調査作業を自然言語インターフェースに置き換えたいIoT運用
- 機能追加のたびにモノリシックなエージェントをデプロイし直したくない場合
