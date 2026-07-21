---
type: guidance
title: 高可用性を備えたSAP BW/4HANAアプリケーション層をAzure仮想マシンで構成するリファレンスアーキテクチャ
title_original: Run SAP BW/4HANA with Linux virtual machines on Azure
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/sap/run-sap-bw4hana-with-linux-virtual-machines
published_at: '2026-06-22'
---

## 概要

SAP BW/4HANAのアプリケーション層を高可用性を持たせてAzure上のLinux仮想マシンで構成するリファレンスアーキテクチャを示す。SAP Web DispatcherとAzure Load Balancerによる負荷分散、Azure Bastionによる安全なリモートアクセス、Azure NetApp FilesやAzure Backup/Site Recoveryによるデータ保護と災害復旧を組み合わせ、小〜中規模の本番環境向けの構成をまとめている。
