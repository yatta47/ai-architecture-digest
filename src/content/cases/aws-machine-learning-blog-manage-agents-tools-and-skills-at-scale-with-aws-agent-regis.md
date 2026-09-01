---
type: announcement
title: AWS Agent Registryでエージェント・ツール・スキルを全社横断で管理する
title_original: Manage agents, tools and skills at scale with AWS Agent Registry
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- policy-as-code
- human-in-the-loop
components:
- AWS Agent Registry
- Model Context Protocol (MCP)
- Agent2Agent (A2A)
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/manage-agents-tools-and-skills-at-scale-with-aws-agent-registry/
published_at: '2026-08-31'
---

## 概要

AWS Agent RegistryがGA提供開始となり、組織内に散在するエージェント・ツール・スキルを検索可能な単一カタログで管理できるようになったことを伝える記事。ガバナンス面を扱うGovernance Planeと、承認済みリソースのみを見せるDiscovery Planeの2層構成により、重複開発の防止と監査証跡の確保を両立する。Southwest AirlinesやPepsiCoなど、既にツールの重複開発削減に活用している事例が紹介されている。

## 設計のポイント

- Governance Plane（包括的な管理・承認ワークフロー）とDiscovery Plane（承認済みリソースのみを見せる高速検索）を分離する
- MCPサーバー・A2Aエージェント・スキル・カスタムディスクリプタの4種類のレコード型で統一的にカタログ化する
- セマンティック検索とロールベースの発見ポリシーにより、権限に応じて見えるリソースを制御する

## 使いどころ

- 数百〜数千のエージェント・ツールが複数チームに分散し、重複開発やガバナンス欠如に悩む大企業
- AIツールの所有者・レビュー状況・監査証跡を一元的に追跡したいプラットフォームチーム
