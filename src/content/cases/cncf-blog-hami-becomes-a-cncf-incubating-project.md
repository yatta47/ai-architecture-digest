---
type: announcement
title: GPU仮想化ミドルウェアHAMiがCNCF Incubatingプロジェクトに昇格
title_original: HAMi becomes a CNCF incubating project
industry: cross-industry
cloud:
- on-prem
patterns:
- gpu-fleet-reliability
components:
- HAMi
- Kubernetes
- Volcano
- Koordinator
- Kueue
outcome:
  type: cost
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/07/15/hami-becomes-a-cncf-incubating-project/
published_at: '2026-07-15'
---

## 概要

異機種アクセラレータをKubernetes上で仮想化・分割スケジューリングするオープンソースミドルウェアHAMiが、CNCF Sandboxから2年でIncubatingプロジェクトに昇格した。DaoCloudは1万台超のGPUに、China Merchants Bankは多様なアクセラレータ資源の管理に本番採用している。

## 設計のポイント

- GPU(やNPU/DCU/MLU等)をメモリ・コア・デバイス数単位で分割し、ハードな実行時分離をコンテナ内で強制する。
- ベンダーごとに異なる運用モデルを単一の一貫したインタフェースに統合し、アプリコードやマニフェストを変更せずに済むようにする。
- binpack/spread/topology-awareなど複数のスケジューリングポリシーで配置を最適化し、Prometheus互換の可観測性を提供する。

## 使いどころ

- 高価なGPUの断片化・underutilizationを解消したいAI基盤チーム。
- 単一ベンダーに縛られずマルチベンダーのアクセラレータを横断運用したい大規模データセンター事業者。
