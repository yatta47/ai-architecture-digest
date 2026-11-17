---
type: case
title: OpenSearchで構築した銀行の集中オブザーバビリティ基盤
title_original: How Rakbank built centralized observability at scale with Amazon OpenSearch Service
ai_relevant: false
company: Rakbank
industry: financial-services
cloud:
- aws
patterns: []
components: []
outcome:
  type: cost
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/how-rakbank-built-centralized-observability-at-scale-with-amazon-opensearch-service/
published_at: '2026-11-17'
---

## 概要

Rakbankは日量約150GBのテレメトリをクロスアカウント・Multi-AZのOpenSearch Serviceに集約し、ホット/ウォーム/コールド階層と7年保管のS3アーカイブを組み合わせた。全ホット構成比で約55%のコスト削減となった。AI/LLMは主題でないため軽量カードとする。
