---
type: announcement
title: 学習を止めずにGPUノード群のOSを宣言的に更新するNodeWright
title_original: Manage Kubernetes Node Fleets with NodeWright
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- gpu-fleet-reliability
- policy-as-code
components:
- NodeWright
- Kubernetes
- NVIDIA DSX OS
- NVIDIA AI Cluster Runtime
- NVCRE
- NVSentinel
- Helm
- Argo CD
- Flux
outcome:
  type: reliability
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/manage-kubernetes-node-fleets-with-nodewright/
published_at: '2026-09-23'
---

## 概要

NodeWrightは、GPUクラスタのホストOS設定をKubernetesネイティブに宣言管理・更新するオープンソースのパッケージマネージャー。cordon、待機、drain、適用、必要なら再起動、uncordonの手順を各ノードで踏み、PodDisruptionBudgetや中断不可ラベルを尊重するため、長時間学習を止めずに変更できる。

## 設計のポイント

- 変更の単位をノードでなくフリートとし、固定・線形・指数のバッチ戦略と成功/失敗閾値で段階的にロールアウトする。
- 中断不可ラベルの付いたPodがあればwait段階で待ち、学習ジョブの終了を待ってからノードに触る。
- パッケージをコンテナイメージ＋検証スクリプトで配布し、失敗時はロールアウトを止めてKubernetes上に結果を出す。
- パッケージをカスタムリソースとして定義し、kubectl、Helm、Argo CD、FluxなどのGitOpsに乗せる。

## 使いどころ

- GPUノード群のカーネル設定変更やCVE対応を、稼働中の学習を止めずに全体展開したい運用チーム。
- Ansibleやランブックによる手作業のメンテナンス窓運用を置き換えたいとき。
- NVCRE、NVSentinelと組み合わせて事前検証と実行時監視を含む運用基盤を作りたいとき。
