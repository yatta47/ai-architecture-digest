---
type: announcement
title: 長文脈でも毎秒3000トークン超を実現するGroq 3 LPXとVera Rubinの協調推論アーキテクチャ
title_original: How NVIDIA Groq 3 LPX Unlocks Ultrafast Interactivity at Long Context on NVIDIA Vera Rubin
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- inference-optimization
- reasoning-computation-separation
components:
- NVIDIA Groq 3 LPX
- NVIDIA Vera Rubin NVL72
- LP30 LPU
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-nvidia-groq-3-lpx-unlocks-ultrafast-interactivity-at-long-context-on-nvidia-vera-rubin/
published_at: '2026-08-24'
---

## 概要

NVIDIA Groq 3 LPXは、コンパイラがチップ間通信をクロックサイクル単位で事前スケジューリングする決定論的実行モデルにより、100Kトークンの長文脈でもGemma 4 31Bモデルで毎秒3,431トークンという業界最高水準のインタラクティブ性をArtificial Analysisベンチマークで達成した。小バッチのテンソル並列で支配的になる「ファーストビットレイテンシ」を事前計画された転送スケジュールで最小化し、Vera Rubin NVL72と組み合わせて2兆パラメータ超のマルチエージェントモデルを高インタラクティブ・長文脈で提供する。

## 設計のポイント

- 実行前にコンパイラがチップ間通信の全スケジュールを決定論的に確定させることで、実行時のアービトレーションを不要にしファーストビットレイテンシを最小化する
- 小バッチサイズでのテンソル並列は協調コストがボトルネックになりやすいため、通信スケジュールの事前最適化で高インタラクティブ性を維持する
- prefill-decode分離やattention-FFN分離、投機的デコードなどVera Rubin NVL72との複数の協調実行構成をサポートし、モデル規模に応じて構成を切り替えられるようにする

## 使いどころ

- マルチターンでコンテキストが数十万トークンまで蓄積するエージェント型セッションを高速に処理したい場合
- 毎秒3000トークン超のようなユーザー体感速度が要求される対話型AIサービス
