---
type: guidance
title: 共有すべきブローカークラスを毎回生成してしまうImproper Instantiationアンチパターン
title_original: Improper Instantiation antipattern
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/antipatterns/improper-instantiation/
published_at: '2026-02-03'
---

## 概要

HttpClientやAzure Cosmos DBのDocumentClientなど、本来シングルトンとして共有すべきブローカークラスをリクエストのたびに生成・破棄してしまうことで、ソケット枯渇や生成コスト増大によりスケーラビリティが低下するアンチパターンを解説する。静的な共有インスタンスやプールへの切り替え、テレメトリによる検知方法を示す。
