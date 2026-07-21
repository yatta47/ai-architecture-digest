---
type: guidance
title: 中堅・中小企業向けMicrosoft Fabric×Azure Databricksモダンデータ基盤
title_original: Build a modern data platform architecture for SMBs by using Microsoft Fabric and Azure Databricks
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: cost
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/small-medium-modern-data-platform
published_at: '2026-06-11'
---

## 概要

中堅・中小企業（SMB）が既存のAzure Databricks環境を活かしつつ、フルマネージドSaaSデータ基盤のMicrosoft Fabricを組み合わせてモダンデータ基盤を構築するアーキテクチャ。OneLakeでAzure Databricks Unity Catalogをミラーリングすることでデータを複製・移動せずに統合し、Delta Lake形式のBronze/Silver/Goldメダリオン構成で構造化・非構造化データを一元管理する。Power BIのDirect LakeモードやFabric Real-Time Intelligenceにより、バッチとストリーミングの両方のデータをコラボレーション・活用できる。
