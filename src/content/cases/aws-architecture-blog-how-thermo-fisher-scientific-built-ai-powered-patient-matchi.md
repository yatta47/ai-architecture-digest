---
type: case
title: 'Thermo Fisherの治験患者マッチング: データ基盤とNLで使えるPatient Match AI'
title_original: How Thermo Fisher Scientific built AI-powered patient matching on AWS
company: Thermo Fisher Scientific
industry: healthcare
cloud:
- aws
patterns:
- text-to-sql
- business-intelligence-resilience
components:
- AWS
- AWS Countdown Premium
- Patient Match AI
- Central Insights Hub
outcome:
  type: speed
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/how-thermo-fisher-scientific-built-ai-powered-patient-matching-on-aws/
published_at: '2026-11-13'
---

## 概要

Thermo Fisher Scientificは、治験の患者募集に関わる分散データをAWS上の基盤に集約し、分析用のCentral Insights Hubと、自然言語でコホート探索を行うPatient Match AIを構築した。従来数日〜数週間かかった探索が数分になった。

## 設計のポイント

- AIの前にデータ基盤を整備し、分析とAI機能を同じ基盤の上に載せる。
- 自然言語で条件を絞り込む対話型のコホート探索を提供する。
- AWS Countdown Premiumで本番移行時の運用準備とリスクを抑える。

## 使いどころ

- 複雑な適格基準を持つ治験の募集部門。
- 複数システムに散在するデータを自己サービスで探索したい業務部門。
