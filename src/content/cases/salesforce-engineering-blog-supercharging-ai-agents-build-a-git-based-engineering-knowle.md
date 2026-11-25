---
type: case
title: 設計判断をエージェントに正しく渡すGitベースの知識グラフ『Second Brain』
title_original: 'Supercharging AI Agents: Build a Git-based Engineering Knowledge Framework in 20 Minutes'
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- context-engineering
- ai-agent
- human-in-the-loop
components:
- Git
- knowledge graph
- Second Brain
- Kubernetes
outcome:
  type: productivity
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/supercharging-ai-agents-build-a-git-based-engineering-knowledge-framework-in-20-minutes/
published_at: '2026-11-24'
---

## 概要

Salesforceは分散した設計判断と根拠を、Gitと知識グラフで管理する仕組みを構築し、人とエージェントが参照できるようにした。Kubernetesアップグレードエージェントは約80%を自動化し、手作業を3か月から3週間に短縮した。

## 設計のポイント

- 巨大な単一リポジトリは検索が遅くトークンも浪費するため、ドメイン別に分割して知識グラフで接続する。
- 判断には根拠ソースを紐づけ、矛盾や未検証事項は黙って解決せず人のレビューに回す。
- 全知識の一括取り込みを避け、1ドメインから始めて必要に応じ広げる。

## 使いどころ

- エージェントが古い設計や却下案を参照する問題を抱える開発組織。
- 属人化した運用知識を継承したいインフラチーム。
