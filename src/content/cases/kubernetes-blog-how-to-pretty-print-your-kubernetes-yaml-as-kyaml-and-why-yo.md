---
type: guidance
title: 型を明示するYAML方言KYAMLでKubernetesマニフェストのバグを防ぐ
title_original: How to Pretty-Print Your Kubernetes YAML as KYAML and Why You'd Want To
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: quality
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/08/11/how-to-pretty-print-kubernetes-yaml-as-kyaml/
published_at: '2026-08-11'
---

## 概要

Kubernetes SIG CLIは、YAMLの厳密なサブセットであるKYAMLを導入した。文字列を常にクォートし、マップは{}、リストは[]で明示することで『ノルウェー問題』のような暗黙の型変換やインデント依存のバグを防ぎつつ、既存のkubectlやYAMLパーサをそのまま使える互換性を保つ。
