---
type: opinion
title: チップから電力網まで見据えたAI推論基盤の効率化戦略
title_original: 'Infrastructure for the frontier era: Scaling intelligence through open industry collaboration'
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- inference-optimization
- cost-optimization
components:
- Azure Maia 300
- Azure Maia 200
- Azure Cobalt 200
- Open Compute Project
outcome:
  type: cost
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://azure.microsoft.com/en-us/blog/infrastructure-for-the-frontier-era-scaling-intelligence-through-open-industry-collaboration/
published_at: '2026-10-13'
---

## 概要

推論が主要負荷になる中で、Maia 300が同世代GPU比で約40%多いトークン/ワット、Cobalt 200がエージェント呼び出し遅延を33%削減するなど、実ワークロードとシリコンを同時設計する方針を述べる。OCPでのオープンな業界協業も強調する。

## 設計のポイント

- モデル・カーネル・通信・システムソフトウェア・シリコンを一つの最適化ループで共同設計する
- エージェント処理で増えるオーケストレーションやメモリ管理向けにCPUも専用設計する

## 使いどころ

- AI基盤の電力効率やトークン単価を重視する事業者
- 自社推論基盤の投資方針を検討する担当者
