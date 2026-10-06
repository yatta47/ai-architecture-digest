---
type: guidance
title: kubeletがinode枯渇に動くのは緊急時だけという話
title_original: Kubelet watches inodes, just not until it's an emergency
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/10/05/kubelet-watches-inodes-just-not-until-its-an-emergency/
published_at: '2026-10-05'
---

## 概要

ディスク使用率が低くてもinode枯渇予測のアラートが発報した障害を題材に、kubeletのイメージGCがバイトのみを見ており、inodeはハード退避しきい値（5%）でしか介入しないことを解説する。
