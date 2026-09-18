---
type: guidance
title: コーディングエージェントの誤ったデプロイ判断をagent skillsで防ぎSageMaker AIへ本番デプロイする
title_original: Deploy Hugging Face models on Amazon SageMaker AI with coding agents
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- llmops
- inference-optimization
components:
- Amazon SageMaker AI
- Claude Code
- Kiro
- AWS Deep Learning Containers
- Amazon CloudWatch
- Hugging Face Skills
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/deploy-hugging-face-models-on-amazon-sagemaker-ai-with-coding-agents/
published_at: '2026-09-18'
---

## 概要

ガイドなしのコーディングエージェントにHugging Faceモデルのデプロイを任せると、学習データが古いために互換性のないサービングコンテナ（TGI）を選び続け、ヘルスチェック失敗やGPU課金の無駄が発生することを実証。デプロイ知識を6つのagent skillsとして外部化し、コーディングエージェントに読み込ませることで、正しいサービングコンテナ選定・オートスケーリング・CloudWatchアラーム・検証済みのティアダウンまで一貫した本番構成を自動生成できるようにした。

## 設計のポイント

- モデルの学習データが持たない『最新のデプロイ知識』を、編集可能なスキルファイル（SKILL.md）として外部化し、モデル更新より速いペースで更新できるようにする
- オーケストレーション用スキルが必要な情報だけを聞き、AWSコンテキスト検出・Python環境構築・IAM事前検証・サービングイメージ選定・本番デフォルト設定の5スキルへ処理を委譲する構成にする
- 『TGIをデフォルトにしない』のような否定形のルールをスキル記述に明示し、学習データに多いが古い選択肢へエージェントが逆戻りするのを防ぐ

## 使いどころ

- リリース直後の新しいモデルなど、学習データに含まれない最新モデルをコーディングエージェント経由でデプロイしたいチーム
- オートスケーリングや監視アラームなど本番運用に必要な構成をエージェント任せにしても抜け漏れなく揃えたいMLOpsチーム
- GPUの無駄な課金につながる試行錯誤型のデプロイ失敗を減らしたい組織
