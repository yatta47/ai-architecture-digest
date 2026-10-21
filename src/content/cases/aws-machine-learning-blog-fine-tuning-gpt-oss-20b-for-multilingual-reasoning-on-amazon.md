---
type: guidance
title: 'GPT-OSS-20Bの多言語推論: SFTとGRPOの使い分け(SageMaker HyperPod)'
title_original: Fine-tuning GPT-OSS-20B for multilingual reasoning on Amazon SageMaker HyperPod
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- fine-tuning
- reinforcement-learning
- multilingual-localization
- eval
components:
- Amazon SageMaker HyperPod
- Amazon EKS
- TRL
- veRL
- KubeRay
- GPT-OSS-20B
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/fine-tuning-gpt-oss-20b-for-multilingual-reasoning-on-amazon-sagemaker-hyperpod/
published_at: '2026-10-20'
---

## 概要

基盤モデルは指示しても英語で推論し、対象言語で推論できた割合は22%だった。SFTで挙動を教え、GRPOは既に出せる挙動を磨く用途と整理し、HyperPod上で検証した。

## 設計のポイント

- SFTはモデルにない挙動を教え、GRPOは既に出る挙動を最適化すると使い分ける。
- 能力ギャップに手法を合わせることが結果を決める。
- 推論言語と回答言語を別指標で評価する。

## 使いどころ

- 非英語ユーザー向けに推論モデルをカスタマイズする場面。
- SFTとRLのどちらに投資するか判断する場面。
