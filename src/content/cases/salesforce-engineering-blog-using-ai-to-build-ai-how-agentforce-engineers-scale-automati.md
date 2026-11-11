---
type: case
title: Atlas Reasoning Engineの開発・保守をAIで自動化し信頼性を保つ仕組み
title_original: 'Using AI to Build AI: How Agentforce Engineers Scale Automation Without Sacrificing Reliability'
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- ai-agent
- rag
- eval
- human-in-the-loop
- memory-consolidation
components:
- Agentforce
- Atlas Reasoning Engine
outcome:
  type: speed
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/using-ai-to-build-ai-how-agentforce-engineers-scale-automation-without-sacrificing-reliability/
published_at: '2026-11-09'
---

## 概要

SalesforceのAgentforce開発チームが、推論エンジンAtlasの診断・修正・テスト・レビューをAIで自動化しつつ信頼性を保った取り組み。インシデントや修正履歴を束ねた意味検索ベースの知識基盤と、軌跡全体を評価するagent-as-a-judgeに人手の確認を組み合わせ、バグ解決を2〜4週間から1〜2日に短縮した。

## 設計のポイント

- インシデント、過去の修正、コード、Slack議論を意味検索で結び付け、古い情報を剪定してコンテキスト肥大を防ぎ、修正の度に記憶を更新している。
- 非決定的なエンジンに対し、最終回答だけでなく中間の推論やツール呼び出しを含む軌跡全体を評価している。
- シナリオテスト、リプレイ、ミューテーションテストを再利用可能な回帰データセットで回し、ローカルとデプロイ先の両方で検証している。
- AI同士の自己選好バイアスを前提に、検証や取り消しが難しい箇所に人間の確認を残している。

## 使いどころ

- AIで自社AIシステムの開発・保守を自動化したいが、品質低下を避けたいチーム。
- 障害対応の知見が分散し、同種の調査が繰り返されている大規模エンジニアリング組織。
- 正解データが無い領域でAI生成物の評価体制を設計する場面。
