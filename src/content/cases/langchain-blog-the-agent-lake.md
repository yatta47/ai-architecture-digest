---
type: opinion
title: エージェントのトレースと成果を集約し改善ループを回す『Agent Lake』構想
title_original: The Agent Lake
company: LangChain
industry: cross-industry
cloud: []
patterns:
- llmops
- eval
- ai-agent
components:
- LangSmith
- SmithDB
- AI Search
- Insights
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/the-agent-lake
published_at: '2026-11-25'
---

## 概要

エージェントのトレースと成果データを専用ストレージに蓄積し、その上で知的な計算処理を走らせて継続改善する『Agent Lake』という基盤像を提唱する記事。LangSmithではSmithDBを土台に、オンライン評価や自然言語検索などを重ねている。

## 設計のポイント

- トレースだけでなく成果（ユーザー評価・マージされたPR・LLM判定など）を紐づけて保存し、ROIと改善を判断できるようにする。
- 大量トレースは人手で読まず、オンライン評価や意味検索で重要なものを抽出する。
- オンライン評価のコストは安価な判定モデルで抑える。

## 使いどころ

- 本番エージェントのトレース量が増え、手動デバッグが追いつかなくなったチーム。
- エージェント改善サイクルのデータ基盤を設計するアーキテクト。
