---
type: guidance
title: 分散アプリにおけるプライベート/共有キャッシュ設計指針
title_original: Caching guidance - Azure Architecture Center
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/best-practices/caching
published_at: '2026-06-12'
---

## 概要

分散アプリケーションにおけるキャッシュ戦略を、プロセス内で保持するプライベートキャッシュと、複数インスタンスが共有するシェアドキャッシュに分けて解説する一般設計ガイド。シェアドキャッシュはインスタンス間でのデータ一貫性とスケーラビリティを提供する一方、アクセス速度低下や別サービス運用の複雑さとのトレードオフがあることを整理する。
