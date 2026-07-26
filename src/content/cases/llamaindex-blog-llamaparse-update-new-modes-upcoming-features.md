---
type: announcement
title: Fast/Balanced/Premiumに再編し、LLM・LVM・エージェント解析を選べるLlamaParseの機能刷新
title_original: 'LlamaParse Update: New and Upcoming Features'
industry: cross-industry
cloud: []
patterns:
- document-processing
components:
- LlamaParse
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaparse-update-new-and-upcoming-features
published_at: '2026-07-19'
---

## 概要

文書解析サービスLlamaParseが解析モードをFast/Balanced/Premiumの3段階に整理し直し、AIなし解析・LLM解析・LVM(大規模視覚モデル)解析・エージェント解析という4つの内部手法を選べるようにアップデート。複数の外部LVMベンダーへの対応や、独自モデルAPIキーの持ち込みにも対応する。

## 設計のポイント

- コスト・速度・精度のトレードオフに応じてFast/Balanced/Premiumの3モードに整理し、内部では用途別に4つの解析手法（無AI・LLM・LVM・エージェント）を使い分ける
- ページ単位ではなく文書全体を俯瞰して解析する『継続モード』を導入し、ページをまたぐ表や見出し階層の一貫性を保つ
- OpenAI・Azure・Anthropic・Googleなど複数の外部LVMベンダーに対応し、ユーザー自身のAPIキー持ち込みも許可している

## 使いどころ

- 大量文書の解析コストと精度のバランスを用途に応じて調整したい開発者
- 表が複数ページにまたがる長大なPDFなど、ページ単位の解析では崩れる文書構造を正確に復元したいケース
