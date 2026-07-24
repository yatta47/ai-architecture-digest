---
type: announcement
title: MAI-Image-2.5-ProとMAI-Voice-2-Flashを発表
title_original: Introducing MAI-Image-2.5-Pro and MAI-Voice-2-Flash
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- multi-model-routing
- inference-optimization
- voice-agent
components:
- MAI-Image-2.5-Pro
- MAI-Voice-2-Flash
- Bing Image Creator
- PowerPoint
- OneDrive
- Dynamics 365 Contact Center
- Azure Voice Live
- MAI-Transcribe-1.5
- Dragon Copilot
outcome:
  type: cost
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/
published_at: '2026-07-23'
---

## 概要

Microsoft AIが内製モデルの新バリアントMAI-Image-2.5-Pro(高品質画像生成)とMAI-Voice-2-Flash(高速・低コスト音声)をプレビュー公開。Bing Image Creator、PowerPoint、OneDrive、Dynamics 365 Contact Centerなど自社製品に本番投入し、GPUコストを最大89%削減した実績を示す。

## 設計のポイント

- 品質重視・速度/コスト重視など用途に応じた複数バリアントのモデルファミリーを internally 用意し、プロダクトごとに最適な点を選べるようにする
- サードパーティモデルからの蒸留を避け、クリーンで追跡可能なエンタープライズデータで内製学習することでプロダクト統合時の制御性を高める
- 医療分野などはDragon Copilotのような専門パートナーと直接連携し、多言語音声認識のドメイン適合を進める

## 使いどころ

- 画像・音声生成を大規模プロダクトに組み込みつつGPUコストを最適化したいプラットフォームチーム
- コールセンターなど低レイテンシが求められる音声エージェント基盤を構築する場合
