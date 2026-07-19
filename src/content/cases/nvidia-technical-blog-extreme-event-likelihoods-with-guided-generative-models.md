---
type: guidance
title: 拡散モデルによる異常気象発生確率のガイド付きサンプリング推定
title_original: Extreme Event Likelihoods with Guided Generative Models
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- generative-simulation
- risk-modeling
components:
- NVIDIA cBottle
- NVIDIA Earth2Studio
- CBottleTCGuidance
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/extreme-event-likelihoods-with-guided-generative-models/
published_at: '2026-07-10'
---

## 概要

NVIDIAは拡散ベースの気候エミュレータcBottleを熱帯低気圧などの稀な極端現象へガイドし、ガイド有無の対数尤度比（オッズ比）で重み付け補正することで、従来のモンテカルロ法よりサンプル効率よく発生確率を推定する手法を提案した。この手法はオープンソースのNVIDIA Earth2Studio上のCBottleTCGuidanceとして実装され、フロリダ沖・ハリケーンシーズンを想定したガイド付きサンプリングの実行例が示されている。

## 設計のポイント

- 拡散モデルを稀事象（熱帯低気圧など）の状態へガイドし、モンテカルロ法よりサンプル効率よく尤度の裾野を探索する
- ガイド有無の対数尤度比（オッズ比）を生成モデルの2階微分から算出し、重要度サンプリングの重みとして元の気候分布下の確率を復元する
- 推論パイプラインをEarth2Studioのようなオープンソース推論基盤へ組み込み、事前学習済みチェックポイントをNGCから取得して再利用可能にする

## 使いどころ

- 沿岸への熱帯低気圧上陸リスクなど、物理シミュレーションでは高コストな稀頻度事象の確率推定を行いたいチーム
- 保険モデリングやインフラ計画、気候アトリビューション研究など、極端事象のテールリスクを定量化したい分析者
