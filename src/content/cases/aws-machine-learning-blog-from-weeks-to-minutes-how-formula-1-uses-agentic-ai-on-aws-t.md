---
type: case
title: F1がBedrock AgentCoreでMarTechデータ連携を自動化
title_original: 'From weeks to minutes: How Formula 1® uses agentic AI on AWS to accelerate data operations'
company: Formula 1
industry: media
cloud:
- aws
patterns:
- ai-agent
- document-processing
- event-driven
- root-cause-analysis
components:
- Amazon Bedrock AgentCore
- AWS Lambda
- Amazon S3
- Amazon CloudWatch
- Amazon SageMaker Unified Studio
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/from-weeks-to-minutes-how-formula-1-uses-agentic-ai-on-aws-to-accelerate-data-operations/
published_at: '2026-08-03'
---

## 概要

F1はマーケティングデータ基盤Customer 360への新規データソース連携に6〜8週間を要していたが、Amazon Bedrock AgentCore上のエージェント群がBRDから設定・パイプライン・ガバナンスポリシーを自動生成することで約40分に短縮した。エージェントはGitHub/Jiraと連携してPRとチケットを起票し、人はレビュー・承認のみを行う。

## 設計のポイント

- BRDアップロードをトリガーに設定生成→承認→本体パイプライン生成の2フェーズに分割し、各段階で人間のレビューゲートを挟む
- 単一エージェントにスキーマ推論・品質検証・ガバナンス適用などのモジュール型スキルを持たせ、リクエストに応じて動的に組み合わせる
- GDPR分類をエージェントが自動タグ付けし、ガバナンスレジストリに即時反映してコンプライアンス確認の待ち時間を無くす
- AgentCore Observabilityで全エージェントの会話・操作をCloudWatchにトレースし、監査可能性を確保する

## 使いどころ

- 新規データソースのオンボーディングが恒常的にボトルネックになっているデータ基盤チーム
- GDPR等の個人情報分類を人手でレビューしているガバナンス担当
- アップストリームのスキーマ変更が頻発し、パイプラインの保守負荷が高い環境
