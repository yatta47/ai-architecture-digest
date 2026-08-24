---
type: case
title: AWS Organizations移行時にRAM共有とLake Formation権限を維持する一時ブリッジ共有パターン
title_original: How a global payment processor preserved AWS RAM shares and Lake Formation permissions during an AWS Organizations
  migration
ai_relevant: false
industry: financial-services
cloud:
- aws
patterns: []
components: []
outcome:
  type: reliability
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/how-a-global-payment-processor-preserved-aws-ram-shares-and-lake-formation-permissions-during-an-aws-organizations-migration/
published_at: '2026-08-24'
---

## 概要

大手決済処理企業が、元親会社からの分離に伴う382のAWSアカウントのOrganizations間移行で、AWS RAMの組織バウンド共有が失われることでAWS Transit GatewayやLake Formation権限のコントロールプレーンアクセスが失われる問題に直面した。組織外プリンシパルとして「一時的なブリッジ共有」を作成してから移行し、移行後に元の共有へ復帰させることでデータプレーンを止めずに移行を完了した。
