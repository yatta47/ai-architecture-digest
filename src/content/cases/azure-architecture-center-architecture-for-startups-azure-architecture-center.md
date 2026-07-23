---
type: guidance
title: スタートアップの成長段階に応じたアーキテクチャ選定ガイド
title_original: Architecture for startups
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: speed
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/startups/startup-architecture
published_at: '2026-02-09'
---

## 概要

スタートアップの成長を探索(Explore)・拡大(Expand)・抽出(Extract)という3段階のS字カーブとして捉え、各フェーズで技術選定の優先順位が変わることを解説するガイド。探索期はマネージドサービスやPaaS（Azure App Serviceなど）を使い速度・コスト・柔軟性を重視し、拡大期にはRAGによるAI追加やゾーン冗長化などの拡張を必要な分だけ段階的に行うべきだとしている。
