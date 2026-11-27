---
type: guidance
title: RA-DIT：LLMと検索器を二段階で調整してRAGを強化
title_original: Improving RAG Effectiveness with Retrieval-Augmented Dual Instruction Tuning (RA-DIT)
company: Meta
industry: cross-industry
cloud: []
patterns:
- rag
- fine-tuning
components:
- RA-DIT
- LLaMA 65B
- LlamaIndex
- REPLUG
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/improving-rag-effectiveness-with-retrieval-augmented-dual-instruction-tuning-ra-dit-01e73116655d
published_at: '2023-10-18'
---

## 概要

Metaが提案したRA-DITは、LLMと検索器を別々にファインチューニングして検索拡張の性能を高める手法である。知識集約タスクで未調整の検索拡張モデルを上回る結果が示されている。

## 設計のポイント

- LLMは検索文脈を使いつつ、誤った検索結果にも耐えるように調整する。
- 検索器はLLMの評価をフィードバックにして調整する（LM-Supervised Retrieval）。
- 学習データは取得ノードからQ&Aを合成して作る。

## 使いどころ

- プロンプト調整だけではRAGの精度が頭打ちになったチーム。
