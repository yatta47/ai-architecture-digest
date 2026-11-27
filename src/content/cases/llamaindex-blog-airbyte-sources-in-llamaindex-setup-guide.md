---
type: announcement
title: AirbyteのSaaSコネクタをLlamaIndexのローダーとして直接利用
title_original: Introducing Airbyte sources within LlamaIndex
company: Airbyte
industry: cross-industry
cloud: []
patterns:
- rag
components:
- Airbyte
- LlamaIndex
- LlamaHub
- Salesforce
- Stripe
- Zendesk
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-airbyte-sources-within-llamaindex-42209071722f
published_at: '2023-08-29'
---

## 概要

Stripe・Salesforceなど7種のAirbyteソースを、Airbyte本体を立てずにPythonプロセス内でLlamaIndexのローダーとして使えるようになった。

## 設計のポイント

- 試作段階は埋め込み実行で済ませ、スケジュールや監視が必要になったらホスト型へ移せる互換設計にする。
- last_stateを保存して増分同期し、変更分だけでベクトルDBを更新する。
- record_handlerで本文とメタデータを分け、不要な項目が埋め込みに混ざらないようにする。

## 使いどころ

- SaaS上の顧客データをRAGに取り込みたい開発者向け。
- 追加サービスを運用せずにデータ取り込みを試したい場面。
