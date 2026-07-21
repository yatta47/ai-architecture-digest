---
type: case
title: LangSmithでLlama2ファインチューンモデルのSQL生成性能を横並び評価
title_original: Testing Fine Tuned Open Source Models in LangSmith
company: ChatOpenSource
industry: cross-industry
cloud: []
patterns:
- fine-tuning
- eval
- text-to-sql
components:
- Llama2-7b-chat
- Llama2-13b-chat
- LangSmith
- Replicate
- GPT-4
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/testing-fine-tuned-open-source-models-in-langsmith
published_at: '2026-06-16'
---

## 概要

ChatOpenSourceが、Llama2-7b/13bをsql-create-contextデータセットでファインチューンし、LangSmithのデータセット・評価機能を使ってGPT-4によるLLM-as-judgeで正誤を自動採点。パラメータ数とデータ量、応答速度、GPT-3.5-turboとの比較を通じて最適なモデルの組み合わせを検証した。

## 設計のポイント

- 複数のファインチューン済みモデルを同一データセットで横並び評価し、パラメータ数とデータ量のどちらが精度に効くか切り分ける
- LangSmithにデータセットをアップロードし、GPT-4によるLLM-as-judgeで正誤を自動評価する
- 精度だけでなくp50/p99応答時間もあわせて比較し、モデル選定の判断材料にする

## 使いどころ

- 複数のオープンソースモデルを候補として比較検討し、アプリに最適なモデルを選びたい場合
- 特化タスク(SQL生成など)向けにファインチューンしたモデルの性能を定量的に検証したい場合
