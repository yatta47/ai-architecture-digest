---
type: guidance
title: Azure File Syncによるオンプレミス⇔クラウドのハイブリッドファイル共有
title_original: Hybrid file services
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/hybrid/hybrid-file-services
published_at: '2026-07-02'
---

## 概要

Azure FilesとAzure File Syncを組み合わせ、オンプレミスのファイルサーバーとクラウドのファイル共有を同期させるハイブリッドアーキテクチャ。直接SMBマウントする方式と、オンプレミスのWindows ServerをAzureファイル共有のキャッシュとして使う方式の2通りを比較する。
