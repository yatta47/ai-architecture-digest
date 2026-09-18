---
type: case
title: CSIROがサーバーレス構成で低コストなゲノムバリアント検索基盤sBeaconを構築
title_original: How CSIRO built scalable, cost-optimized genomic variant querying on AWS
ai_relevant: false
company: CSIRO
industry: healthcare
cloud:
- aws
patterns: []
components: []
outcome:
  type: cost
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/how-csiro-built-scalable-cost-optimized-genomic-variant-querying-on-aws/
published_at: '2026-09-18'
---

## 概要

オーストラリア国立科学機関CSIROは、ゲノムデータ共有の標準プロトコルBeaconを実装したServerless Beacon（sBeacon）を、S3・Lambda・DynamoDB・Athenaによるサーバーレス構成で構築した。数億人規模のコホートまでスケールしながら、1000 Genomes相当のデータセットで月額約0.40ドルという低コストと、約5秒での実クエリ応答を両立している。
