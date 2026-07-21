---
type: guidance
title: RAGソリューションのプロンプトエンジニアリング:検索結果を根拠づけて答えさせる設計
title_original: RAG prompt engineering
industry: cross-industry
cloud:
- azure
patterns:
- rag
- prompt-optimization
- context-engineering
components: []
outcome:
  type: quality
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-prompt-engineering
published_at: '2026-07-02'
---

## 概要

RAG(検索拡張生成)における情報検索後の工程として、システムメッセージとシナリオ別インストラクションを分離し、モデルに『提供されたコンテキストのみを根拠に回答させる』ためのプロンプト構造・グラウンディング手法をまとめたガイド。カスタマーサポート・法務調査・技術ドキュメントなど用途別のプロンプト例も示す。

## 設計のポイント

- システムメッセージ(役割・グラウンディング制約など普遍的な部分)とシナリオ別インストラクション(業務固有のルール)を分離し、シナリオが変わってもシステムメッセージを使い回せるようにする
- コンテキストに答えがない場合の振る舞いや、複数出典が矛盾する場合の扱いを明示的にインストラクションへ書き、モデルの外挿を防ぐ
- エージェント型RAGではリトリーバルをツールとして扱い、いつ・どう呼び出すかをツール説明文とエージェント指示で制御する、通常RAGとは別の設計が必要になる

## 使いどころ

- 検索結果を根拠にした回答生成の精度・グラウンディングを改善したいRAGシステムの開発者
- カスタマーサポート・法務・技術文書など、ドメインごとに異なる引用/免責ルールを持つRAGアプリ
