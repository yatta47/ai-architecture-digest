---
type: case
title: AgentCoreで金融データ処理を刷新したDucoのエージェント基盤
title_original: How Duco transforms financial data automation with Amazon Bedrock AgentCore
company: Duco
industry: financial-services
cloud:
- aws
patterns:
- ai-agent
- multi-tenant-rag
- guardrails
components:
- Amazon Bedrock
- Amazon Bedrock AgentCore
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-duco-transforms-financial-data-automation-with-amazon-bedrock-agentcore/
published_at: '2026-11-16'
---

## 概要

Ducoは従来の機械学習中心の構成から、BedrockとAgentCoreを使うエージェント型の基盤へ移行した。銀行ごとにデータを分離したまま、デプロイ時間とオンボーディングコストを削減した。

## 設計のポイント

- 柔軟性に欠ける従来型MLを、基盤モデルとエージェントで置き換えた。
- 顧客（銀行）ごとのデータ分離を前提に、実行基盤をマネージド化した。
- 規制環境で求められるコンプライアンスを基盤側で担保する。

## 使いどころ

- 顧客ごとの隔離が必須な金融SaaS。
- 個別カスタマイズが多い業務自動化プラットフォーム。
