---
type: guidance
title: サプライチェーン攻撃に強いセキュアなデプロイパイプライン設計
title_original: Design secure deployment pipelines
ai_relevant: false
industry: cross-industry
cloud:
- gcp
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/design-secure-deployment-pipelines-bp
published_at: '2026-07-25'
---

## 概要

デプロイパイプライン自体がパイプライン汚染攻撃やサプライチェーン攻撃の標的になりうることを踏まえ、CI/CDシステムから入力アーティファクトまで含めたアクセスのグラフ全体を評価してセキュアなパイプラインを設計する方法を解説する。データの機密性・完全性・可用性からリソースの機微度を評価する手順を示す。
