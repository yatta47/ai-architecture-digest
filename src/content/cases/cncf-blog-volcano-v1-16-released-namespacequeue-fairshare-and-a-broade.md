---
type: announcement
title: 'Volcano v1.16: 名前空間キューとfairshareでAI基盤のスケジューリングを改善'
title_original: 'Volcano v1.16 released: NamespaceQueue, fairshare, and a broader HyperNode ecosystem'
company: Volcano
industry: cross-industry
cloud:
- on-prem
patterns:
- gpu-fleet-reliability
- cost-optimization
components:
- Volcano
- Kubernetes
- HyperNode
outcome:
  type: reliability
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/10/28/volcano-v1-16-released-namespacequeue-fairshare-and-a-broader-hypernode-ecosystem/
published_at: '2026-10-28'
---

## 概要

Volcano v1.16.0は、名前空間内で階層キューを管理するNamespaceQueueと、過去の使用量を考慮するfairshareプラグインを追加した。HyperNodeを他のスケジューラーでも使えるようにし、スケジュール不能ジョブのキャッシュで性能も改善した。

## 設計のポイント

- テナントが名前空間内で階層キューとクォータを管理でき、管理者承認済みのリソースプールの範囲で共有できる。
- fairshareが過去の消費量を判断に入れ、共有キュー内のチーム間の公平性を高める。
- PodGroupのトポロジアンチアフィニティで推論インスタンスをスーパーノードに分散し、障害ドメインの偏りを減らす。

## 使いどころ

- 複数チームでGPUクラスタを共有するAI/MLの基盤運用。
- 大規模な待ちジョブを抱えるバッチスケジューリング環境。
