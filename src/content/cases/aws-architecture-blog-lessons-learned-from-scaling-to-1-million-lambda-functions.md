---
type: case
title: AWS Lambda関数100万規模へのマルチアカウントSaaSスケーリング教訓
title_original: Lessons learned from scaling to 1 million Lambda functions
ai_relevant: false
company: ProGlove
industry: manufacturing
cloud:
- aws
patterns: []
components: []
outcome:
  type: cost
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/lessons-learned-from-scaling-to-1-million-lambda-functions/
published_at: '2026-06-29'
---

## 概要

ウェアラブルバーコードスキャナー企業ProGloveが、AWSベースのSaaSプラットフォーム「Insight」をテナントごとに1つのAWSアカウントを割り当てるマルチアカウント方式で運用し、Lambda関数が100万を超える規模まで成長する過程で得た教訓をまとめた記事。CloudFormation StackSetsによる一括デプロイ、Step Functionsによるアカウント自動プロビジョニング、スケジュール分散によるセルフDDoS回避、オブザーバビリティコストの最適化など、各フェーズで直面した課題と対策を紹介する。
