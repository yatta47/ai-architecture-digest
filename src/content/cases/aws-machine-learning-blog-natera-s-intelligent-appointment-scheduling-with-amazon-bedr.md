---
type: case
title: NateraのBedrock AgentCoreで実現したリアルタイム音声予約エージェント
title_original: Natera's intelligent appointment scheduling with Amazon Bedrock AgentCore
company: Natera
industry: healthcare
cloud:
- aws
patterns:
- voice-agent
- ai-agent
- event-driven
components:
- Amazon Bedrock AgentCore
- Amazon Bedrock
- Twilio
- Amazon ECS
- Amazon Connect Health
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/nateras-intelligent-appointment-scheduling-with-amazon-bedrock-agentcore/
published_at: '2026-08-26'
---

## 概要

遺伝子検査企業Nateraは、訪問採血の予約受付をAmazon Bedrock AgentCore上のリアルタイム音声エージェントに置き換え、電話予約の自動化と患者体験の向上を実現した。デュアルWebSocketブリッジ、イベント駆動のレイテンシーマスキング、段階的信頼モデルという3原則により、500件のE2Eシミュレーションでツール呼び出し精度100%・体感レイテンシー7秒未満・1件あたり0.01ドル未満のコストを達成した。

## 設計のポイント

- テレフォニー側とモデル推論側それぞれに独立したWebSocket接続を張り、間にオーケストレーション層を挟む『デュアルWebSocketブリッジ』でベンダーやモデルの差し替えを容易にした
- ツール呼び出し中は文脈に沿ったフィラー応答を並行生成する『イベント駆動レイテンシーマスキング』で、バックエンド処理中も会話の自然な流れを維持した
- 本人確認を会話の最初に一括で求めず、対話が進むにつれて認証レベルとメモリアクセス範囲を段階的に引き上げる『プログレッシブ信頼モデル』を採用した
- 自前運用のAmazon ECSコンテナから、AgentCoreのフルマネージド実行環境とビルトイン観測機能・メモリ管理へ移行し運用負荷を削減した

## 使いどころ

- 医療など高いコンプライアンス要件下で、電話予約や本人確認を自動化したいコールセンター業務
- テレフォニーとFMベンダーを疎結合にして将来差し替えたいリアルタイム音声AIシステム
- 処理待ち時間中も自然な会話体験を保ちたいカスタマーサポート／スケジューリングエージェント
