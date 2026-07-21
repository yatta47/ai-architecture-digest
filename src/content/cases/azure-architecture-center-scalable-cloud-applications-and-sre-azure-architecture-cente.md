---
type: guidance
title: SRE原則で構築するスケーラブルなAzure APIプラットフォーム
title_original: Scalable cloud applications and site reliability engineering (SRE)
ai_relevant: false
industry: retail
cloud:
- azure
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/apps/scalable-apps-performance-modeling-site-reliability
published_at: '2026-06-25'
---

## 概要

Azure Architecture Centerが示す参考アーキテクチャで、Azure Front Door・API Management・Application Gateway for Containers・AKSを組み合わせたスケーラブルなAPIプラットフォームにサイトリライアビリティエンジニアリング（SRE）の原則を適用する方法を解説する。Front Doorからバックエンドのマイクロサービスに至る各レイヤーで個別にテレメトリを収集し、サービスレベル指標（SLI）とサービスレベル目標（SLO）を定義・計測することで、信頼性を測定可能かつ達成可能な形にしている。
