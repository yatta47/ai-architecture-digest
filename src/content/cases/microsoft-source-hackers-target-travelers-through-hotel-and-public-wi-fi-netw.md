---
type: case
title: ロシア系国家ハッカー集団によるホテル/公衆Wi-Fi経由の出張者標的攻撃キャンペーン「CaptiveCrunch」
title_original: 'CaptiveCrunch: Midnight Blizzard Targets Travelers Worldwide for Malware Delivery and Credential Theft'
ai_relevant: false
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/
published_at: '2026-08-03'
---

## 概要

Microsoft Threat Intelligenceは、ロシア対外情報庁(SVR)系のMidnight Blizzardのサブクラスターである Storm-2945 が、2026年5月以降、ホテルや会議施設などのキャプティブポータル経由のWi-Fiネットワークで大規模なDNS/HTTPトラフィック改ざんを行っていると報告した。攻撃者はこの中間者(AiTM)的な立場を悪用し、Microsoft Entra IDのデバイスコード認証フローを狙ったフィッシングや、ブラウザ/OS更新を装うClickFix手口でWindows向けRAT「CornFlake」やAndroid向けAPKを配布し、出張中の企業アカウントの侵害を狙っている。この一連の作戦の一部でStorm-2945がAIを活用していたことも確認されている。
