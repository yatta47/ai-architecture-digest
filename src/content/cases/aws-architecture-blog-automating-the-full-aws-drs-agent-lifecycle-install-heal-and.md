---
type: case
title: SSM AutomationでAWS DRSエージェントの導入・修復・撤去を自動化
title_original: 'Automating the full AWS DRS agent lifecycle: Install, heal, and offboard'
ai_relevant: false
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: reliability
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/automating-the-full-aws-drs-agent-lifecycle-install-heal-and-offboard/
published_at: '2026-11-02'
---

## 概要

300台超のEC2でAWS DRSのレプリケーションエージェントが停止したり、対象外のサーバーが課金され続ける問題に対し、導入・修復・撤去をSSM Automationドキュメントで自動化した事例。EC2タグの値で適用フェーズを切り替え、Lambdaを使わずに運用する。
