---
type: case
title: 年次報告書(10-K)を読み解くRAGアプリ「FinSight」の構築
title_original: How I built the Streamlit LLM Hackathon winning app — FinSight using LlamaIndex
industry: financial-services
cloud: []
patterns:
- rag
- document-processing
components:
- LlamaIndex
- Streamlit
- FAISS
- GPT-4
- SubQuestionQueryEngine
- AlphaVantage
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/how-i-built-the-streamlit-llm-hackathon-winning-app-finsight-using-llamaindex-9dcf6c46d7a0
published_at: '2023-10-17'
---

## 概要

企業の年次報告書から洞察を抽出するハッカソン優勝アプリの構築記録。PDFをFAISSに索引化し、複雑な質問は下位質問に分解して回答する。

## 設計のポイント

- 小規模で一時的な索引にはインメモリのFAISSを使い、構成を軽く保つ。
- 広い問いは単純なtop-k検索では浅くなるため、SubQuestionQueryEngineで下位質問に分解して複数箇所から文脈を集める。
- クエリエンジンをツールとして名前と説明付きで包み、対象が増えてもLLMが使い分けられるようにする。

## 使いどころ

- 決算資料の読み込みと比較を効率化したい金融アナリスト向け。
- 長文PDFに対する要約・質問応答を短期間で試作したい開発者向け。
