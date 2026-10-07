---
type: guidance
title: エージェント自動化の事業価値を測る Agentic Value Model
title_original: 'Beyond hours saved: Building the business case for agentic automation'
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- human-in-the-loop
components: []
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/beyond-hours-saved-building-the-business-case-for-agentic-automation/
published_at: '2026-10-07'
---

## 概要

RPA時代の「削減時間×人件費−構築費」というROIモデルはエージェント自動化の価値を捉えきれないとして、時間削減・例外処理・意思決定品質・変化耐性と保守経済性の4軸で評価するAgentic Value Modelを提案する。価値が損益に反映される実現メカニズムと責任者を定義することを条件とする。

## 設計のポイント

- 価値プールごとにベースライン・期待改善幅・実現係数・責任者を定義し、二重計上を避ける
- 削減した時間は人員削減や残業削減、または名指しの成果への再配置が伴う場合のみ価値として計上する
- エージェント運用コスト（評価・プロンプト・監視）を保守回避分と相殺して純額で見る

## 使いどころ

- AI CoEがエージェント導入の投資判断資料を作る場面
- RPAからエージェントへ移行する案件の費用対効果を財務部門に説明する場面
