---
type: announcement
title: Data AgentsとLlamaIndex.TS、ベンチマーク対応の月次更新（2023-08-01）
title_original: LlamaIndex Update 08/01/2023
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- ai-agent
- rag
- eval
components:
- LlamaIndex
- LlamaIndex.TS
- Llama 2
- Claude 2
- BEIR
- Chroma
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-update-08-01-2023-185514d9b897
published_at: '2023-08-01'
---

## 概要

Data Agents、TypeScript版、Zapier NLA連携、BEIRやHotpotQAのベンチマーク対応などをまとめた更新情報。

## 設計のポイント

- 対話型エージェントは毎回の発話で文脈検索を挟み、幻覚を抑える。
- 引数の多いAPIは自然言語1引数の形に単純化し、エージェントをツール選択に集中させる。
- 検索や多段推論は公開ベンチマークで評価する。

## 使いどころ

- LlamaIndexの機能動向を追いたい開発者向け。
- ベクトルDBやモデルの選定材料を集めたいチーム向け。
