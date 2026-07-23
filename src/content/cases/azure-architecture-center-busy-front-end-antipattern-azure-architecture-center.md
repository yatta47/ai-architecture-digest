---
type: guidance
title: 重い処理でフロントエンドが圧迫されるBusy Front Endアンチパターンと解決策
title_original: Busy Front End antipattern
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/antipatterns/busy-front-end/
published_at: '2026-02-03'
---

## 概要

リクエスト処理層と重い処理が同居するモノリシックな構成では、バックグラウンドスレッドに処理を逃がしても共有リソースを消費し続け、他のリクエストのレイテンシが悪化するBusy Front Endアンチパターンを解説している。解決策として、重い処理をメッセージキュー(Service Busなど)経由で別バックエンドに渡し、非同期かつオートスケール可能な形で処理するキューベースの負荷平準化を提案している。あわせてスロットリングや優先度別キューとの組み合わせ、監視によるボトルネック特定手順も示す。
