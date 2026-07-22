---
type: guidance
title: Azureにおけるネットワーク仮想アプライアンス(NVA)の高可用性デプロイパターン
title_original: Deploy highly available NVAs
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/networking/guide/network-virtual-appliance-high-availability
published_at: '2026-04-07'
---

## 概要

Azure上でネットワーク仮想アプライアンス(NVA、ファイアウォールやVPN/SD-WANアプライアンスなど)を高可用性構成にする代表的な4パターンを比較したガイダンス記事。ロードバランサー方式、Azure Route Server方式、Gateway Load Balancer方式、動的パブリックIP+UDR方式それぞれについて、フェイルオーバーの収束時間、対応トポロジ(アクティブ/アクティブやスケールアウト)、SNATの要否によるトラフィック対称性の違いを整理している。共通の推奨事項として、可用性ゾーンをまたいだNVA配置なども挙げている。
