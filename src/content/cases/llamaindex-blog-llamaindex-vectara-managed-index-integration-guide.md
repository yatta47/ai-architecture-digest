---
type: announcement
title: 取り込みから検索まで委ねるManaged Index：VectaraとLlamaIndexの統合
title_original: LlamaIndex + Vectara
company: Vectara
industry: cross-industry
cloud: []
patterns:
- rag
components:
- Vectara
- LlamaIndex
- VectaraIndex
- Managed Index
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-vectara-7a3889cd34cb
published_at: '2023-09-12'
---

## 概要

分割・埋め込み・保存・検索をVectara側で一括管理するManagedIndexをLlamaIndexに追加した告知。取り込みは1回のAPI呼び出しで済む。

## 設計のポイント

- 取り込みと索引化をマネージドサービスに委ね、アプリ側はクエリ構成に集中する。
- 抽象を揃えることで、自前のVectorStoreIndexと同じクエリ部品を再利用できる。
- ハイブリッド検索と再ランキングを標準機能として使う。

## 使いどころ

- ベクトルDBやMLOpsを自前運用せずにRAGを本番化したいチーム向け。
- 顧客管理鍵などの暗号化要件がある文書検索。
