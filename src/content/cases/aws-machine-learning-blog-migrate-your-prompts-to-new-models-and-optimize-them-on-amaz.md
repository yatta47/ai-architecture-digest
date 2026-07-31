---
type: announcement
title: Bedrock Advanced Prompt Optimizationでモデル移行時のプロンプト再調整を自動化
title_original: Migrate your prompts to new models and optimize them on Amazon Bedrock
industry: cross-industry
cloud:
- aws
patterns:
- prompt-optimization
- eval
- multi-model-routing
components:
- Amazon Bedrock
- AWS Lambda
- Amazon S3
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/migrate-your-prompts-to-new-models-and-optimize-them-on-amazon-bedrock/
published_at: '2026-07-30'
---

## 概要

Amazon Bedrockに、最大5モデルを対象にプロンプトを最適化し性能を比較できるAdvanced Prompt Optimizationが追加された。評価指標に基づき「評価→書き換え→再評価」を繰り返す強化学習的なフィードバックループでプロンプトを改善し、モデル移行と同一モデルでの性能改善の両方に使える。

## 設計のポイント

- プロンプト最適化を評価指標（Lambda関数・LLM-as-a-Judge・自然言語の基準）から逆算するメトリクス駆動ループとして設計する
- 1ジョブで最大5モデルを比較し、品質スコアだけでなくTTFTと推論コストも同時に評価する
- 複数の評価観点がある場合は重み付き複合メトリクスとして単一スコアに集約する
- 画像やPDFを含むマルチモーダル入力にも同じ最適化ループを適用できるようにする

## 使いどころ

- 新モデル登場のたびに手作業でプロンプトを再チューニングしているチーム
- モデルロックインを避けて低コスト・低レイテンシなモデルへ乗り換えたいプロダクトチーム
- プロンプト変更のリグレッションを体系的な評価なしに見逃してしまっている開発チーム
