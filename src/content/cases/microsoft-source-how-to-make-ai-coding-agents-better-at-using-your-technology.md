---
type: guidance
title: AIコーディングエージェントに自社技術を正しく使わせる評価手法AX Playbook
title_original: How to make AI coding agents better at using your technology (AX Practitioner Playbook)
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- eval
- context-engineering
components:
- Azure Cosmos DB Agent Kit
- SharePoint Framework
- MCP
outcome:
  type: quality
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://developer.microsoft.com/blog/introducing-the-agent-experience-ax-practitioner-playbook/
published_at: '2026-10-09'
---

## 概要

MicrosoftのDevRelが数百回のエージェントセッションから得た、コーディングエージェントによる自社技術の扱いを評価・診断・改善する手法をまとめたAX Practitioner Playbookの紹介。docs、MCP、skill、指示ファイルなどエージェントが参照する情報源を直すことに焦点を当てる。

## 設計のポイント

- モデルの改善を待たず、エージェントが参照するdocs・MCP・skillなどの情報源を改善対象にする。
- 結果だけでなくトレジェクトリを見て、拡張が未ロード・未呼び出し・誤適用のどれかを切り分ける。
- コンパイル可否などのゲートと、意味を判定する基準を組み合わせて評価の信頼性を担保する。
- 改善案は仮説として検証してから、所有チームに根拠付きで提案する。

## 使いどころ

- SDK/API/MCPサーバーなどを提供し、エージェントからの利用品質を上げたい開発元。
- エージェント向けドキュメントやskillを整備するDevRel担当者。
