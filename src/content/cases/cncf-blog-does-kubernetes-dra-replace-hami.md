---
type: guidance
title: Kubernetesのネイティブリソース割り当て(DRA)は分割GPU共有ツールHAMiを置き換えるか
title_original: Does Kubernetes DRA replace HAMi?
industry: cross-industry
cloud: []
patterns:
- gpu-resource-scheduling
- cost-optimization
- inference-optimization
components:
- Kubernetes
- HAMi
- Dynamic Resource Allocation (DRA)
- NVIDIA GPU
outcome:
  type: cost
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/08/07/does-kubernetes-dra-replace-hami/
published_at: '2026-08-07'
---

## 概要

Kubernetesの標準リソースAPIは整数個のデバイスしか数えられなかったため、HAMiはミューテーティングWebhookとスケジューラ拡張、独自アノテーションを使ってGPUメモリやコア単位の分割共有を実現してきた。Kubernetes v1.34でGA、v1.35でデフォルト有効化されたDynamic Resource Allocation(DRA)のconsumable capacity機能により、この「どのカードにどれだけ」という決定をネイティブAPIのClaimオブジェクトとして表現できるようになったが、コンテナ内でのCUDA呼び出し単位の強制はDRAの範囲外であり、HAMiは強制部分を残しつつエンコーディング部分をDRA上に再構築する方向に移行している。

## 設計のポイント

- リソース記述をアノテーション文字列ではなくAPIファーストなResourceClaimオブジェクトに移し、RBACや他のコントローラから扱えるようにする
- スケジューリング（どのカードにどれだけ割り当てるか）と、コンテナ内での実際の使用量強制を別レイヤーの責務として分離する
- 上流APIの表現力が追いつくまではWebhook＋スケジューラ拡張＋独自アノテーションで機能を先取り実装し、標準化後にエンコーディング部分だけ移行する

## 使いどころ

- GPUを分割してマルチテナントで共有し、コスト効率を上げたいML/AI基盤チーム
- HAMiなどフラクショナルGPUプロジェクトを運用しており、DRAへの移行方針を検討しているプラットフォームエンジニア
- Kubernetes上でGPUメモリ超過による過剰プロビジョニングを防ぎたい運用者
