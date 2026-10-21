---
type: case
title: Amazon QuickとBedrock AgentCoreによる会話型サプライチェーン分析
title_original: 'From data to decisions: Conversational supply chain intelligence with Amazon Quick and Amazon Bedrock AgentCore'
company: AWS
industry: logistics
cloud:
- aws
patterns:
- ai-agent
- multi-agent-orchestration
- human-in-the-loop
- context-engineering
components:
- Amazon Quick
- Amazon Bedrock AgentCore
- MCP
- AWS Agent Registry
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/from-data-to-decisions-conversational-supply-chain-intelligence-with-amazon-quick-and-amazon-bedrock-agentcore/
published_at: '2026-10-20'
---

## 概要

複数システムにまたがる在庫・障害・調達情報を、AgentCoreが公開するMCPサーバー群とAmazon Quickで会話的に横断照会する。5システム45〜60分の作業が3プロンプトに短縮され、変更は人の承認を待つ。

## 設計のポイント

- 企業MCPサーバーを組み合わせ可能なツール層としAgent Registryで発見する。
- 回答はモデルの記憶でなく実システムの最新データから作る。
- 変更系の操作は必ず指名された人間の承認を挟む。

## 使いどころ

- 港湾閉鎖など混乱時の影響SKU特定と緊急RFQ発行。
- ERP・調達・メールを行き来する担当者の負荷軽減。
