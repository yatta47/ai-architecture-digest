---
type: guidance
title: 多層防御によるAzure仮想マシンアクセス保護（JITアクセス＋Bastion＋PIM）
title_original: Multilayered protection for Azure virtual machine access
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/multilayered-protection-azure-vm
published_at: '2026-06-03'
---

## 概要

Microsoft Entra Conditional Access・Entra PIMによるJust-In-Timeロール昇格・Defender for CloudのJIT VMアクセス・Azure Bastionを組み合わせ、RDP/SSHポートを常時公開せずに最小権限で管理アクセスを提供する多層防御アーキテクチャ。
