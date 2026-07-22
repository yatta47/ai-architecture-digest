---
type: guidance
title: Azure Virtual DesktopのマルチリージョンBCDR実装ガイド
title_original: Multiregion BCDR for Azure Virtual Desktop
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/azure-virtual-desktop/azure-virtual-desktop-multi-region-bcdr
published_at: '2026-03-25'
---

## 概要

Azure Virtual Desktopをリージョン障害から保護するための実装レベルのBCDR構成ガイド。FSLogixのクラウドキャッシュによるユーザープロファイルのリージョン間レプリケーションを軸に、アクティブ-アクティブ、アクティブ-パッシブ、Azure Site Recoveryを使う個人ホストプールという3つのBCDRモデルのRPO/RTOトレードオフを整理し、フェイルオーバー/フェイルバック手順やDRテスト方法まで具体的に解説する。
