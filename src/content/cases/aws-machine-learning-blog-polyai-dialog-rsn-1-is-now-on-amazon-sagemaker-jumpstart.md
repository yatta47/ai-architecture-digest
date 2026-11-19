---
type: announcement
title: 音声を直接推論するリアルタイム対話モデルをSageMaker上に自社環境デプロイ
title_original: PolyAI Dialog-RSN-1 is now on Amazon SageMaker JumpStart
company: PolyAI
industry: cross-industry
cloud:
- aws
patterns:
- voice-agent
- inference-optimization
components:
- Amazon SageMaker JumpStart
- AWS Marketplace
- Amazon SageMaker
- Amazon CloudWatch
- AWS IAM
- Amazon VPC
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/polyai-dialog-rsn-1-is-now-on-amazon-sagemaker-jumpstart/
published_at: '2026-11-19'
---

## 概要

PolyAIの音声対話推論モデルDialog-RSN-1がAWS MarketplaceとSageMaker JumpStartで提供開始された。通話音声を直接入力として推論・応答まで単一パスで行い、利用者のAWSアカウント内のVPC/IAM配下でエンドポイントとして動かせる。

## 設計のポイント

- STT・推論・発話タイミング判定を1モデルに統合し、複数段のハンドオフによる遅延を排除している。
- OpenAI Realtimeプロトコル互換のエンドポイントにして、既存クライアントはbase URL変更だけで接続できる。
- レイテンシ/スループット/コスト/バランスの最適化プロファイルを選ぶだけで配信構成を決められる。
- 推論を自アカウントVPC内に閉じ、通話音声と文字起こしのデータ境界を自社管理にできる。

## 使いどころ

- コンタクトセンターで音声データを外部に出さずに音声エージェントを導入したいとき。
- 既存のRealtimeクライアントを流用してモデルだけ差し替えたいとき。
- 通話量の増減に応じて配信プロファイルを切り替えたいとき。
