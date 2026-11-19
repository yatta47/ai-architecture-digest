---
type: case
title: AWS Neuron上の埋め込み推論をエージェント開発で最適化し数百億件を処理
title_original: Exa boosts embedding throughput by 50% to index billions of documents on AWS AI chips
company: Exa
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- cost-optimization
components:
- AWS Inferentia2
- AWS Trainium2
- AWS Neuron
- Exa vector database
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/exa-boosts-embedding-throughput-by-50-to-index-billions-of-documents-on-aws-ai-chips/
published_at: '2026-11-18'
---

## 概要

ExaはWebインデックス用の埋め込み生成をAWS Inferentia2/Trainium2に移し、エージェント型の開発ワークフローで最適化して、スループットを50%向上させた。300億件規模の再埋め込みでは1件あたりコストが全体に効く。

## 設計のポイント

- 数百億件規模では1件あたりの埋め込みコストを最優先の指標にする。
- 非同期パイプラインで取得、解析、フィルタ、埋め込み、配信を分離する。
- Neuron向けの最適化にエージェント開発を使う。

## 使いどころ

- 大量文書の埋め込みや再埋め込みを行う検索基盤。
- ベクトル検索のコスト削減を狙うチーム。
