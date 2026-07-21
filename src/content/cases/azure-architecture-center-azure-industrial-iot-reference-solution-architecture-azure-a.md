---
type: guidance
title: OPC UAで世界中の工場ラインをクラウド接続する産業IoTリファレンスアーキテクチャ
title_original: Azure industrial IoT reference solution architecture
ai_relevant: false
industry: manufacturing
cloud:
- azure
patterns: []
components: []
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/iot-industrial-solution-architecture
published_at: '2026-06-23'
---

## 概要

本記事はMicrosoft Learnのソリューションアイデアで、Azure IoT Operations・Event Hubs・Data Explorer・Logic Apps・Arc・Managed Grafanaなどを組み合わせ、世界中の製造拠点をOPC UA標準で単一の産業IoTプラットフォームに接続するリファレンス構成を示す。状態監視やOEE算出、予測、異常検知に加え、しきい値超過時にクラウドから現場のOPC UAサーバーへコマンドを送るデジタルフィードバックループ（圧力リリース制御）のデモも含む。特定企業の実装事例ではなく、クラウドアーキテクトが自社構成を設計する際の出発点として提供される汎用リファレンスアーキテクチャである。
