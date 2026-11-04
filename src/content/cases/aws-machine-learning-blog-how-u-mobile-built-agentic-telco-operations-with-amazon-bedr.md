---
type: case
title: 通信事業者のエージェント型ヘルプデスクAiDaH
title_original: How U Mobile built agentic telco operations with Amazon Bedrock AgentCore
company: U Mobile
industry: telecom
cloud:
- aws
- on-prem
patterns:
- ai-agent
- multi-agent-orchestration
- spec-driven-development
components:
- Amazon Bedrock AgentCore
- Amazon Bedrock
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-u-mobile-built-agentic-telco-operations-with-amazon-bedrock-agentcore/
published_at: '2026-11-04'
---

## 概要

マレーシアのU Mobileは、ログ、BSS API、ナレッジベースを横断して原因診断と対処案提示を行うAiDaHを、Bedrock AgentCore上の6層構成で構築した。1年で150超の運用シナリオを6部門でカバーし、主要カテゴリで障害チケットが最大84.5%減ったとする。

## 設計のポイント

- マネージドなエージェントランタイムとメモリでインフラ運用を持たない。
- ログ参照・資格確認・方針参照など複数システムの調査を1エージェントで連携させる。
- 仕様駆動の手法で開発を進めた。

## 使いどころ

- 複数システムをまたぐ問い合わせ対応でエスカレーションを減らしたいとき。
- オンプレとクラウドが混在する通信・IT運用。
