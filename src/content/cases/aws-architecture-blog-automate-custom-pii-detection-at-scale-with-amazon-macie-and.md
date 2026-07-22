---
type: case
title: Amazon MacieとStep Functionsで実現する大規模カスタムPII自動検出パイプライン
title_original: Automate custom PII detection at scale with Amazon Macie and Step Functions
ai_relevant: false
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/automate-custom-pii-detection-at-scale-with-amazon-macie-and-step-functions/
published_at: '2026-07-22'
---

## 概要

金融・保険・医療・公共など規制業界向けに、S3へのファイル到着をイベント駆動で検知しMacieによるPII検出を自動実行するパイプラインを構築する事例。標準のPII識別に加え、ポリシー番号や会員IDなど組織固有のデータ形式をカスタムデータ識別子で検出し、監査用レポート生成と高深刻度検知時のリアルタイム通知までを人手を介さず実現する。
