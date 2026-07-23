---
type: announcement
title: kubeconfigの資格情報プラグインをアローリストで制限する新機能
title_original: 'Kubernetes v1.35: Restricting executables invoked by kubeconfigs via exec plugin allowList added to kuberc'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/01/09/kubernetes-v1-35-kuberc-credential-plugin-allowlist/
published_at: '2026-01-09'
---

## 概要

Kubernetes v1.35では、kubeconfigのexecプラグイン経由で任意の実行ファイルが起動できてしまうリスクに対処するため、kubercの設定にcredentialPluginPolicyとcredentialPluginAllowlistがベータ機能として追加された。AllowAll・DenyAll・Allowlistの3モードで、資格情報取得に使われるコマンドを制御し、サプライチェーン攻撃などで汚染されたkubeconfigによる不正実行を防ぐ。
