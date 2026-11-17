---
type: case
title: MCPベースのAIでテスト失敗600件超のトリアージを短縮した事例
title_original: How AI slashed 600 test failure triage from days to 90 minutes
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- ai-agent
- root-cause-analysis
- ci-cd
components:
- Model Context Protocol
outcome:
  type: speed
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/how-ai-slashed-600-test-failure-triage-from-days-to-90-minutes/
published_at: '2026-11-17'
---

## 概要

SalesforceはSOAPログイン廃止で意図的に生じる600件超のテスト失敗から、本物のリグレッションを見分けるMCPベースのAIツールを構築した。失敗の分類と担当チームへの振り分けにより、2〜3日の作業を約90分に短縮した。

## 設計のポイント

- 想定内の失敗と実不具合を、スタックトレースの文脈から分類する。
- 共通原因ごとに失敗をまとめ、担当チームへ振り分ける。
- 50件の再割り当て上限を、重複や誤配を避けて処理する。

## 使いどころ

- 大規模な仕様変更で大量のテスト失敗が出るプラットフォーム開発。
- 複数チームにまたがる失敗の振り分け。
