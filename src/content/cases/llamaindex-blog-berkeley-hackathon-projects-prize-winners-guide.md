---
type: case
title: ハッカソン発の知識活用アプリ：市場情報フィードや文体を学ぶメール生成
title_original: 'Special Feature: Berkeley Hackathon Projects (LlamaIndex Prize Winners)'
industry: cross-industry
cloud:
- azure
patterns:
- rag
- ai-agent
components:
- LlamaIndex
- LangChain
- Pinecone
- OpenAI GPT
- Azure App Services
- Hume
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/special-feature-berkeley-hackathon-projects-llamaindex-prize-winners-c135681bb6f0
published_at: '2023-06-30'
---

## 概要

Berkeleyハッカソンの受賞作紹介。ニュースを取り込み洞察をフィード表示するHelmet AIや、過去メールから本人の文体で下書きするSplitなどを掲載する。

## 設計のポイント

- RSSを購読して継続的に取り込み、埋め込みをベクトルDBに蓄える。
- 洞察のフィードと、個別記事を深掘りするチャットを併設する。
- 過去メールに感情タグを付け、宛先や話題と結び付けて文体を再現する。

## 使いどころ

- 独自データを使うLLMアプリの題材を探す開発者向け。
- 市場動向の把握やメール作成の効率化を試したい場面。
