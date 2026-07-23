---
type: guidance
title: オンプレミスとAzure Filesを統合したハイブリッドファイル共有構成
title_original: Use Azure file shares in a hybrid environment
ai_relevant: false
industry: cross-industry
cloud:
- azure
- on-prem
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/hybrid/azure-file-share
published_at: '2026-01-23'
---

## 概要

本アーキテクチャは、オンプレミスのActive Directory Domain Services(AD DS)とMicrosoft Entra IDを連携させ、Azure FilesをAD DS認証で保護されたクラウドファイル共有として既存のオンプレミス環境に統合する構成を示す。オンプレミスファイルサーバーの置き換え・リフト&シフト・バックアップ/災害復旧・Azure File Syncによるハイブリッド運用など、既存資格情報を維持したまま段階的にクラウド移行するユースケースを想定している。
