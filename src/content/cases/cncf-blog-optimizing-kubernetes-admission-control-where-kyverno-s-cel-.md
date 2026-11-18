---
type: case
title: Kyverno CEL管理コントロールのコスト要因を特定し、ポリシー数に比例する変換処理を解消
title_original: 'Optimizing Kubernetes admission control: where Kyverno''s CEL admission cost actually goes'
ai_relevant: false
company: Nirmata
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: speed
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/11/18/optimizing-kubernetes-admission-control-where-kyvernos-cel-admission-cost-actually-goes/
published_at: '2026-11-18'
---

## 概要

KyvernoのCELエンジンをプロファイルした結果、割り当てバイトの約86%がポリシー評価ではなくオブジェクトのunstructured変換に使われていた。変換がマッチしたポリシーごとのループ内で繰り返されていたため、ループ外へ移す修正をKyverno 1.19.2で提供した。
