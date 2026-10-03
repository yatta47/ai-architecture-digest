---
type: guidance
title: Amazon EVSとFSx for ONTAPによるOracle高可用性アーキテクチャ設計
title_original: Architect highly available Oracle Database on Amazon EVS and FSx for ONTAP
ai_relevant: false
company: AWS
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: reliability
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/architect-highly-available-oracle-database-on-amazon-evs-and-fsx-for-ontap/
published_at: '2026-10-02'
---

## 概要

VMware Cloud Foundationを使う企業がOracle DBをAWSへ再設計なしで移行するため、Amazon EVS、EC2ベアメタル、FSx for ONTAPのNFSデータストア、SnapMirrorによるクロスリージョンDRをどう組み合わせるかを解説する。サブミリ秒のストレージレイテンシと既存VMware運用の維持が狙い。AIアーキテクチャではなく汎用インフラの設計記事。
