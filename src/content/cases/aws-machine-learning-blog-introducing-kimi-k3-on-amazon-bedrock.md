---
type: announcement
title: Amazon BedrockでのKimi K3提供開始と明示的プロンプトキャッシュ活用
title_original: Introducing Kimi K3 on Amazon Bedrock
industry: cross-industry
cloud:
- aws
patterns:
- llmops
- context-engineering
- inference-optimization
components:
- Amazon Bedrock
- Kimi K3
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-kimi-k3-on-amazon-bedrock/
published_at: '2026-09-18'
---

## 概要

Amazon BedrockでMoonshot AIのオープンウェイトモデルKimi K3が利用可能になった。1Mトークンのコンテキスト窓と明示的プロンプトキャッシュに対応し、長時間稼働するコーディング・知識ワークフローでの再利用コンテキストのレイテンシとコストを削減する。ゼロデータ保持・ゼロオペレーターアクセスにより、セキュリティ姿勢を変えずにオープンウェイトモデルを採用できる。

## 設計のポイント

- 1,024トークン以上の再利用可能なプロンプト前半部分に明示的なキャッシュブレークポイントを設定し、以降のリクエストでキャッシュヒット時に入力トークン課金を割引する
- 地域制約のないワークロードはグローバル推論プロファイルを使い約10%コストを抑え、データ在住要件がある場合は米国リージョン限定プロファイルを選ぶ
- OpenAI互換のResponses/Chat Completions APIとBedrock Invoke/Converse APIの両方を提供し、既存のコーディングエージェント（OpenCode等）からモデル切り替えのみで利用できるようにする

## 使いどころ

- リポジトリ全体やツール定義など安定したコンテキストを繰り返し送るコーディングエージェント・知識ワークフロー
- オープンウェイトモデルを使いたいがデータ境界・不学習保証などセキュリティ要件を維持したいチーム
- 複数のオープンウェイトモデルをBedrock上で一元的に評価・切り替えたいプラットフォームチーム
