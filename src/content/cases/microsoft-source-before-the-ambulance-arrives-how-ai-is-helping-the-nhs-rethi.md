---
type: case
title: NHS(救急サービス)での管理業務向けMicrosoft Copilot展開
title_original: 'Before the ambulance arrives: How AI is helping the NHS rethink patient care'
company: Microsoft / NHS England
industry: healthcare
cloud:
- azure
patterns:
- human-in-the-loop
- guardrails
components:
- Microsoft Copilot
outcome:
  type: productivity
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://news.microsoft.com/source/emea/features/before-the-ambulance-arrives-how-ai-is-helping-the-nhs-rethink-patient-care/
published_at: '2026-10-21'
---

## 概要

NHS Englandは3万人の試行を経て、最大50.5万人の職員にMicrosoft Copilotを展開する計画を発表した。用途は臨床ではなく管理業務に限定され、試行では1人1日平均43分の削減が報告された。

## 設計のポイント

- 利用範囲を管理業務に限定し、臨床判断にはAIを使わない線引きをしている。
- Copilotは判断せず情報を整理し、人が専門知識で確認する運用にしている。
- 臨床安全・情報ガバナンス・サイバーセキュリティ等の基準と人による監督を前提にしている。

## 使いどころ

- 大規模な公的機関が生成AIを段階的に導入する場面。
- 報告書作成やメール下書きなど事務負担の大きい職種の支援。
- ディスレクシアなど読み書き支援が必要な職員のアクセシビリティ向上。
