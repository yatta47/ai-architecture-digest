---
type: guidance
title: UpTrainでRAGパイプラインの各段階を評価する
title_original: Supercharge your LlamaIndex RAG pipeline with UpTrain evaluations
company: UpTrain
industry: cross-industry
cloud: []
patterns:
- rag
- eval
- llmops
- root-cause-analysis
components:
- UpTrain
- LlamaIndex
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/supercharge-your-llamaindex-rag-pipeline-with-uptrain-evaluations
published_at: '2024-03-19'
---

## 概要

UpTrainのコールバックを数行追加し、RAGの応答品質・取得文脈・中間ステップを自動評価する連携の紹介。失敗の原因分析や設定の比較に使える。

## 設計のポイント

- 最終応答だけでなく中間の取得・再構成ステップも評価対象にする。
- 評価はローカルで実行し、外部送信はLLM呼び出しに限る。
- 評価器LLMを差し替え可能にしてコストと品質を比較する。

## 使いどころ

- RAGを本番化する前に品質を定量評価したいチーム。
- 失敗箇所を特定して改善したい開発者。
