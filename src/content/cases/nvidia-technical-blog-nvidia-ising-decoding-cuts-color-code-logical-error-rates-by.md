---
type: announcement
title: 3D CNNプリデコーダで量子誤り訂正カラーコードを高速・高精度復号
title_original: NVIDIA Ising Decoding Cuts Color Code Logical Error Rates by Over 300x
ai_relevant: false
company: NVIDIA
industry: other
cloud: []
patterns: []
components: []
data_sources: []
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/nvidia-ising-decoding-cuts-color-code-logical-error-rates-by-over-300x/
published_at: '2026-07-17'
---

## 概要

NVIDIAは量子誤り訂正向けのIsing Decoder ColorCode 1 Fastを公開し、三角カラーコードを対象とした小型の3D CNNプリデコーダで従来デコーダChromobius比で論理エラー率を最大347.7倍改善し、実行時間も7.3倍高速化したと報告した。cuQuantum/cuStabilizerによる合成データ生成から学習まで一式のパイプラインとモデル重み・学習レシピをオープンに提供し、各QPUのノイズ特性に合わせたリアルタイム復号器の構築を可能にする。速度と精度のトレードオフはCNN層数で調整でき、格子手術を含むフォールトトレラント計算への拡張を狙う。
