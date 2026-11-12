---
type: guidance
title: カスタマー管理KBからBedrock Managed Knowledge Baseへ、コーディングエージェントで移行する手引き
title_original: Migrate to Amazon Bedrock Managed Knowledge Base with your coding agent
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- rag
- ai-agent
components:
- Amazon Bedrock Knowledge Bases
- Agent Toolkit for AWS
- Amazon S3 Vectors
- AgentCore Gateway
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/migrate-to-amazon-bedrock-managed-knowledge-base-with-your-coding-agent/
published_at: '2026-11-12'
---

## 概要

カスタマー管理のBedrock Knowledge BaseをManaged Knowledge Baseへ移行するため、Agent Toolkit for AWSのamazon-bedrockスキルに移行ガイドが追加された。エージェントが読み取り専用の調査と計画提示を行い、承認後に新KB作成またはIaC生成を行う。

## 設計のポイント

- 読み取り専用のディスカバリと行単位でレビューする計画を先に作り、承認後にのみリソースを作成する。
- 新KBを既存KBと並行して作成し、検索品質を検証してからトラフィックを切り替える。
- 取り込みとアプリ側のRetrieve呼び出し変更は利用者側に残し、エージェントは手順の案内に徹する。

## 使いどころ

- ベクトルストアの運用や容量計画を手放したいRAG運用チーム。
- 低利用率で従量課金のメリットが大きい社内QA/ポリシー検索基盤。
- 複数チームでKBを分割・共有したい組織。
