---
type: guidance
title: GitHubで実装するInfrastructure as CodeのDevSecOpsパイプライン
title_original: DevSecOps for infrastructure as code (IaC)
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/devsecops-infrastructure-as-code
published_at: '2026-06-03'
---

## 概要

GitHub ActionsとTerraformを用いたIaCパイプラインに、CodeQLによる静的解析、Microsoft Defender for CloudとSentinelによる継続的監視、Azure Policyによるコンプライアンス強制を組み込んだDevSecOpsアーキテクチャを解説する。構成ドリフトを検知するとGitHub Issueを自動起票してガバナンスを閉じるループを作る。
