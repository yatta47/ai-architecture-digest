---
type: guidance
title: SageMaker HyperPodでの学習中サイレントデータ破損の検知と復旧
title_original: Detecting and recovering from silent data corruption on Amazon SageMaker HyperPod
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- gpu-fleet-reliability
components:
- Amazon SageMaker HyperPod
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/detecting-and-recovering-from-silent-data-corruption-on-amazon-sagemaker-hyperpod/
published_at: '2026-11-11'
---

## 概要

GPUが誤った値をエラーなく返すサイレントデータ破損は、HyperPodの既存のヘルス監視をすり抜け、全レプリカの勾配に伝播する。学習ジョブ自身から検知する3つの仕組みを追加して検知と復旧を行う方法を示す。

## 設計のポイント

- ハードウェアが報告しない異常を、学習ジョブ側の検査で検知する。
- 破損検知後に不良ノードを置換し、健全な状態から再開する。
- 損失が正常に見えても検査で発散を早期に捉える。

## 使いどころ

- 大規模GPUで事前学習を行う組織。
- 学習の計算資源の無駄を減らしたい基盤チーム。
- 障害の自動復旧を整備するSRE。
