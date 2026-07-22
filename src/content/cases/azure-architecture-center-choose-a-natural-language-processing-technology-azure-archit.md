---
type: guidance
title: 自然言語処理技術の選定ガイド（Azure AI Language vs Spark NLP）
title_original: Choose a natural language processing technology
industry: cross-industry
cloud:
- azure
patterns:
- document-processing
components:
- Azure AI Language
- Apache Spark NLP
- Azure Databricks
- Microsoft Fabric
outcome:
  type: quality
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/data-guide/technology-choices/natural-language-processing
published_at: '2026-04-21'
---

## 概要

感情分析・固有表現抽出・文書分類・要約といった自然言語処理タスクに対し、API駆動のマネージドサービスであるAzure AI Languageと、Azure Databricks/Microsoft Fabric上のSpark NLPという分散OSSフレームワークをどう使い分けるかを整理するガイド。自然言語処理と言語モデル（LLM）の違いも明確化している。

## 設計のポイント

- 自然言語処理（トークナイズ・固有表現抽出等の広い技術群）と言語モデルの深層学習的アプローチを区別してから技術選定に入る
- 手軽さと運用負荷の低さを優先するならAzure AI Languageのマネージド型API、カスタム性やスケールを優先するならSpark NLPを選ぶ

## 使いどころ

- 既製のAPIで十分な感情分析・エンティティ抽出をすぐに使いたいチーム
- 大規模データ基盤上でカスタムNLPパイプラインを構築したいデータエンジニアリングチーム
