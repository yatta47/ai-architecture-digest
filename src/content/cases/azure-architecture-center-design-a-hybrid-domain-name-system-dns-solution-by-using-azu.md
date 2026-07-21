---
type: guidance
title: Azureランディングゾーン向けにハブスポーク構成でハイブリッドDNSを設計するアーキテクチャガイド
title_original: Design a hybrid Domain Name System (DNS) solution by using Azure
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/hybrid/hybrid-dns-infra
published_at: '2026-06-18'
---

## 概要

Azureランディングゾーン実装の重要な要素として、オンプレミスとAzure、他クラウドにまたがるワークロードのドメイン名を解決するハイブリッドDNS設計を解説する。Azure DNS Private ResolverをハブVNetに配置し、Azure FirewallのDNSサーバー設定と組み合わせて、集中型・分散型のいずれのDNSアーキテクチャでもAzure⇔オンプレミス間の双方向の名前解決を実現する具体的なIPアドレス設計を示している。
