---
type: case
title: 'Databricks MemCurrent: 本番エージェントの永続メモリ設計'
title_original: 'MemCurrent: Designing persistent memory for production agents'
company: Databricks
industry: cross-industry
cloud:
- multi-cloud
patterns:
- context-engineering
- memory-consolidation
- ai-agent
components:
- Agent Bricks Memory
- Genie
- Lakebase
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/memcurrent-designing-persistent-memory-production-agents
published_at: '2026-10-20'
---

## 概要

MemCurrentは、エージェントが作業中にメモリを読み書きし、オフラインの「ドリーミング」で統合・更新する永続メモリ設計である。社内ベンチマークでメモリ無しに比べ合格率が3倍、トークンは31%減、実行は26%高速になり、Mem0などを上回った。

## 設計のポイント

- 全履歴を渡さず、何を保持し、どう維持し、有用性をどう測るかを設計の中心に置く。
- オンラインの読み書きとオフラインの統合パイプラインを分け、メモリの一貫性と鮮度を保つ。
- 品質とコスト・遅延を同時に改善できるかをパレート面で評価する。

## 使いどころ

- ユーザー嗜好や指標定義、成功手順を継続利用したい業務エージェント。
- 同じ探索を繰り返すことでコストと遅延が膨らむエージェント運用。
