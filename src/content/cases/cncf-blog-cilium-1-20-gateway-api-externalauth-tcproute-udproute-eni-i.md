---
type: announcement
title: 'Cilium 1.20リリース: Gateway API拡張とeBPFデータパスプラグイン'
title_original: 'Cilium 1.20: Gateway API ExternalAuth, TCPRoute/UDPRoute, ENI IPAM for IPv6 and more'
ai_relevant: false
industry: cross-industry
cloud:
- multi-cloud
patterns: []
components: []
outcome:
  type: reliability
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/09/14/cilium-1-20-gateway-api-externalauth-tcproute-udproute-eni-ipam-for-ipv6-and-more/
published_at: '2026-09-14'
---

## 概要

CNCFのネットワーキングプロジェクトCiliumがバージョン1.20をリリースした。Gateway APIをv1.6へ引き上げてExternalAuthやTCPRoute/UDPRouteなど非HTTPトラフィックにも対応させたほか、AWS ENI IPAMのIPv6対応、カーネルに応じて自動でnetkit/vethを切り替えるデータパスモード、サードパーティがeBPFデータパスを拡張できるデータパスプラグイン機構を追加した。
