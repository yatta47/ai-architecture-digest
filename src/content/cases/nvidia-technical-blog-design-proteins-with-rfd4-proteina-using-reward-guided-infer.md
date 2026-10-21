---
type: guidance
title: RFD4-Proteinaによる報酬誘導型推論時探索でのタンパク質設計
title_original: Design Proteins with RFD4-Proteina Using Reward-Guided Inference-Time Search
company: NVIDIA
industry: healthcare
cloud: []
patterns:
- inference-optimization
- ai-agent
components:
- RFD4-Proteina
- NVIDIA NIM
- OpenFold3
- BioNeMo Agent Toolkit
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/design-proteins-with-rfd4-proteina-using-reward-guided-inference-time-search/
published_at: '2026-10-21'
---

## 概要

RFD4-Proteinaはタンパク質の配列と全原子構造を同時に共設計し、報酬誘導型の推論時探索で有望候補に計算を集中させる。サンプリングを約400から60ステップに減らし、RFD3比で3.8倍高速・ピークメモリ84%減としている。PD-L1バインダー設計のチュートリアルを示す。

## 設計のポイント

- 配列と構造を同時生成し、逆折りたたみの受け渡し工程を省く。
- 生成途中の状態を報酬で評価して分岐・保持し、計算を有望候補に集中させる。
- OpenFold3などのオラクルで幾何・相互作用・信頼度を採点する。
- エージェント用スキルで生成・探索・評価・保存をキャンペーンとして自動化できる。

## 使いどころ

- 創薬の計算生物学者がバインダー候補を絞り込む場面。
- HTTPのNIMで素早く推論をデプロイしたい場面。
