---
type: guidance
title: kindでGateway APIをローカル検証するハンズオン環境構築
title_original: Experimenting with Gateway API using kind
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: productivity
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/01/28/experimenting-gateway-api-with-kind/
published_at: '2026-01-28'
---

## 概要

本ガイドは、kind（Kubernetes in Docker）とcloud-provider-kindを用いてGateway APIをローカルで学習・検証する手順を解説する。GatewayとHTTPRouteを作成してデモアプリにトラフィックをルーティングし、curlで動作確認する一連の流れを、本番運用を想定しない実験用セットアップとして紹介している。
