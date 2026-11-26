---
type: case
title: 自然言語でECのDBに質問し分析まで返すNa2SQLアプリ
title_original: Transforming Natural Language to SQL and Insights for E-commerce with LlamaIndex, GPT3.5, and Streamlit
industry: retail
cloud: []
patterns:
- text-to-sql
components:
- LlamaIndex
- SQLTableQueryEngine
- GPT-3.5
- Streamlit
- SQLite
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/transforming-natural-language-to-sql-and-insights-for-e-commerce-with-llamaindex-gpt3-5-e08edefa21f9
published_at: '2023-12-17'
---

## 概要

SQLを知らない利用者が平易な言葉でECデータベースに質問できるデモアプリを構築した個人プロジェクト。SQLの生成・実行に加え、質問と実行結果を踏まえた分析文もLLMが返す。

## 設計のポイント

- SQL生成と実行結果の解釈をひと続きの流れにして、利用者には洞察まで返す。
- スキーマを確認できるDBビューアを併設し、質問の組み立てを助ける。
- 本番で使う場合はDB権限を読み取り専用に絞る。

## 使いどころ

- 非エンジニアのセルフサービス分析を試したいチーム。
- text-to-SQLの最小構成を学びたい開発者。
