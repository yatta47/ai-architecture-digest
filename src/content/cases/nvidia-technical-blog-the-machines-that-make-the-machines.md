---
type: case
title: NVIDIAがロボットでGB300テスターのトレイを組み立てる
title_original: The Machines that Make the Machines
company: NVIDIA
industry: manufacturing
cloud: []
patterns:
- inference-optimization
components:
- FoundationPose
- SAM3
- DOPER
- NVIDIA Isaac
outcome:
  type: productivity
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/the-machines-that-make-the-machines/
published_at: '2026-10-07'
---

## 概要

NVIDIAのロボティクスラボがGB300テスタートレイの組み立てをロボットで実現。FoundationPoseによる知覚とインピーダンス制御でバスバー組み立ては成功率95%超。コネクタ把持には専用の姿勢推定DOPERを使う。

## 設計のポイント

- 古典的モジュール構成に、難所だけ専用の学習モデルを足す。
- 合成データと実データで姿勢推定を学習する。

## 使いどころ

- 製造ラインでの精密な組み立て自動化を検討する場面に効く。
