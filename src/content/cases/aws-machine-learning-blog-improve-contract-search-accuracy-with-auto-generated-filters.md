---
type: case
title: 'AIDA: メタデータフィルタリングで精度を高めた契約書検索RAG'
title_original: Improve contract search accuracy with auto-generated filters in Amazon Bedrock
industry: media
cloud:
- aws
patterns:
- rag
- document-processing
- guardrails
components:
- Amazon Bedrock Knowledge Bases
- Amazon Bedrock Guardrails
- Amazon OpenSearch Service
- Amazon S3 Vectors
- AWS IAM
- Amazon CloudWatch
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/improve-contract-search-accuracy-with-auto-generated-filters-in-amazon-bedrock/
published_at: '2026-08-18'
---

## 概要

エンタメ・メディア業界などで複数法域にまたがる大量の契約書を扱う企業向けに、AWS上のRAGソリューション「AIDA」が自然言語での契約書横断検索を可能にする。効力発生日や当事者などのメタデータでインプリシット/エクスプリシットにフィルタリングしてから意味検索を行う二段階の絞り込みにより、関連条項の見落としや誤読を防ぐ。

## 設計のポイント

- 契約書の取り込み時に当事者・発効日・終了日・法域などの構造化メタデータを付与し、チャンク分割はセマンティックな意味のまとまりを保ちながら簡潔にする
- ベクトル検索の前にメタデータによる暗黙的フィルタリングでまず検索対象を絞り込み、その後にコサイン類似度による意味検索を行う二段階のRAGで精度を高める
- クエリ時にはBedrock Guardrailsでプロンプトインジェクションや情報漏えいを防ぎ、応答生成時にも同GuardrailsでコンテンツフィルタリングとPII保護を適用する
- Retrieve APIで応答を元の契約書ソースまでトレース可能にし、ハルシネーションを抑えつつ根拠を提示できるようにする

## 使いどころ

- 複数の法域・大量の契約書を抱え、自然言語での横断検索が必要な企業法務・コンプライアンス部門
- 一般的な意味検索だけではLLMが処理しきれない量の文書が返ってきてしまうRAGシステムの精度改善
- 回答の根拠となる原文書への追跡可能性が求められる、コンプライアンス要件の強い文書QAシステム
