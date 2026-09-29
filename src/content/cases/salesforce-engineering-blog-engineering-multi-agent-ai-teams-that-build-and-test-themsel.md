---
type: case
title: エージェントチームを設計・検証・修復するSalesforceのAgent Designer
title_original: Engineering multi-agent AI teams that build and test themselves
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- ai-agent
- human-in-the-loop
- eval
components:
- Agent Designer
- Claude Unleashed
- Marketing Cloud
outcome:
  type: speed
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/engineering-multi-agent-ai-teams-that-build-and-test-themselves/
published_at: '2026-09-28'
---

## 概要

SalesforceのMarketing Cloudチームは、依頼から検証済みのマルチエージェントチームを15〜30分で作るAgent Designerを開発した。従来は2〜4時間かかっていた。オーケストレーターと7専門エージェントが設計・検証・テスト・限定的な修復を担うが、オーケストレーター自身はエージェントのファイルを書けない。

## 設計のポイント

- 設計案は人が承認するまで止め、承認後に別のエージェントが書き込み・検証・テスト・修復を行う。
- 書き込み範囲をプロンプトで決定的に区切り、複数エージェントの成果物の衝突や権限の逸脱を防ぐ。
- アーキテクチャ・失敗モード・コンプライアンスの各分析を統合して整合の取れた設計にする。
- 修復は回数を限定し、誤った問題を延々と直さないようにする。

## 使いどころ

- エージェントチームの構築を自動化したいプラットフォーム開発者。
- マルチエージェントのガバナンスと権限分離を設計する担当者。
- エンジニアのレビュー中心の運用（manager-of-agents）を進める組織。
