---
type: guidance
title: NVIDIA AlpaGymで自動運転モデルをクローズドループの強化学習によりポストトレーニングする手法
title_original: How to Post-Train Autonomous Vehicle Models in Closed-Loop with NVIDIA Alpamayo
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- reinforcement-learning
- parallel-execution
components:
- NVIDIA Alpamayo
- AlpaSim
- AlpaGym
- NVIDIA Cosmos-RL
- Physical AI NuRec dataset
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-to-post-train-autonomous-vehicle-models-in-closed-loop-with-nvidia-alpamayo/
published_at: '2026-06-22'
---

## 概要

自動運転向けのVision-Language-Actionモデルは通常オープンループで学習されるため、実際の走行では小さな誤差が累積して性能が劣化する課題がある。NVIDIAはAlpaSimのシミュレーションロールアウトを学習経験に変換するクローズドループ強化学習フレームワークAlpaGymを提供し、GRPOアルゴリズムと分散Cosmos-RL学習基盤により単一GPUからマルチノードGPUクラスタまでスケールする非同期RLパイプラインで、Alpamayoモデルをポストトレーニングする方法を示す。

## 設計のポイント

- シミュレーションを最終評価だけでなく学習ループそのものに接続し、モデル自身の行動がもたらす結果から学習させることでオープンループとクローズドループの乖離を縮小する。
- 進行・車線維持・衝突回避・逸脱・快適性など複数の報酬項をAlpaSimのメトリクスから直接合成するシンプルな報酬設計から始め、観測された失敗モードに応じて段階的に報酬項を追加する。
- 推論・シミュレーション・学習・重み同期・ノード間通信を非同期かつ安定的に協調させるオーケストレーション層を用意し、ユーザーコードを変更せずにGPUクラスタへスケールできるようにする。

## 使いどころ

- オープンループ学習だけでは検出できない、走行の累積誤差や稀な失敗モードを本番投入前に洗い出したい自動運転モデル開発チーム。
- 既存のAlpamayoモデルや自前のAVモデルを、静的データセットではなくシミュレーションフィードバックで継続的に改善したいチーム。
- 単一GPUでの検証から大規模GPUクラスタでの本格学習まで、コード変更なしにスケールさせたい強化学習基盤の担当者。
