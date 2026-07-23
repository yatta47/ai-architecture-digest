---
type: guidance
title: clientcmdライブラリでkubectl風CLIクライアントを作る方法
title_original: Uniform API server access using clientcmd
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: productivity
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/01/19/clientcmd-apiserver-access/
published_at: '2026-01-19'
---

## 概要

Kubernetesプロジェクトが提供するclientcmdライブラリを使うと、kubectl互換のコマンドライン引数（kubeconfig選択、コンテキストや名前空間の切り替え、認証情報など）を独自のGo製CLIやkubectlプラグインに簡単に組み込める。記事はローディングルールの設定、オーバーライドとフラグの定義・バインド、設定のマージ、APIクライアントの取得までの手順を解説している。
