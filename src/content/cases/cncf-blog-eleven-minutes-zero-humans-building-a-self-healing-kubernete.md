---
type: case
title: KairosとGitOpsで実現した無人・11分完了のKubernetesコントロールプレーンアップグレード
title_original: 'Eleven minutes, zero humans: building a self-healing Kubernetes upgrade pipeline on Kairos'
ai_relevant: false
industry: other
cloud:
- on-prem
patterns: []
components: []
outcome:
  type: reliability
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/08/14/eleven-minutes-zero-humans-building-a-self-healing-kubernetes-upgrade-pipeline-on-kairos/
published_at: '2026-08-14'
---

## 概要

OpenTofuでブートストラップしたK3s HAクラスタを、A/Bパーティション方式でOSイメージを丸ごと入れ替えるKairos Hadronと、Renovate・Kyverno・Cosign・ArgoCD・kairos-operatorを組み合わせたGitOpsパイプラインで無人アップグレードする事例。実運用では3ノード同時再起動を招く並行度設定ミスや、カスタムバージョン変換テンプレートの設定漏れによる「見た目は動いたが実は何も更新されていない」バグを経て、人手を介さず11分・etcdクォーラム維持でのアップグレードを達成した。
