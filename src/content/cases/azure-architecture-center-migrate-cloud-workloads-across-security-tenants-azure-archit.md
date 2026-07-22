---
type: guidance
title: セキュリティテナント間でのクラウドワークロード移行アーキテクチャ
title_original: Migrate cloud workloads across security tenants
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/migrate-cloud-workloads-across-security-tenants
published_at: '2026-05-04'
---

## 概要

M&Aなどの組織再編に伴い、Microsoft Entraテナントをまたいでクラウドワークロードを移行するためのソリューションアイデア。元テナントに一時的な『サイドカーサブスクリプション』を作成してデータをクローン・バックアップし、ARMテンプレートとIaCで新テナントの対象リソースグループへ再デプロイしたのち、サブスクリプションごと新テナントへ移動して復元する。セキュリティ境界を保ちながら事業継続性を確保する移行戦略を示す。
