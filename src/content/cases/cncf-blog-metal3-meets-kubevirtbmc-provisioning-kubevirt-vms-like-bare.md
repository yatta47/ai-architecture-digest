---
type: guidance
title: Metal3とKubeVirtBMCによるKubeVirt VMのベアメタル風プロビジョニング
title_original: 'Metal3 Meets KubeVirtBMC: Provisioning KubeVirt VMs Like Bare Metal'
ai_relevant: false
industry: cross-industry
cloud:
- on-prem
patterns: []
components: []
outcome:
  type: productivity
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/09/02/metal3-meets-kubevirtbmc-provisioning-kubevirt-vms-like-bare-metal/
published_at: '2026-09-02'
---

## 概要

CNCFのMetal3とKubeVirtBMCを組み合わせ、KubeVirt上のVMに仮想BMCエンドポイントを持たせることで、物理ベアメタルサーバーと同じ手順でVMをプロビジョニングできるエンドツーエンドのデモを紹介する記事。Ironic経由のRedfishリクエストをBMC podがKubernetes API呼び出しへ変換することで、Metal3はVMを物理サーバーと区別せずBareMetalHostとして管理できる。
