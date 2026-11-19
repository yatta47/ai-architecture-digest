---
type: case
title: 実顧客データが無い状態でのITSM予測モデルを合成データで作る
title_original: Building predictive AI models when synthetic data is all you have
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- eval
components:
- Salesforce Data 360
- Predictive Model Templates
outcome:
  type: risk-compliance
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/building-predictive-ai-models-when-synthetic-data-is-all-you-have/
published_at: '2026-11-19'
---

## 概要

SalesforceのITSMチームは、SLA違反予測、重大インシデント予測、変更リスクスコアの3テンプレートを、現実的な合成データで学習して作った。精度だけに頼らない検証を行い、Data 360の取り込みから学習・スコアリングまでを顧客別パイプラインとして再利用できるようにした。

## 設計のポイント

- 顧客データを横断学習できない制約のもと、合成シナリオで初期モデルを作る。
- 精度だけで判断せず、実環境で通用するかを別の観点で検証する。
- 取り込み・変換・学習・スコアリングを顧客別の再利用可能なパイプラインにする。

## 使いどころ

- 実データが少ない状態で予測機能を出したいSaaS事業者。
- 顧客ごとにモデルを分離したい組織。
