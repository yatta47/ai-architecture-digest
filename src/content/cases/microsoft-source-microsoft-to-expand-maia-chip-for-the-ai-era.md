---
type: announcement
title: Microsoft、Maia 200を本番稼働しMaia 300をマルチギガワット展開へ
title_original: Azure Maia 200 now in production; Azure Maia 300 coming in 2027
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- inference-optimization
- cost-optimization
- gpu-fleet-reliability
components:
- Azure Maia 200
- Azure Maia 300
- Microsoft Copilot
- GitHub Copilot
- Microsoft Foundry
- HBM4
outcome:
  type: cost
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://blogs.microsoft.com/blog/2026/10/12/microsoft-to-expand-azure-maia-system-to-multi-gigawatt-deployments/
published_at: '2026-10-12'
---

## 概要

MicrosoftはMaia 200がCopilotなどの本番ワークロードを処理中であり、2027年からMaia 300をマルチギガワット規模で展開してMicrosoft製品の主要な推論基盤にすると発表した。Maia 300は推論優先の設計で、主要GPUシステムと比べ1メガワット当たりのトークン数が40%多いとされる。

## 設計のポイント

- データ移動を最小化するソフトウェア定義のデータフローと、HBM帯域・SRAMスクラッチパッドを重視した推論優先の設計。
- MXFP4などの低精度形式でKV-cacheと帯域の要件を下げ、同じ電力で長いコンテキストを扱う。
- 計算・メモリ制御・I/Oを分けたチップレット構成と、Ethernetベースのスケールアップ網で96アクセラレータのラックを構成する。

## 使いどころ

- 長文脈推論やマルチステップのエージェント処理を大規模に提供する事業者の基盤戦略を把握したいとき。
- GPU以外の推論基盤との電力当たり性能の比較を検討する場面。
