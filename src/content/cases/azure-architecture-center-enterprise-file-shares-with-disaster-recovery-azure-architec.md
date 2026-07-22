---
type: guidance
title: Azure NetApp Filesによるエンタープライズファイル共有のDR構成
title_original: Enterprise file shares with disaster recovery
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/file-storage/enterprise-file-shares-disaster-recovery
published_at: '2026-06-03'
---

## 概要

Azure NetApp Filesのクロスリージョンレプリケーションと Windows Server DFS Namespacesを組み合わせ、クライアントに透過的なフェイルオーバーを実現するファイル共有アーキテクチャ。SMB共有を要するデスクトップ/アプリケーション向けに、リージョン障害時の自動復旧を提供する。
