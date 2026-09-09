---
type: case
title: トークン生成に頼らず潜在空間で推論する脳型アーキテクチャBDHの開発基盤(Pathway)
title_original: Pathway's brain-inspired architecture development on Amazon SageMaker HyperPod
company: Pathway
industry: cross-industry
cloud:
- aws
patterns:
- reasoning-computation-separation
- inference-optimization
components:
- Amazon SageMaker HyperPod
- PyTorch
- BDH (Dragon Hatchling)
- BDH-CQ
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/pathways-brain-inspired-architecture-development-on-amazon-sagemaker-hyperpod/
published_at: '2026-09-08'
---

## 概要

Pathwayは、chain-of-thoughtのようにトークン列として推論を外部化するのではなく、疎で局所的なニューロン結合による潜在空間の反復計算で推論する『BDH（Dragon Hatchling）』アーキテクチャを開発した。学習にはAmazon SageMaker HyperPodを用い、PyTorchと統合してコンピュートを効率的に共有・スケールしている。150Mパラメータのモデルで、ARC-AGI-1におけるコスト効率で新たな最高水準を達成したという。

## 設計のポイント

- 推論をトークン列として外部化せず、疎で局所的なニューロン間結合（シナプス的接続）による潜在状態の反復計算として実装する
- Hebb則（同時発火するニューロンほど結合が強まる）でアテンション機構を実装し、常時活性化するニューロンを全体の約5%に抑えて計算量を削減する
- テスト時の重み更新やファインチューニングを行わずに、文脈内で内部メモリ（潜在状態）を更新して新しい問題に適応する
- Amazon SageMaker HyperPodでコンピュート資源を弾力的かつ低コストに共有し、独自アーキテクチャの学習をスケールする

## 使いどころ

- 長時間・多段階の推論を、肥大化するコンテキストウィンドウやKVキャッシュに頼らず低コストで行いたい研究開発
- モデルの意思決定過程を（シナプス的接続として）解釈・監視したい高規制業界向けAIの信頼性要件
- 既存Transformer基盤の学習・推論コストを見直し、次世代アーキテクチャを大規模クラスタで試したいAI研究チーム
