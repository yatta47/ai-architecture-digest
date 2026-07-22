---
type: guidance
title: Azure仮想デスクトップ基盤(VDI)のアーキテクチャ設計ガイド
title_original: Get started with virtual desktop architecture design
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/virtual-desktop/virtual-desktop-get-started
published_at: '2026-04-01'
---

## 概要

Azure上で仮想デスクトップを構築する際のアーキテクチャ全体像を示すハブ記事で、Azure Virtual Desktop・Windows 365・Omnissa Horizon Cloud・Citrix Virtual Apps and Desktopsといった複数の選択肢を整理している。基本構成としてはハブアンドスポーク型ネットワークとExpressRoute接続、Microsoft Entra IDやAD DSによるID管理、ホストプールとセッションホスト、Azure FilesやAzure NetApp Filesによるストレージ、Log Analyticsによる監視を組み合わせる。ランディングゾーン設計、マルチリージョンBCDR、セキュリティベースライン、VMサイジングなど、本番導入に向けた関連ガイドへの入り口としてまとめられている。
