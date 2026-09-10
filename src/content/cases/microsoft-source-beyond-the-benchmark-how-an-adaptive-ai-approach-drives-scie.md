---
type: case
title: Microsoft Discovery CLIOによる適応的な科学的推論
title_original: 'Beyond the benchmark: How an adaptive approach drives scientific discovery'
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- multi-agent-orchestration
- eval
- human-in-the-loop
- reasoning-computation-separation
components:
- Microsoft Discovery Engine
- CLIO
outcome:
  type: quality
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://azure.microsoft.com/en-us/blog/beyond-the-benchmark-how-an-adaptive-approach-drives-scientific-discovery/
published_at: '2026-09-09'
---

## 概要

Microsoft DiscoveryのCLIO（Cognitive Loop via In-Situ Optimization）は、長時間・ツール利用型の専門タスクを評価するベンチマークAgent's Last Examで、健康医療61.6%・物理科学75.2%・生命科学64.6%と他のエージェントハーネスを上回るスコアを達成した。CLIOは複数の独立した推論経路を探索・比較し、最も有力な経路を証拠付きで単一の結論に収束させ、必要に応じて戦略転換や人間専門家の介入を判断する。

## 設計のポイント

- 単一の明確なワークフローが存在しない問題に対し、複数の推論経路を並行して探索し比較検討する
- 証拠を保存しながら推論過程を追跡可能にし、結論に至った経緯と人間の判断を挟むべき箇所を明示する
- 探索の継続・戦略変更・モデル切り替え・専門家投入のいずれを取るかをシステム自身が判断する

## 使いどころ

- 答えが定まっていない材料科学・創薬などの研究開発領域でのエージェント活用
- ベンチマークスコアだけでなく、根拠と過程の説明責任が求められる専門的タスク
