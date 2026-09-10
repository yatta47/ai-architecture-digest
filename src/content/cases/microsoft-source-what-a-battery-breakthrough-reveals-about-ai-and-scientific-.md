---
type: case
title: Microsoft Discoveryが加速する有機レドックスフロー電池の発見
title_original: Reinventing Organic Redox Flow Batteries with Microsoft Discovery
company: Microsoft
industry: other
cloud:
- azure
patterns:
- rag
- multi-agent-orchestration
- human-in-the-loop
- context-engineering
components:
- Microsoft Discovery Engine
- Discovery Bookshelf
- GraphRAG
outcome:
  type: speed
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://techcommunity.microsoft.com/blog/microsoft-discovery-blog/reinventing-organic-redox-flow-batteries-with-microsoft-discovery/4552343
published_at: '2026-09-09'
---

## 概要

Microsoft Discoveryは、グリッド蓄電で重要鉱物バナジウムへの依存を減らす有機負極液の候補をCLIOモードとGraphRAGベースのDiscovery Bookshelfを用いた閉ループ探索で発見し、Yale大学やPNNLとの協働で実験室検証まで完了した。生成AIによる化合物提案自体はもはやボトルネックではなく、計算予測と実験のスケジューリング、失敗からの学習の蓄積が新たな課題であることを示す。

## 設計のポイント

- 失敗した実験結果もBookshelfに蓄積し、将来の仮説生成に活用する『負の結果を残す』設計にする
- 複数エージェントがナレッジグラフ上で共有理解を持ちながら協調し、局所最適への収束を避けて全体視点を維持する
- 数値化しにくい科学的な要件・選好を言語モデルによって第一級の優先事項として扱えるようにする

## 使いどころ

- きれいな最適化問題として定式化できない、専門家の判断を要する材料探索・創薬などの科学研究
- 計算予測と実験（ウェットラボ）を反復させながら知見を蓄積したいR&D組織
