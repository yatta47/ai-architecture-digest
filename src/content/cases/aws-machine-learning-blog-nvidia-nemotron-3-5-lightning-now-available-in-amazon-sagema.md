---
type: announcement
title: 高頻度エージェント処理向け軽量モデルNemotron 3.5 LightningをSageMaker JumpStartで提供開始
title_original: NVIDIA Nemotron 3.5 Lightning Now Available in Amazon SageMaker JumpStart
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- inference-optimization
- multi-model-routing
- reasoning-computation-separation
components:
- Amazon SageMaker JumpStart
- Amazon SageMaker AI
- NVIDIA Nemotron 3.5 Lightning
- NVIDIA NeMo Switchyard
- NVIDIA NeMo
- Hugging Face
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/nvidia-nemotron-3-5-lightning-now-available-in-amazon-sagemaker-jumpstart/
published_at: '2026-08-17'
---

## 概要

NVIDIAのオープンモデルNemotron 3.5 Lightning(MoE、総パラメータ30B・アクティブ3B)がAmazon SageMaker JumpStartから独自のサービングインフラ構築なしにデプロイ可能になった。常時稼働するエージェントの中でも、アラート分類やフォーム抽出のような高頻度・定型的なステップをフロンティアモデルより低コスト・低レイテンシで処理することを狙い、最大4倍のスループットと最大30%高速なタスク完了を謳う。NeMo Switchyardのようなルーターと組み合わせ、複雑な計画立案はフロンティアモデル、定型処理はLightningに振り分ける『モデルのシステム』構成を想定している。

## 設計のポイント

- すべてのエージェントステップを単一の大規模モデルに通さず、高頻度・定型ステップは特化型軽量モデルにルーティングする『モデルのシステム』構成にする
- MoEアーキテクチャ(30B中3Bアクティブ)と投機的デコーディング(DFlash)でスループットとレイテンシを最適化する
- 100万トークンのコンテキスト長で長時間セッションの状態を保持し、頻繁な再グラウンディングを避ける
- SageMaker JumpStartのモデルカードからサービングインフラを自前で構築せずにワンクリックでエンドポイントを立てる

## 使いどころ

- 常時稼働するパーソナルアシスタントやアラート分類・記録抽出など高頻度なエージェントのサブタスク処理
- 金融の文書抽出・ポリシーチェック、通信のアラームトリアージ、小売のカタログ整備など業種別の定型的エージェントワークフロー
- フロンティアモデルと軽量モデルを使い分けてコストとレイテンシを最適化したいマルチモデル構成のエージェント基盤
