---
type: case
title: コンパイル済みWikiと証拠グラフでエージェント記憶を作る
title_original: Building Evidence-Grounded Agent Memory with OpenWiki and Graphs
company: LangChain
industry: financial-services
cloud: []
patterns:
- rag
- memory-consolidation
- context-engineering
- eval
components:
- OpenWiki
- Deep Agents
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/building-agent-memory-openwiki-graphs
published_at: '2026-10-28'
---

## 概要

複数ソースにまたがる質問で、OpenWikiでコンパイルしたWikiを記憶層にしたエージェントは検索のみの場合の約5倍の精度だった。引用や参照をグラフの辺にした証拠グラフを足すと、さらに精度が27%上がり、正解あたりのコストが58%下がった。

## 設計のポイント

- ソースを要約・相互リンクしたWikiを作り、チャンク検索では再構成が必要な関係を保持する。
- Wikiの記述から根拠となる原文へたどれる証拠グラフを持たせ、引用の一貫性を高める。
- 単純な検索質問では記憶なしでも同等の精度で速いため、複数ソース横断の推論に絞って使う。

## 使いどころ

- 銀行や保険のように規程が改定・上書きされ合ううえで横断的な回答が要る分野。
- コードベースの構造を毎回調べ直させたくないコーディングエージェント。
