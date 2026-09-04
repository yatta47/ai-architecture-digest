---
type: opinion
title: AI需要で再び難しくなるKubernetes導入
title_original: Kubernetes isn't new, but AI makes it scary again
industry: cross-industry
cloud:
- multi-cloud
patterns:
- gpu-fleet-reliability
components:
- Kubernetes
- GKE
- AKS
- EKS
outcome:
  type: reliability
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/09/04/kubernetes-isnt-new-but-ai-makes-it-scary-again/
published_at: '2026-09-04'
---

## 概要

AIワークロードの本番投入によってKubernetes導入のハードルが再び上がっているという指摘。GPU予算の逼迫・他アプリケーションへの影響・セキュリティ低下を避けるにはジョブ配置の管理やガードレールの整備が必要であり、本番運用前に実環境での挙動を確認できる試験的な環境が有効だとする考察。

## 設計のポイント

- GPUバーストを伴う学習・自動復旧が必要な推論・一貫した制御プレーンが必要なデータパイプラインという異なる要件を同じKubernetesクラスタ上で管理する必要がある
- クラスタを立てること自体は容易になった一方、GPU予算を守りつつ他アプリを飢餓状態にせずセキュリティを保つジョブ配置とガードレールの運用が本当の難所である
- 本格導入前に実インフラ上での挙動を確認できる試験的な環境を用意し、リスクを取る前に検証する

## 使いどころ

- はじめてAIワークロードをKubernetesに載せる、あるいは既存K8s運用チームがAI特有の要件(GPUバースト・推論スケーリング)に対応したい場合
- GPU予算超過や他アプリへの影響を避けつつ本番AI基盤の運用ガバナンスを整備したい場合
