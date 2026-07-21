---
type: guidance
title: プライベートリンクで守るゾーン冗長App Serviceのベースライン構成
title_original: Baseline highly available zone-redundant web application
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/web-apps/app-service/architectures/baseline-zone-redundant
published_at: '2026-07-02'
---

## 概要

Azure Application Gateway＋WAFを唯一の公開エンドポイントとし、Azure Private Linkでゾーン冗長なApp ServiceからKey Vault・SQL Database・Storageへプライベート接続する、セキュアで高可用なWebアプリのベースラインリファレンスアーキテクチャ。インバウンド／アウトバウンドのトラフィックフローをステップごとに定義し、そのまま本番実装の土台として使えるサンプル実装も提供する。
