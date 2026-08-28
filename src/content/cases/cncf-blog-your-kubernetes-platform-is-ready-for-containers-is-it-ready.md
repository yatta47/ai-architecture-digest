---
type: guidance
title: Kubernetesプラットフォームを『AI対応』にするための4つの拡張ポイント
title_original: Your Kubernetes platform is ready for containers. Is it ready for AI?
industry: cross-industry
cloud: []
patterns:
- llmops
- ci-cd
- gpu-fleet-reliability
components:
- Kubernetes
- Dynamic Resource Allocation
outcome:
  type: productivity
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/08/28/your-kubernetes-platform-is-ready-for-containers-is-it-ready-for-ai/
published_at: '2026-08-28'
---

## 概要

CNCFの調査では生成AIモデルをホストする組織の66%がKubernetesを推論基盤に使う一方、日次でモデルをデプロイしている組織はわずか7%にとどまり、AI稼働と運用基盤の間にギャップがあると指摘する。記事は、リソースモデルをGPU/アクセラレータへ拡張し（DRA等）、CI/CDをコード＋モデル＋設定の単位まで広げ、クラスタだけでなくワークロード（推論レイテンシやキュー待ち時間等）を観測し、開発者にモデルからエンドポイントまでのゴールデンパスを提供する、という4つの拡張ポイントを提案する。

## 設計のポイント

- GPU/アクセラレータをCPU・メモリと並ぶ一級のスケジューリング対象とし、Dynamic Resource Allocationなどで宣言的に扱う
- デプロイ単位を「コード→ビルド→デプロイ」から「コード＋モデル＋設定→評価→デプロイ→観測→更新」へ拡張する
- クラスタ視点の指標に加え、アクセラレータ利用率・キュー待ち時間・推論レイテンシ・モデルロード時間を既存の観測基盤に統合する
- モデル・アクセラレータを意識したゴールデンパスを整備し、開発者がKubernetesの専門知識なしにモデルをデプロイできるようにする

## 使いどころ

- コンテナ運用は成熟しているが、AIワークロードの本番運用体制がまだ整っていないプラットフォームチーム
- GPUスケジューリングやモデルのライフサイクル管理を既存のクラウドネイティブプラクティスの延長で整備したい組織
- AI専用の別基盤を作らず、既存のKubernetes基盤にAI運用を統合したい場合
