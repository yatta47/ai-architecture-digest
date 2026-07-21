---
type: guidance
title: エージェント型RAG(Agentic RAG)の実装ガイド
title_original: Develop an agentic RAG solution
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- rag
- context-engineering
components:
- Microsoft Agent Framework
- Foundry Agent Service
outcome:
  type: quality
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-agentic
published_at: '2026-06-30'
---

## 概要

標準RAGの固定パイプラインでは対応しきれない多段階推論やソース選択が必要な場面に向けた、エージェント型RAGの設計と実装を解説する記事。AIエージェントが検索をオンデマンドで呼び出せるツールとして扱い、クエリを理解し、次のアクションを判断し、中間結果を評価し、十分な文脈が得られるまで反復するループを構成する。Microsoft Agent FrameworkとFoundry Agent Serviceを用いた実装方法を示す。

## 設計のポイント

- 固定パイプラインではなく、エージェントが検索ツールを呼び出すか判断する推論ループとして構成する。
- エージェントは中間結果を評価し、十分な文脈が得られるまで反復的にツール呼び出しを行う。
- 単一検索で解決できる単純なクエリには標準RAGを使い、複雑な場合のみエージェント型RAGを採用してレイテンシとトークン消費のコストを抑える。
- Microsoft Agent FrameworkやFoundry Agent Serviceを用いて検索をツール呼び出しとして構造化する。

## 使いどころ

- 複数のデータソースを横断する多段階推論が必要な質問応答(例: 製品カタログとリコール規制データベースの突合)に効く。
- 実行時にどのデータソースを問い合わせるか動的に選択する必要があるシナリオに向く。
- 複雑な質問をサブクエリに分解し、個別に検索・比較する必要がある場合に有効。
- 検索で得た情報をもとに後続のアクション(注文履歴取得後の返品処理など)を同一ワークフロー内で実行するエージェントに適する。
