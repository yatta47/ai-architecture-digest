---
type: announcement
title: 読み書き両方をこなすData Agentsの提供開始
title_original: Data Agents
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- ai-agent
- rag
components:
- LlamaIndex
- LlamaHub
- OpenAI Function API
- ReAct
- Gmail
- OpenAPI
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/data-agents-eed797d7972f
published_at: '2023-07-12'
---

## 概要

データの検索だけでなく外部APIで状態を変更できるData Agentsの発表。推論ループとツール抽象を中核に、15以上のツールを提供する。

## 設計のポイント

- エージェントを推論ループとツール定義に分離する。
- 関数呼び出し対応モデルにはその機能を使い、他のモデルにはReActプロンプトで対応する。
- 状態を持つchatと持たないqueryを使い分ける。

## 使いどころ

- 検索を超えてメール送信や予定作成まで自動化したい開発者向け。
- 複数のデータ源をまたぐ業務支援エージェントの構築。
