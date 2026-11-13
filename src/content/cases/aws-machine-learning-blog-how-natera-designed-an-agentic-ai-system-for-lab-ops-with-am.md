---
type: case
title: Nateraのラボ機器サポート向けエージェントSWARM
title_original: How Natera designed an agentic AI system for lab ops with Amazon Bedrock AgentCore
company: Natera
industry: healthcare
cloud:
- aws
patterns:
- ai-agent
- rag
- eval
components:
- Amazon Bedrock AgentCore
- Jira
- Confluence
- AWS IAM
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-natera-designed-an-agentic-ai-system-for-lab-ops-with-amazon-bedrock-agentcore/
published_at: '2026-11-12'
---

## 概要

Nateraは、ラボ機器の障害対応ノウハウを継承するため、Amazon Bedrock AgentCore上にエージェントSWARMを構築した。Jiraチケットに自動で一次回答し、初回応答時間は約130倍高速化、自動カバー率は96.2%となった。

## 設計のポイント

- ベンダー文書や過去の解決事例から知識ベースを構築し、機器ファミリごとの診断に使う。
- JiraやConfluenceと統合し、チケット到着時点で自律処理する。
- 評価ループを組み込み、継続的に精度を改善する。

## 使いどころ

- 属人的な保守ノウハウが散在する運用チーム。
- 高ボリュームのチケットに即応したいサポート部門。
