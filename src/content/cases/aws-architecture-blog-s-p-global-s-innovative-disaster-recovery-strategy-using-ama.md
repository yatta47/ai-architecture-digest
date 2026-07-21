---
type: case
title: S&P Global、FSx for NetApp ONTAPのスナップショット×FlexCloneで15分以内のDRフェイルオーバーを実現
title_original: S&P Global's innovative disaster recovery strategy using Amazon FSx for NetApp ONTAP snapshots
ai_relevant: false
company: S&P Global
industry: financial-services
cloud:
- aws
patterns: []
components: []
outcome:
  type: reliability
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/sp-globals-innovative-disaster-recovery-strategy-using-amazon-fsx-for-netapp-ontap-snapshots/
published_at: '2026-07-07'
---

## 概要

S&P Global Market IntelligenceはCapital IQプラットフォームのDR戦略として、Amazon FSx for NetApp ONTAPのSnapMirrorレプリケーションとFlexCloneを組み合わせ、リージョン障害時に読み取り専用モードへ15分以内でフェイルオーバーできる仕組みを構築した。その後、地理クラスタ構成に基づき読み書き可能な完全復旧へ移行する二段階アプローチを採用している。
