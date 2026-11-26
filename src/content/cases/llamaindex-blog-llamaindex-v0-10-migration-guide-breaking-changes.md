---
type: announcement
title: コアと連携パッケージを分離したLlamaIndex v0.10の移行解説
title_original: LlamaIndex v0.10
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
components:
- LlamaIndex
- llama-index-core
- LlamaHub
outcome:
  type: reliability
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-v0-10-838e735948f8
published_at: '2024-02-12'
---

## 概要

LlamaIndex v0.10はコアと数百の連携機能を別パッケージに分割し、ServiceContextを非推奨にした。移行スクリプトとレガシー版も提供される。

## 設計のポイント

- コアと外部連携を別パッケージにして、依存とバージョンを個別管理する。
- 何でも入る共通コンテキストをやめ、引数指定か既定値設定にする。

## 使いどころ

- v0.9系からの移行を計画するチーム。
