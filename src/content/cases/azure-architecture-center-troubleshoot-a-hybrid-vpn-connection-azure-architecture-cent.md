---
type: guidance
title: Azure ハイブリッドVPN接続のトラブルシューティング手順
title_original: Troubleshoot a hybrid VPN connection
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/hybrid-networking/troubleshoot-vpn
published_at: '2025-12-09'
---

## 概要

オンプレミス環境とAzure間のハイブリッドVPN接続で問題が発生した際の切り分け手順をまとめたリファレンスです。Windows Server上のRRASのイベントログ確認やPsPingによる接続性・経路の検証など、オンプレミス側VPNアプライアンスが正常に機能しているかを確認する具体的な方法を示しています。また、ポリシーベース(AES256/AES128/3DES)とルートベース(AES256/3DES)のゲートウェイで対応する暗号化方式が異なる点など、Azure VPN Gatewayとの互換性確認のポイントにも触れています。
