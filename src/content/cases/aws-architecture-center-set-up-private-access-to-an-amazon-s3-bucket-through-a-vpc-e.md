---
type: guidance
title: VPCエンドポイント経由でS3への非公開アクセスを実現する構成
title_original: Set up private access to an Amazon S3 bucket through a VPC endpoint
ai_relevant: false
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: aws-architecture-center
source_name: AWS Architecture Center
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-private-access-to-an-amazon-s3-bucket-through-a-vpc-endpoint.html?did=pg_card&trk=pg_card
published_at: '2024-03-28'
---

## 概要

presigned URLをインターネットを経由せず社内ネットワークからのみ利用可能にするため、ALB・API Gateway・Lambda・S3用VPCエンドポイントを組み合わせたサーバーレス構成を解説。S3バケット名をドメイン名と一致させる制約や監視・入力検証を追加する際の注意点も示す。
