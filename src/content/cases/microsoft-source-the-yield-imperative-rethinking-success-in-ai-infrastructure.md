---
type: opinion
title: 『有用な歩留まり』で測るAIインフラの次のフェーズ
title_original: 'The yield imperative: Rethinking success in AI infrastructure'
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- gpu-fleet-reliability
- inference-optimization
- cost-optimization
components:
- Azure Maia
- Azure Cobalt
outcome:
  type: cost
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://news.microsoft.com/source/asia/2026/09/02/the-new-imperative-for-ai-infrastructure-useful-yield/
published_at: '2026-09-02'
---

## 概要

MicrosoftのAzureハードウェア責任者が、AIインフラの進歩を『どれだけ容量を構築したか』ではなく『その資源をどれだけ効率的に有用な知能へ変換できたか（ユースフル・イールド）』で測るべきだと訴えたSEMICON Taiwan基調講演の内容。メモリ・ネットワーキング・電力を横断してシリコンからシステムまで一貫して最適化するクロスレイヤー設計を次の効率フロンティアと位置づける。

## 設計のポイント

- 単一レイヤーの最適化ではなく、シリコン・メモリ・ネットワーク・電力・ソフトウェア・モデル・ワークロード・運用を横断して設計し、制約はそれが発生したレイヤーの外で解決されることが多いという前提に立つ
- Azure Maiaでは2層スケールアップネットワークトポロジとシリコン統合NICでネットワーク機材を減らしつつ計算資源の稼働率を上げる
- Azure Cobalt CPUでシリコン上に細粒度の電力制御を実装し、同じメガワットでより多くのサーバーを稼働させる

## 使いどころ

- トークン単価・ワット単価でAIインフラ投資対効果を評価したいクラウド事業者
- 大規模言語モデルの提供コストを下げつつ可用性を高めたいプラットフォームチーム
- 半導体・電力・データセンター事業者が協調してAI基盤の効率を高める際の共通言語
