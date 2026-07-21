---
type: guidance
title: RAGのチャンクをクレンジングとメタデータ付与で強化し、検索精度とプロンプトインジェクション耐性を高める
title_original: RAG chunk enrichment phase
industry: cross-industry
cloud:
- azure
patterns:
- rag
- document-processing
- guardrails
components: []
outcome:
  type: quality
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-enrichment-phase
published_at: '2026-06-18'
---

## 概要

チャンク分割後の強化フェーズとして、小文字化・ストップワード除去・スペル修正・Unicode正規化などのクレンジングによりベクトル検索の意味的な一致精度を高める手法と、タイトル・要約・キーワード・想定質問といったメタデータをチャンクに付与してフィルタや複合検索を可能にする手法を整理する。取り込み対象のコンテンツに埋め込まれた指示文をエージェントやモデルへの指示として決して解釈しないよう、プロンプトインジェクション対策の必要性にも言及している。

## 設計のポイント

- 元のチャンクとクレンジング済みチャンクを別フィールドとして両方保持し、検索は正規化後のベクトルで行い、結果表示には原文を使うという役割分担にする。
- ストップワード除去やUnicode除去は次元削減に有効な一方で意味を持つ場合もあるため、機械的に適用せず対象データで効果を検証してから採用する。
- 取り込むコンテンツに埋め込まれた指示文をエージェントへの命令として絶対に解釈しないという原則を明示し、フラグ付けや除外、制約付きデコーディングによる分類を検討する。

## 使いどころ

- 全文検索と意味検索を組み合わせたいが、チャンクにどのメタデータを持たせるべきか設計基準が欲しいRAG設計者。
- 取り込み対象の文書が外部から投稿される可能性があり、プロンプトインジェクション対策を検討したいチーム。
- 検索結果の質を上げるために、クレンジング処理の効果をデータドリブンに検証したいエンジニア。
