---
type: case
title: Salesforceのプライベート接続基盤「Private Connect」刷新でAgentforce導入のセキュリティ障壁を解消
title_original: Removing the Security Barrier to Agentforce Adoption
ai_relevant: false
company: Salesforce
industry: cross-industry
cloud:
- aws
- azure
- multi-cloud
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/removing-the-security-barrier-to-agentforce-adoption/
published_at: '2026-08-03'
---

## 概要

Salesforceは、AgentforceやData 360などのAIサービスと顧客環境をパブリックインターネットを経由せず接続する専用ネットワーク層「Private Connect」を、AWS専用のVPN・プロキシ方式からマルチクラウド対応の軽量アーキテクチャ(v2.0)へと刷新した。プライベートリンクとトランジットゲートウェイを用いた直接エンドポイント接続により、プロビジョニング時間を数週間から30分未満に短縮しつつ、月間約120TB・6億8300万リクエストを15のAWSリージョンで処理する規模まで成長させ、医療・金融・政府など規制業界におけるAI導入時のセキュリティレビューの障壁を取り除いた。
