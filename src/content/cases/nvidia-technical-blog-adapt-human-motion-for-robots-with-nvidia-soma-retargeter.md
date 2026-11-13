---
type: announcement
title: 人間のモーションをヒューマノイドロボット向けに変換するSOMA Retargeter
title_original: Adapt Human Motion for Robots with NVIDIA SOMA Retargeter
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- reinforcement-learning
components:
- NVIDIA SOMA Retargeter
- NVIDIA Warp
- Newton
- GEM-X
- Kimodo
- ARDY
- Unitree G1
outcome:
  type: productivity
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/adapt-human-motion-for-robots-with-nvidia-soma-retargeter/
published_at: '2026-11-13'
---

## 概要

オープンソースのSOMA Retargeterは、SOMA骨格上の人間モーション(BVH)をロボットの体格に合わせてスケーリングし、逆運動学とフットプラント補正を経てCSVの関節軌道に変換する。v0.2では5種のヒューマノイド向け参照設定が提供され、SONICやProtoMotionsなどの方策学習に渡せる。

## 設計のポイント

- 共通のSOMA骨格を入力表現に据え、モーキャプ・動画再構成・生成モデルなど多様な入力源を一つのパイプラインに統合している。
- スケーリング→IK→後処理の段階を設定ファイルで調整でき、新しいロボットへの適応はConfiguratorで行える。
- 出力をCSVとモーションライブラリ形式にして方策学習へ接続する。

## 使いどころ

- ヒューマノイドの模倣学習用に参照モーションを大量に用意したいロボティクス研究者。
- 新しいロボット機体向けに既存モーションを再利用したい開発者。
