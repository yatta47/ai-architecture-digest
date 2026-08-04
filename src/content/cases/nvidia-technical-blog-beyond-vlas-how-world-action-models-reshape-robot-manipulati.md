---
type: guidance
title: NVIDIA Cosmos 3によるワールドアクションモデル(WAM)基盤とロボット操作ポリシーの構築
title_original: 'Beyond VLAs: How World Action Models Reshape Robot Manipulation'
company: NVIDIA
industry: manufacturing
cloud: []
patterns:
- fine-tuning
- inference-optimization
- video-intelligence
- unified-runtime
components:
- NVIDIA Cosmos 3
- Cosmos3-Nano-Policy-DROID
- Cosmos3-Edge-Policy-DROID
- NVIDIA Jetson
- NVIDIA Cosmos Edge
- NVIDIA Cosmos Nano
- NVIDIA Cosmos 3 Super
- DROID
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/beyond-vlas-how-world-action-models-reshape-robot-manipulation/
published_at: '2026-07-31'
---

## 概要

VLM(視覚言語モデル)をバックボーンとするVLAはシーンの意味理解には優れるが、物体がどう動くかという物理ダイナミクスを学習していないため未知環境への汎化が弱い。NVIDIAはビデオワールドモデルをバックボーンとするWorld Action Model(WAM)という考え方を提示し、Mixture-of-Transformers構成のオープンモデルCosmos 3を物理事前知識を持つ基盤として、DROIDプラットフォーム向けポリシー(Cosmos3-Nano/Edge-Policy-DROID)をポストトレーニングした。この基盤により、少ないタスク固有データでの新規ロボットへの適応や、ワークステーションからJetsonでのオンデバイス推論まで幅広い展開が可能になる。

## 設計のポイント

- 言語理解に強いVLMではなく、物理ダイナミクスを学習したビデオワールドモデルをバックボーンに採用し、ポリシーに物理事前知識を持たせる
- Mixture-of-Transformers構成により、テキスト等の離散トークンは自己回帰生成、画像・動画・アクション等の連続モダリティは拡散モデルで生成し、モダリティごとに適した生成機構を使い分ける
- ポストトレーニングはバックボーンのオムニ機能(推論・動画生成)を保持したまま特定ロボット向けのアクション生成に特化させる設計とする
- 4B(Edge)・16B(Nano)・64B(Super)と複数サイズを用意し、ワークステーションでの高スループット推論からJetsonでのオンデバイス推論まで段階的にデプロイできるようにする

## 使いどころ

- 同一タスクの厳密なデモンストレーションが揃わない多様なインタラクションデータしかなくても、物理法則の学習によってデータを有効活用したいロボティクスチーム
- 新しいロボットアームやグリッパーへ少数デモンストレーションで迅速に適応させたい場面
- 訓練分布に含まれない物体形状・配置・照明などへのゼロショット汎化が求められるマニピュレーションタスク
- クラウド上の高スループット推論からエッジデバイス(Jetson)でのリアルタイム推論まで、複数の展開形態を1つの基盤モデルでカバーしたい場合
