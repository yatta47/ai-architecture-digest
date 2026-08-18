---
type: case
title: 通信タワー計画を自然言語で支援する社内AIアシスタント
title_original: 'High-Stakes Network Decisions Made in Minutes: How EDOTCO Group Is Transforming Network Planning With AI'
company: EDOTCO Group
industry: telecom
cloud:
- azure
patterns:
- rag
- text-to-sql
- data-federation
components:
- Azure Container Apps
- Azure Blob Storage
- Azure Generative AI
outcome:
  type: speed
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://news.microsoft.com/source/asia/features/high-stakes-network-decisions-made-in-minutes-how-edotco-group-is-transforming-network-planning-with-ai/
published_at: '2026-08-18'
---

## 概要

通信インフラ企業EDOTCO Groupは、計画・地理空間・運用データを統合するNaPAプラットフォームに続き、Azure Container Apps/Blob Storage/Generative AIで構築した対話型AIインターフェース『NaPA GPT』を導入した。プランナーは自然言語で質問するだけで、以前はデータサイエンスチームへの依頼から3日〜1週間かかっていた分析結果を数分で得られるようになり、基地局の新設候補地の評価やランキングを高速化した。

## 設計のポイント

- 計画・地理空間・運用データを単一プラットフォーム(NaPA)にまず統合し、複数レポート/ツールを行き来せずにカバレッジギャップや候補地を比較できるようにする
- データ統合の次のステップとして、専門チームへの依頼を待たずに誰でもデータへアクセスできる自然言語インターフェース(NaPA GPT)をAzure上に構築する
- チャットボット単体ではなく運用・地理空間データセットに直結させることで、条件を絞り込む追加質問(交通結節点付近を優先等)にもリアルタイムで応答できるようにする
- 社内利用にとどめず、選定した政府機関向けにインフラダッシュボードとして知見を拡張し、AI活用の対象領域を通信以外(規制計画・スマートシティ)にも広げる

## 使いどころ

- ネットワークプランナーが新規タワー設置候補地を人口・電波強度・需要増加などの複数条件から即座に絞り込みたい場合
- 商用・地域チームが専門のデータサイエンスチームを介さずに計画シナリオを自ら探索したい場合
- 政府機関など社外のステークホルダーにインフラ計画データをダッシュボード経由で共有したい場合
