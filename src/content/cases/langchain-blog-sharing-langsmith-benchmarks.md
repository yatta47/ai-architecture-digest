---
type: announcement
title: LangSmithが公開したLLMアーキテクチャ横断のQ&Aベンチマーク
title_original: Sharing LangSmith Benchmarks
industry: cross-industry
cloud: []
patterns:
- eval
- rag
components:
- LangSmith
- langchain-benchmarks
- ChromaDB
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/public-langsmith-benchmarks
published_at: '2026-06-16'
---

## 概要

LangSmithがLangChainドキュメントに対するQ&Aベンチマークとlangchain-benchmarksパッケージを公開し、異なるLLM・認知アーキテクチャ(chain/agent/assistant)の性能を、集計スコアだけでなくステップ単位のトレースまで含めて誰でも再現・比較できるようにした。

## 設計のポイント

- 評価結果を集計指標だけでなく個々のトレース単位で公開し、アーキテクチャ間の違いを再現可能にする
- 同一データセット・同一評価基準で異なるLLMや認知アーキテクチャ(chain/agent/assistant)を横並び比較する
- コサイン距離とLLM採点スコアの両方を使い、多角的に回答品質を測る

## 使いどころ

- RAGやエージェントの実装方式を選定する前に客観的なベンチマークで比較したい場合
- 自社アーキテクチャの性能を公開ベンチマークと比較し妥当性を確認したい場合
