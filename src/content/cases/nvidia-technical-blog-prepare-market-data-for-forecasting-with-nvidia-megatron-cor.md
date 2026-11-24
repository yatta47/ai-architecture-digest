---
type: guidance
title: Megatron Coreで株式バー時系列を予測学習用テンソルに整える
title_original: Prepare Market Data for Forecasting with NVIDIA Megatron Core
ai_relevant: false
company: NVIDIA
industry: financial-services
cloud: []
patterns: []
components: []
outcome:
  type: productivity
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/prepare-market-data-for-forecasting-with-nvidia-megatron-core/
published_at: '2026-11-24'
---

## 概要

NVIDIA Megatron Coreを使い、日中の市場バー(Parquet)をパッチ化・スライディングウィンドウ化して、リターンと出来高の複数ホライズン予測用テンソルに変換する前処理の手引き。日付分割とエンバーゴで情報漏洩を防ぎ、メモリマップのデータローダでテンソル並列グループ内にバッチを共有する。
