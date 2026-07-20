---
type: guidance
title: Azure Backupによるランサムウェア耐性バックアップアーキテクチャ
title_original: Design a ransomware-resilient backup architecture by using Azure Backup
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/security/ransomware-resilient-backup-architecture/
published_at: '2026-07-08'
---

## 概要

ランサムウェア攻撃は本番環境だけでなくバックアップも標的にするため、削除・変更不可能で本番から独立して復旧できる2つのイミュータブルなバックアップコピーを異なるサブスクリプション・リージョンに保持するアーキテクチャを提案している。バックアップ管理を本番運用から分離し、Resource GuardやMUAによる承認境界、保持期間ポリシー、定期的な復元ドリルを組み合わせることで、攻撃発覚後も汚染されていない復旧ポイントから安全に復旧できるようにする。
