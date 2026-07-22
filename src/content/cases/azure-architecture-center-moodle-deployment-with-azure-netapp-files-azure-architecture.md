---
type: guidance
title: Azure NetApp Filesを使ったMoodle（LMS）の高可用構成
title_original: Moodle deployment with Azure NetApp Files
ai_relevant: false
industry: other
cloud:
- azure
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/file-storage/moodle-azure-netapp-files
published_at: '2026-06-03'
---

## 概要

オープンソース学習管理システムMoodleを、Virtual Machine Scale SetsとAzure NetApp Filesの組み合わせでゾーン冗長にデプロイする構成。クロスゾーンレプリケーションによるディザスタリカバリと、需要に応じたスケールイン/アウトの設計を示す。
