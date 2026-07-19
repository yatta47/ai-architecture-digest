---
type: announcement
title: 'Aurora 1.5: 気象・地球システム基盤モデルの拡張と確率的アンサンブル予報'
title_original: Aurora 1.5 Makes Weather Forecasts Smarter
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- fine-tuning
- eval
- foundation-model
components:
- Aurora 1.5
- Microsoft Weather
- Hugging Face
- GitHub
outcome:
  type: quality
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://www.microsoft.com/en-us/research/blog/aurora-1-5-extending-open-foundation-models-for-weather-and-earth-system-applications/
published_at: '2026-07-10'
---

## 概要

Microsoft ResearchのEarth系基盤モデルAuroraを拡張したAurora 1.5が公開され、22種の新しい気象変数、1時間単位の時間解像度、確率的アンサンブル予報に対応した。多段階のファインチューニングで潜在空間に確率的摂動を導入してアンサンブル化した結果、ECMWFのアンサンブル予報(ENS)を評価対象の88.9%で上回り、台風・ハリケーンの進路誤差も従来モデル比で約3分の1に削減した。モデル本体はGitHub/Hugging Faceでオープンソース公開され、Microsoft Weatherが企業向けのデータ・インフラ・マネージドアクセスを提供する。

## 設計のポイント

- 変数拡張→時間解像度向上→潜在空間への確率的摂動導入→ECMWF HRESデータでの自己回帰ファインチューニングという多段階の手順でアンサンブル予報能力を段階的に獲得する
- 単一の基盤モデルを気象・海洋波・大気化学など複数のEarth系タスクに適応させる設計により、用途ごとの専用モデル開発コストを削減する
- オープンソースのモデル本体と、企業向けデータ・インフラ・運用保証を提供するマネージドサービス(Microsoft Weather)を分離し、研究成果を実運用へ橋渡しする

## 使いどころ

- 電力・農業・輸送・気候リスクなど、予報の不確実性(確率分布)が意思決定に直結する業種
- 台風・ハリケーンなど進路予測の精度向上が求められる防災・気象業務
- オープンな基盤モデルを評価・拡張したい研究者やモデル開発者
- 自社データ・運用体制と組み合わせた企業向け気象インテリジェンスを構築したい組織
