---
type: opinion
title: 金融サービスにおける自律型AIエージェント活用事例集
title_original: Building AI agents for financial services
industry: financial-services
cloud:
- aws
patterns:
- ai-agent
- human-in-the-loop
components:
- Claude
- Amazon Bedrock
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/building-ai-agents-in-financial-services
published_at: '2025-10-30'
---

## 概要

NBIM、Brex、Intuit TurboTaxなど金融機関がClaudeを使い、不正検知・顧客対応・レポーティングなどの業務に自律型AIエージェントを導入した事例を紹介。規制対応やリスク管理を踏まえたエージェント設計の勘所を解説する。

## 設計のポイント

- エージェントに調整・分析を任せつつ最終判断はアナリストに残す人間参加型ワークフローにする
- 複数システムに分散したデータを横断してエージェントに監視・分析させる
- 規制要件やコンプライアンスを踏まえた監査可能なエージェント設計にする

## 使いどころ

- 不正検知やAML監視を人手だけでスケールさせたい金融機関
- 顧客対応の自動化と品質維持を両立したいカスタマーサポート部門
- レガシー基幹系システムとAIエージェントを統合したい金融IT部門
