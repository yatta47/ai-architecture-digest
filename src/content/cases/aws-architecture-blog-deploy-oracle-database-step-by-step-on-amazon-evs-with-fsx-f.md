---
type: guidance
title: Amazon EVSとFSx for ONTAPでOracle DBを構築する手順書
title_original: Deploy Oracle Database step by step on Amazon EVS with FSx for ONTAP
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
source_url: https://aws.amazon.com/blogs/architecture/deploy-oracle-database-step-by-step-on-amazon-evs-with-fsx-for-ontap/
published_at: '2026-10-02'
---

## 概要

Amazon EVS上のVMware環境にFSx for NetApp ONTAPをNFSデータストアとして接続し、Oracle 19cを導入してSnapMirrorでリージョン間DRを構成する手順を解説する。4つの移行パス、スナップショットバックアップ、PITR、DBクローンなどの日次運用も扱う。AI関連ではなく汎用インフラ手順の記事。
