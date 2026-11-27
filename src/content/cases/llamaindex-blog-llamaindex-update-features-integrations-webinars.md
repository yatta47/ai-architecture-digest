---
type: announcement
title: 知識グラフ・引用付き回答・クエリ計画などの初回更新まとめ（2023-06-26）
title_original: LlamaIndex Update 6/26/2023
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- ai-agent
- eval
components:
- LlamaIndex
- NebulaGraph
- Microsoft Guidance
- OpenAI Function API
- TruLens
- OpenBB
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-update-6-26-2023-ed30a9d45f84
published_at: '2023-06-26'
---

## 概要

知識グラフ索引、引用付き回答エンジン、構造化出力、FLARE、MMR、クエリ計画エージェントなどを紹介する更新情報。

## 設計のポイント

- 回答に出典の引用を付けて追跡可能にする。
- MMRで検索結果の重複を減らすが、閾値を調整して無関係な文脈の混入を防ぐ。
- ベクトル検索と知識グラフを併用すると文脈は補えるが、遅延は増える。

## 使いどころ

- 根拠提示が求められるRAGアプリの開発者向け。
- 複数ソースにまたがる質問への対応を強化したい場面。
