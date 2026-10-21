---
type: case
title: Octaveの規制業種向けマルチテナントAI基盤(Bedrock)
title_original: How Octave built a secure multi-tenant AI foundation on Amazon Bedrock
company: Octave
industry: manufacturing
cloud:
- aws
patterns:
- multi-tenant-rag
- rag
- defense-in-depth
- document-processing
components:
- Amazon Bedrock
- Cohere Embed v4
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-octave-built-a-secure-multi-tenant-ai-foundation-on-amazon-bedrock/
published_at: '2026-10-20'
---

## 概要

Octaveは1.4万超の顧客を抱える品質管理SaaSで、テナント分離を絶対条件に、個別機能でなく水平のAI基盤を先に構築した。20億文書を埋め込み、クレームトリアージ支援で実証し、ユースケース当たりの展開時間を50%削減した。

## 設計のポイント

- 個別機能でなく共通基盤を先に作り、縦の機能を後から載せる。
- テナント境界を越えない分離を設計の前提にする。
- Cohere Embed v4をBedrockで使い、多言語・多形式文書を意味検索する。

## 使いどころ

- データ漏えいが規制リスクとなるSaaSへのAI導入。
- 過去の不具合・CAPAを横断検索する品質調査。
