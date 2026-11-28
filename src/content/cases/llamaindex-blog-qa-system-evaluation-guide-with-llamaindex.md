---
type: guidance
title: 質問生成とラベル不要評価によるRAG QAシステムの評価手順
title_original: Building and Evaluating a QA System with LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- eval
components:
- LlamaIndex
- gpt-3.5-turbo
- GPT-4
- Google Colab
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/building-and-evaluating-a-qa-system-with-llamaindex-3f02e9d87ce1
published_at: '2023-05-07'
---

## 概要

LlamaIndexでQAシステムを作り、文書から自動生成した質問とLLMによる判定で品質を評価する手順の解説。正解ラベルなしで、回答が根拠文脈や質問に沿っているかを確認する。

## 設計のポイント

- 文書からLLMで評価用の質問を生成し、正解データなしで評価を始める。
- 回答と根拠の一致（幻覚検出）と、質問を含めた妥当性を別々に判定する。
- 根拠ノードを個別に評価し、回答に寄与した出典を特定する。

## 使いどころ

- RAGを本番に出す前に品質を測りたいチーム。
- 出典提示のために有効な根拠を絞りたい場面。
