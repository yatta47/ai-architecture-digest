---
type: announcement
title: AMD Heliosを取り込みAzureが推論・データ処理・EDA向けVMを拡張
title_original: Microsoft expands Azure AI and HPC infrastructure with AMD
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- inference-optimization
components:
- Azure HDv2
- Azure HXv2
- Azure ND MI455X v7
- AMD EPYC
- AMD Instinct GPU
- AMD Helios
outcome:
  type: speed
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/working-at-the-frontier-rakuten
published_at: '2026-07-20'
---

## 概要

MicrosoftはAMDの次世代EPYC CPUとHeliosプラットフォームを採用し、データ処理向けHDv2、半導体設計(EDA)向けHXv2、AI推論向けND MI455X v7の3種のAzure VMを発表した。CPU性能や高速ストレージ・ネットワーキングを強化し、エージェント連携やRTLシミュレーションなど多様なAIインフラ需要にワークロード最適化した選択肢を提供する。

## 設計のポイント

- AIアクセラレータの手前で高密度・省電力なCPU処理を担うHDv2を用意し、データ準備やエージェント調整のボトルネックを解消する。
- 3D V-cacheと高クロックのHXv2でRTLシミュレーションなど半導体設計のシングルスレッド性能を強化し、800Gb InfiniBandで大規模MPIシミュレーションに対応する。
- AMD Instinct GPUを使うND MI455X v7で推論・検索・エージェントワークロード向けの本番スケール選択肢を追加する。

## 使いどころ

- エージェント連携やデータ前処理でCPUがボトルネックになっている大規模AI基盤運用チーム。
- 半導体設計・EDAワークロードをクラウドにオフロードしたい企業。
