---
type: guidance
title: Cohesity HeliosによるGoogle Cloudでのデータ管理とバックアップ
title_original: Data management with Cohesity Helios and Google Cloud
ai_relevant: false
industry: cross-industry
cloud:
- gcp
patterns: []
components: []
outcome:
  type: reliability
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/partners/using-cohesity-with-cloud-storage-for-enterprise-hybrid-data-protection
published_at: '2026-07-22'
---

## 概要

この記事はCohesity HeliosデータプラットフォームをGoogle Cloudと組み合わせて、Compute EngineやVMware EngineのVM、SAP HANAなどのアプリケーションワークロードをバックアップ・復旧する方法を解説する。Cloud Storageの各ストレージクラスを長期アーカイブ先として利用し、Cohesity SmartFilesでNFS/SMBによるファイルサービスも提供する。Cloud Storageを外部ターゲットとして登録し、アーカイブポリシーを作成する具体的な設定手順も示している。
