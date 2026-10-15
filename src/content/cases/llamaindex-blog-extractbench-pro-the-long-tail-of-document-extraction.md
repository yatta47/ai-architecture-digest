---
type: announcement
title: 長尾の文書抽出を測るベンチマークExtractBench Pro
title_original: 'Introducing ExtractBench Pro: the long tail of document extraction'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- eval
- ai-agent
components:
- ExtractBench Pro
- LlamaExtract
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-extractbench-pro
published_at: '2026-10-15'
---

## 概要

LlamaIndexは文書抽出ベンチマークの拡張版ExtractBench Proを公開した。実顧客の難しい文書から6種の課題（ECG、フローチャート、地図、家系図など）を合成し、固定的なパイプラインは苦戦し、適切なツールを持つエージェント型が適応できると述べる。

## 設計のポイント

- 決定的パイプラインで正解付きの難文書を合成する
- 図表内のみに現れる値や、ページ間で意味が変わるルールを評価する

## 使いどころ

- 図表を多く含む文書抽出の精度を評価したい開発者
