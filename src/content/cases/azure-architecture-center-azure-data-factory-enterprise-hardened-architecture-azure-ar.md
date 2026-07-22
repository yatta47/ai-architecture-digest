---
type: guidance
title: 企業データプラットフォームとしてのAzure Data Factory堅牢化アーキテクチャ
title_original: Azure Data Factory enterprise hardened architecture
ai_relevant: false
industry: financial-services
cloud:
- azure
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/databases/architecture/azure-data-factory-enterprise-hardened
published_at: '2026-05-01'
---

## 概要

財務部門向けに構築したメダリオンレイクハウスのベースライン構成を、全社展開に耐えるよう堅牢化するアーキテクチャ。ドメイン単位でデータ所有権を持たせつつ、ID/ネットワーク/ガバナンスなど共通基盤を中央で提供するドメイン設計を採用し、Power BI・Azure Machine Learning・Azure Databricksをユーザー成熟度に応じて使い分けることで、99.9%稼働率やRPO1.5日などのエンタープライズSLAを満たす。
