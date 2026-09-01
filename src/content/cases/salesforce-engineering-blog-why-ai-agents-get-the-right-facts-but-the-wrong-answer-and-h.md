---
type: case
title: GraphRAGでAgentforceの複数ホップ推論による誤答を防ぐ
title_original: Why AI Agents Get the Right Facts but the Wrong Answer—and How GraphRAG Helps
company: Salesforce
industry: retail
cloud: []
patterns:
- rag
- ai-agent
components:
- Agentforce
- GraphRAG
outcome:
  type: quality
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/why-ai-agents-get-the-right-facts-but-the-wrong-answer-and-how-graphrag-helps/
published_at: '2026-08-31'
---

## 概要

通常のRAGは関連する文書チャンクを個別に取得できても、複数の文書やレコードにまたがる条件（商品分類・会員ランク・購入額など）を結び付けられず、正しい根拠を示しながら誤った結論を出すことがある。SalesforceはAgentforceにナレッジグラフを組み込んだGraphRAGを導入し、エンティティ間の関係をたどるマルチホップ検索で見落とされがちな例外条件を発見できるようにした。

## 設計のポイント

- TBox（エンティティ型と関係の定義）とABox（実際のレコード）を分離し、AIが提案したグラフ構造を業務担当者がレビューしてから実データを投入する
- 文書由来の概念と構造化データ（カタログ・CRM等）を明示的なポインタで結び付け、実行時に毎回マッピングを推論させない
- 検索の失敗を『単純な参照』と『複数条件をまたぐ判断』に切り分け、後者にのみグラフの多段階トラバーサルを適用する

## 使いどころ

- 返品・値引きなど複数の業務ルールが絡む問い合わせに答えるカスタマーサポートエージェント
- 文書とマスタデータの両方に条件が分散している業務でRAGの誤答を減らしたいチーム
- ナレッジグラフの構造レビューを業務側と協働させたいAIプラットフォームチーム
