---
type: guidance
title: Azure NetApp FilesによるTeamcenter PLMストレージ基盤
title_original: Use Teamcenter PLM with Azure NetApp Files
ai_relevant: false
industry: manufacturing
cloud:
- azure
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/manufacturing/teamcenter-plm-netapp-files
published_at: '2026-06-11'
---

## 概要

Siemens Teamcenter PLMのストレージ基盤としてAzure NetApp Filesを活用するマルチゾーン構成のリファレンスアーキテクチャ。SQL Server Always On可用性グループによるデータベースの同期レプリケーションと、Azure NetApp Filesのゾーン間非同期レプリケーションを組み合わせ、CADファイルや製品データに低遅延かつ高可用なアクセスを提供する。設計管理、BOM管理、原価管理など複数のPLMユースケースにおいて、パフォーマンスと耐障害性を両立する狙いがある。
