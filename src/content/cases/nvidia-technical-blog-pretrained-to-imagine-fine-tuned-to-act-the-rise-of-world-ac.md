---
type: opinion
title: '世界モデルから行動へ: World-Action Model(WAM)の台頭'
title_original: 'Pretrained to Imagine, Fine-Tuned to Act: The Rise of World-Action Models'
industry: cross-industry
cloud: []
patterns:
- fine-tuning
- video-intelligence
components:
- NVIDIA Cosmos
- Wan
- GR00T N1
- Pi-0
- DROID
- RoboArena
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/pretrained-to-imagine-fine-tuned-to-act-the-rise-of-world-action-models/
published_at: '2026-06-30'
---

## 概要

VLA(Vision-Language-Action)モデルに代わり、事前学習済みの動画・世界モデル(Wan、Cosmosなど)をバックボーンとして行動生成を学習する「World-Action Model(WAM)」という新潮流を解説する研究者による考察記事。WAMは現在の観測と行動から将来の状態を予測する世界モデルの能力を活用し、言語指示を物理世界での行動へ接続する「グラウンディングギャップ」を埋めることを目指すとしている。

## 設計のポイント

- VLM(視覚言語モデル)からの初期化ではなく、動画/世界モデルを行動生成のバックボーンとして再利用する
- 現在と将来の観測から行動系列を推定する逆ダイナミクスと、観測と行動を同時予測するjoint predictionという2つの学習目的を使い分ける
- Mixture-of-TransformersやDiffusion Transformerなど、動画トークンと行動トークンを別々の専門家で扱いつつAttentionを共有する構成を採る
- DROID・RoboArena・CALVIN・LIBEROなど複数ベンチマークで分布外(OOD)タスクへの汎化性能を検証する

## 使いどころ

- 実機デモンストレーションの収集が難しいロボット操作タスクで、動画データからの事前学習を活かしたい場合
- 言語指示から物理的な行動への「グラウンディングギャップ」を埋める必要がある汎用ロボットポリシーの開発
- 新しい物体・環境・指示への汎化性能(OOD耐性)が求められるマニピュレーションタスクの評価・設計
