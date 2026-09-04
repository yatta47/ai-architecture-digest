---
type: guidance
title: NVIDIA Cosmos 3で回すフィジカルAIモデルファクトリー
title_original: Build a Physical AI model factory with NVIDIA Cosmos 3 on SageMaker HyperPod
industry: manufacturing
cloud:
- aws
patterns:
- fine-tuning
- gpu-fleet-reliability
components:
- NVIDIA Cosmos 3
- Amazon SageMaker HyperPod
- Amazon EKS
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-a-physical-ai-model-factory-with-nvidia-cosmos-3-on-sagemaker-hyperpod/
published_at: '2026-09-04'
---

## 概要

ロボットや自動運転車のようなフィジカルAIは合成データ生成・後段学習・評価の継続的ループが必要であり、単一のMixture-of-TransformersモデルNVIDIA Cosmos 3をAmazon SageMaker HyperPod上の1つのGPUノードプールで時分割共有することで、生成・行動ラベリング・ポリシー推論の3役割を賄うモデルファクトリーの構築方法を解説する。

## 設計のポイント

- 1つのトランスフォーマー本体が世界モデル(生成)・逆ダイナミクス(行動ラベリング)・ポリシー(推論)の3モードを切り替えて担い、ステージごとに別々のGPUプールを持たずに済む
- 学習時はフル拡散ステップと動画デコードまで行う一方、推論時は数ステップの拡散と行動トークンのみのデコードに絞る非対称設計で計算コストを抑える
- コスト指標としてピークスループットではなく予約GPU時間あたりの有効な進捗(GPU goodput)を重視し、パイプライン全体でまとめてキャパシティを確保する

## 使いどころ

- ロボットアームや自動運転車など実世界データの収集コストが高い領域で合成データ学習を回したいチーム
- 生成・学習・評価それぞれに別クラスタを立てず、1つの永続的なGPUクラスタで運用コストを下げたい基盤チーム
- テレオペ記録や第三者視点映像など大量の未ラベル動画を行動ラベル付きデータに変換したい場合
