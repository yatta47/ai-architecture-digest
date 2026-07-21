---
type: announcement
title: 'NVIDIA Cosmos 3: 推論・世界生成・行動生成を統合した物理AI基盤モデル'
title_original: Develop Physical AI Reasoning, World, and Action Models with NVIDIA Cosmos 3
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- unified-runtime
- video-intelligence
- eval
- fine-tuning
components:
- NVIDIA Cosmos 3 Nano
- NVIDIA Cosmos 3 Super
- Cosmos NIM
- NVIDIA RTX PRO 6000
- NVIDIA Hopper
- NVIDIA Blackwell
- Hugging Face
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3/
published_at: '2026-06-25'
---

## 概要

NVIDIAはロボットや自動運転車、スマートスペース向けの物理AI基盤モデル「Cosmos 3」をオープンソースで公開した。Mixture-of-Transformers構成のReasonerタワー（VLMによる物理理解）とGeneratorタワー（拡散モデルによる物理整合的な映像・行動生成）を単一モデルに統合し、従来別々だった世界生成・物理理解・シーン生成の複数モデル運用を不要にしている。あわせて16Bと64Bの2サイズのモデル、学習データセット、後学習スクリプト、そして人手検証ベースの新評価基準HUEを公開し、開発の再現性と評価の信頼性を高めている。

## 設計のポイント

- VLMベースの自己回帰型Reasonerタワーと拡散ベースのGeneratorタワーを1モデルに統合し、複数モデル間のオーケストレーションを排除するMixture-of-Transformers構成を採用した。
- 推論専用の軽量呼び出し（Reasonerのみ）と、両タワーを使う本格的な生成呼び出しを使い分けられるようにし、用途に応じた計算コストの最適化を可能にした。
- 16B（Nano、ワークステーションでのリアルタイム推論向け）と64B（Super、データセンターでの最高品質・大規模合成データ生成向け）の2モデル展開で、推論速度と生成品質のトレードオフに応じた選択肢を用意した。
- 自動採点が飽和しがちなSOTA動画生成モデルの差を可視化するため、意味整合性・物理法則・幾何学的推論・視覚的整合性の4軸でYes/Noのアトミックな事実検証を行うHUE評価フレームワークを新設し、主観評価から客観検証へ転換した。

## 使いどころ

- ロボットマニピュレーションを開発するチームが、映像・行動同時生成のワールドアクションモデルやVision-Language-Actionモデルとしてロボット学習ポリシーを構築する場面。
- 自動運転開発チームが、実車で収集しにくい稀なエッジケースの走行映像を合成生成し、交通異常検知（Traffic Anomaly Reasoning）などの評価に活用する場面。
- 倉庫の安全監視システムを構築するチームが、倉庫内オペレーションの合成映像データを生成し異常検知モデルの学習・評価に用いる場面。
- エッジ/ワークステーションでのリアルタイム推論が必要なチームはCosmos 3 Nanoを、データセンターで大規模合成データ生成や高精度な物理推論が必要なチームはCosmos 3 Superを選択する場面。
