---
type: guidance
title: DeepEvalでRAGパイプラインを定量評価する手法
title_original: Evaluating RAG with DeepEval and LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- eval
components:
- LlamaIndex
- DeepEval
- OpenAI GPT-4o
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/evaluating-rag-with-deepeval-and-llamaindex
published_at: '2026-07-19'
---

## 概要

DeepEvalが提供するAnswer Relevancy・Faithfulness・Contextual PrecisionなどのLLM評価指標を使い、LlamaIndexで構築したRAGパイプラインの応答品質を定量的にテストする方法を解説する。各指標がパイプラインのどの構成要素（プロンプト・モデル・リランカー）に対応するかを整理し、スコア低下の原因特定に役立てる。

## 設計のポイント

- Answer Relevancy・Faithfulness・Contextual Precisionなど指標ごとに責任範囲（プロンプト/LLM/リトリーバ）を切り分けて原因診断をしやすくする
- LLMTestCaseに入力・出力・retrieval_contextをまとめてテストケース化し、CIでのユニットテストのように再現可能な評価を行う
- top-Kや類似度しきい値などのハイパーパラメータをスコアに紐づけて比較検証する

## 使いどころ

- RAGパイプラインの品質改善サイクルを属人的なレビューから定量評価に置き換えたいチーム
- プロンプトテンプレートやモデル変更のA/Bを数値で比較したい場合
