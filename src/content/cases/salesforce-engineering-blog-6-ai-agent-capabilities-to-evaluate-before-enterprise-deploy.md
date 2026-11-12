---
type: guidance
title: EGI-Bench：企業エージェントの6つの能力軸で本番適性を評価する統合ベンチマーク
title_original: 6 AI agent capabilities to evaluate before enterprise deployment
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- eval
components:
- EGI-Bench
outcome:
  type: quality
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/6-ai-agent-capabilities-to-evaluate-before-enterprise-deployment/
published_at: '2026-11-12'
---

## 概要

Salesforce AI Researchは、独立に作られた8つの企業向けベンチマークを統合し、6つのスキル軸・20超のサブドメイン・1,500タスクにマップするEGI-Benchを構築した。単一スコアでは見えない弱点を本番前に明らかにする狙い。

## 設計のポイント

- 異なる指標を共通のスキル次元に写像して統合スコアを作る。
- 正答だけでなくツール選択、計画、文脈利用、安全性、エンジニアリング作業まで測る。
- 本番で初めて発覚する弱点を評価段階で露出させる。

## 使いどころ

- エージェントの導入可否を判断する企業。
- モデルやエージェント間を比較評価したい研究・選定担当。
- 独自ベンチマークを設計する評価チーム。
