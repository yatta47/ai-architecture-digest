---
type: guidance
title: エッジからクラウドまで共通基盤で設計するソブリンAI
title_original: 'Designing for sovereign AI: A shared foundation from edge to cloud'
company: Microsoft
industry: cross-industry
cloud:
- azure
- on-prem
patterns:
- confidential-computing
- defense-in-depth
components:
- Azure
- Intel
outcome:
  type: risk-compliance
source_id: azure-blog
source_name: Azure Blog
source_url: https://azure.microsoft.com/en-us/blog/designing-for-sovereign-ai-a-shared-foundation-from-edge-to-cloud/
published_at: '2026-10-19'
---

## 概要

AI処理が機密データの発生源に近づくなか、デジタル主権はデータの保管場所だけでなく、実行場所、運用者、セキュリティ継続性まで含めてシリコンからAIまで一貫して設計する必要がある。MicrosoftとIntelは、ワークロードごとに配置を選べる柔軟なソブリン基盤を示す。

## 設計のポイント

- データ所在、実行場所、運用アクセス、継続性をスタック全体で設計する。
- ワークロードごとに配置先と制御水準を選べるようにする。
- エッジで機密データを現場処理し、必要な範囲だけをクラウドと連携する。

## 使いどころ

- 製造現場で機密の生産データを発生源の近くで分析する場面。
- 政府や製薬で、管理された環境内でAIを実行する場面。
