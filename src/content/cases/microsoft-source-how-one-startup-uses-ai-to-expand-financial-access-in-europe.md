---
type: case
title: Welcountが移住者向け金融サービスをAIで拡張
title_original: How one startup uses AI to expand financial access in Europe
company: Welcount
industry: financial-services
cloud:
- azure
patterns:
- document-processing
- guardrails
- ai-agent
components:
- Microsoft Azure
outcome:
  type: speed
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://www.microsoft.com/en-us/startups/blog/building-fintech-for-greater-financial-success-how-welcount-uses-ai-to-serve-more-customers/
published_at: '2026-09-10'
---

## 概要

フランスの移民・難民向けフィンテックWelcountは、Microsoft Azureを基盤にコンプライアンス業務・本人確認・カスタマーサポートにAIを組み込み、口座開設に必要な本人確認を24時間以内で完了できる仕組みを構築した。Microsoft for StartupsやGenAI Studioの支援を受けて拡張した。

## 設計のポイント

- 本人確認・コンプライアンス・スケーラビリティを同一プラットフォーム上で満たすためAzureを基盤に選定する
- 決済（Visa）やBaaS（Okali）など外部パートナーとAI活用範囲を分離し、規制当局（ACPR）との連携を前提に設計する
- 生成AIをカスタマーサポートや内部業務、コンプライアンスワークフローの複数箇所に段階的に組み込む

## 使いどころ

- 従来の金融システムが想定していない、移住者・難民・留学生など新規顧客層向けのオンボーディング高速化
- 本人確認や規制対応を伴うフィンテック立ち上げ期のスタートアップ
