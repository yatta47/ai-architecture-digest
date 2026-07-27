---
type: guidance
title: ハイブリッド環境でのActive Directory活用パターン
title_original: Patterns for using Active Directory in a hybrid environment
ai_relevant: false
industry: cross-industry
cloud:
- gcp
- on-prem
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/patterns-for-using-active-directory-in-a-hybrid-environment
published_at: '2026-07-21'
---

## 概要

Google CloudへActive Directoryを展開する際のドメイン/フォレストアーキテクチャの選び方を解説するガイド。単一ドメインを複数環境に拡張する方式と、別ドメイン/フォレストをトラストで接続する方式のどちらを選ぶかを、既存セキュリティゾーンとの整合性やオンプレミスとの相互作用などの観点から判断する。
