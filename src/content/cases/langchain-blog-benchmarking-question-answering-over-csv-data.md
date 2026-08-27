---
type: case
title: 実ユーザーの質問ログとLLM評価でCSVデータQ&Aエージェントを改善した事例
title_original: Benchmarking Question/Answering Over CSV Data
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- eval
- rag
components:
- LangSmith
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/benchmarking-question-answering-over-csv-data
published_at: '2026-08-26'
---

## 概要

LangChainはCSV（表形式データ）への自然言語Q&Aを改善するため、まずTitanicデータセットを使ったStreamlitアプリを公開して実際のユーザー質問とフィードバックを収集し、LangSmithで低評価のやり取りを抽出してラベル付けした評価データセットを作った。最終的にPython REPLとリトリーバーの2つのツールを持つOpenAI Functionsベースのカスタムエージェントに落ち着き、LLMによる評価で改善を検証した。

## 設計のポイント

- 本番投入前に実アプリを公開して実際のユーザー質問とフィードバックを収集し、推測ではなく実データに基づいて改善対象を決めた
- OpenAI Functionsを使うカスタムエージェントにPython REPLとリトリーバーの2つのツールを持たせ、数値集計とあいまいなテキスト照合（人名の表記ゆれなど）の両方に対応させた
- LangSmithで低評価だったやり取りを収集・修正し、評価用データセットとして蓄積した
- 自然言語出力の評価にBLEU/ROUGEではなくLLMによる評価（LLM-as-judge）を採用した

## 使いどころ

- 表形式データ（CSV/SQL）に対する自然言語Q&Aシステムを構築したいチーム
- LLMアプリの評価データセットをどう作るか悩んでいる開発者
- 数値集計とあいまい検索が混在するデータに対するエージェント設計の参考
