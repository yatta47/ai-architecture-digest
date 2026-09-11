---
type: case
title: エンタープライズ文書RAGの精度をパイプライン逆算デバッグで46%から90%超へ改善
title_original: 'Enterprise AI Accuracy: Building a More Trustworthy RAG Application'
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- rag
- document-processing
components:
- Intelligent Parsing
outcome:
  type: quality
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/enterprise-ai-accuracy-building-a-more-trustworthy-rag-application/
published_at: '2026-09-09'
---

## 概要

SalesforceのRAGパイプラインは標準的なテキストベンチマークで90%超の精度だったが、表のヘッダーが分断される、無関係な文書が検索されるといった問題で、複雑なエンタープライズ文書では約46%まで精度が低下した。生成結果から逆向きに検索・チャンキング・パースの各段階を切り分けてデバッグし、ページの複雑さに応じてパース方式を振り分けるIntelligent Parsingを導入することで、ある評価では精度を65.1%から84.4%まで改善した。

## 設計のポイント

- 誤答の原因をLLMの推論力ではなく、パース→チャンキング→埋め込み→検索→生成のどの段階で情報の意味が失われたかを切り分けて診断する
- ページの複雑さ(単純テキストか、表・図・merged cellsを含むか)に応じて決定的パーサーとLLM/vision処理を使い分けるルーティングを行う
- チャンキングを容量制約ではなく意味的境界の単位として設計し、複数ページにまたがる表を1つの論理単位として保持する
- エンドツーエンドの精度を単一指標として扱わず、各段階の出力を個別にテストして責任の所在を特定する

## 使いどころ

- 標準ベンチマークでは高精度なのに本番運用で誤答が目立つRAGシステムの原因調査に
- 財務諸表・保険約款・製造マニュアルなど、表や図を含む複雑なエンタープライズ文書を扱うRAG基盤の設計に
