---
type: opinion
title: ポッドキャストを文字起こししてLlamaIndexで要点抽出し、同ツールの構想を整理
title_original: 'LlamaIndex on TWIML AI: a distilled summary using LlamaIndex'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- ai-agent
- context-engineering
components:
- LlamaIndex
- whisper.cpp
- OpenAI Whisper
- Dropbox
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-on-twiml-ai-a-distilled-summary-using-llamaindex-de2a88551595
published_at: '2023-05-10'
---

## 概要

TWIML AIポッドキャスト出演内容をwhisper.cppで文字起こしし、LlamaIndexで要約と質疑を行った記事。top-k検索を超えるルーティングや複数データの合成、エージェント層の構想が語られている。

## 設計のポイント

- 全体要約にはリスト索引、個別の質問にはベクトル索引と、目的で索引を使い分ける。
- 判断の連鎖が増えるほど誤りが伝播しうるため、連鎖の可観測性を考慮する。

## 使いどころ

- 音声コンテンツを文字起こしして要約・QAしたい場面。
- LlamaIndexの設計思想を把握したい読者。
