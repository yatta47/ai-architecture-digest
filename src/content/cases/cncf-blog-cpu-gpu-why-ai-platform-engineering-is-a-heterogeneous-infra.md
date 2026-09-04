---
type: opinion
title: AI基盤はGPUだけでなくCPU/メモリ/ストレージを含むヘテロジニアス問題
title_original: 'CPU + GPU: Why AI Platform Engineering Is a Heterogeneous Infrastructure Problem'
industry: cross-industry
cloud: []
patterns:
- gpu-fleet-reliability
- cost-optimization
components:
- Kubernetes
- Dynamic Resource Allocation (DRA)
outcome:
  type: reliability
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/09/04/cpu-gpu-why-ai-platform-engineering-is-a-heterogeneous-infrastructure-problem/
published_at: '2026-09-04'
---

## 概要

AI基盤はGPU単体の問題ではなく、CPU・GPU・メモリ・ストレージ・ネットワークが連携するヘテロジニアスなワークロードだと捉え、各ステージに必要なリソースを見極めてボトルネックを特定すべきだとする考察。KubernetesのDynamic Resource Allocation(DRA)のような機能が特殊なデバイスもクラウドネイティブなリソースモデルに統合していく方向性を紹介する。

## 設計のポイント

- 「このワークロードにGPUは何台必要か」ではなく「各ステージにどのリソースが必要で、どこに依存関係があるか」を問い、パイプライン全体をシステムとして最適化する
- 推論ですらプロンプト処理とトークン生成で計算・メモリ要件が異なるため、単一の均一なワークロードとして扱わない
- GPU使用率だけでなくCPU→データ→アクセラレータ→アプリケーションという経路全体のテレメトリを相関させ、どのリソースがボトルネックかを可視化する

## 使いどころ

- Kubernetes上でAI学習・推論パイプラインを運用し、GPU追加だけでは解決しないスループット問題を切り分けたいプラットフォームチーム
- GPU使用率が低い原因が需要不足なのか前段の律速なのか判断できず困っている場合
