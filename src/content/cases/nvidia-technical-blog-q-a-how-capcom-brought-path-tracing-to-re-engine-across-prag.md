---
type: case
title: RE ENGINEへのリアルタイム・パストレーシング導入（Capcom）
title_original: 'Q&A: How Capcom Brought Path Tracing to RE ENGINE Across PRAGMATA and Resident Evil Requiem'
ai_relevant: false
company: Capcom
industry: media
cloud: []
patterns: []
components: []
data_sources: []
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/qa-how-capcom-brought-path-tracing-to-re-engine-across-pragmata-and-resident-evil-requiem/
published_at: '2026-07-17'
---

## 概要

Capcomの内製ゲームエンジンRE ENGINEチームが、約2年かけてリファレンス・パストレーサーを開発し一般的なDCC系パストレーサーと照合検証したうえで、DLSS Ray Reconstructionに最適化したゲーム向けパストレーサーへとスケールダウンし、『バイオハザード レクイエム』と『PRAGMATA』の2タイトルへ同時導入した事例。従来は間接光のみだったレイトレーシングを直接光にも拡張し、シャドウマップに依存しないことでゲームプレイとカットシーンの見た目の差を大幅に縮小、ストランドヘアのリアルタイム光透過なども実現した。NVIDIA RTX Kit上に構築し、AlphaTest向けのScreenSpaceAlphaTestや独自のReSTIR GIといった実装で実時間性能とノイズ低減を両立している。
