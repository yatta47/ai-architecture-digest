---
type: guidance
title: RAG評価でOSSのPrometheusとGPT-4を比較する
title_original: LlamaIndex RAG Evaluation Showdown with GPT-4 vs. Open-Source Prometheus Model
industry: cross-industry
cloud: []
patterns:
- eval
- rag
components:
- LlamaIndex
- Prometheus
- GPT-4
- Hugging Face Inference Endpoints
- Llama Datasets
outcome:
  type: cost
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-rag-evaluation-showdown-with-gpt-4-vs-open-source-prometheus-model-14cdca608277
published_at: '2023-12-15'
---

## 概要

正確性・忠実性・文脈関連性の3指標について、OSSの評価特化モデルPrometheusとGPT-4の評価結果を同じプロンプトで比較した。Prometheusはプロンプト内の採点ルーブリックに依存する点に注意が必要。

## 設計のポイント

- 評価指標ごとに明示的な採点基準をプロンプトに含める。
- 評価モデルを替える際は同一データ・同一プロンプトでスコア分布の差を確認する。
- 正確性の評価には参照回答付きデータを用意する。

## 使いどころ

- RAG評価のGPT-4利用コストを下げたいチーム。
- 自己ホストの評価モデルを検討する場面。
