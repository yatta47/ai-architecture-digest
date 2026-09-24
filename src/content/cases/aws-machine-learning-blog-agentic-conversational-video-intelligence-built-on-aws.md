---
type: guidance
title: Strands AgentsとBedrockで動く会話型の動画インテリジェンス
title_original: Agentic conversational video intelligence built on AWS
company: AWS
industry: media
cloud:
- aws
patterns:
- video-intelligence
- ai-agent
- guardrails
- multi-tenant-analytics
components:
- Amazon Bedrock
- Amazon Rekognition
- Amazon Transcribe
- Amazon Bedrock Data Automation
- Amazon S3
- Strands Agents SDK
- Claude Sonnet
- Amazon Bedrock Guardrails
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/agentic-conversational-video-intelligence-built-on-aws/
published_at: '2026-09-23'
---

## 概要

動画への自然言語の質問に答えるソリューションを、Strands Agents SDKの単一エージェントで構築する方法の解説。質問内容に応じてエージェントがTranscribe、Rekognition、Bedrock Data Automationを実行時に選び、結果をキャッシュして追質問に再利用する。メディア企業の事例では、200本超の録画のレビュー工数を約80%削減したとされる（顧客の社内比較、第三者検証なし）。

## 設計のポイント

- 質問ごとに固定パイプラインを組まず、エージェントがツールの説明に基づいて処理を実行時に決める。
- 解析結果をS3にキャッシュし、既処理の動画への追質問は1秒未満で返す。
- ユーザー別のS3プレフィックスでマルチテナント分離を行う。
- 顔照合など監視用途ではBedrock Guardrailsでフィルタリングと根拠チェックを追加する。

## 使いどころ

- 会議録画や現地調査動画が溜まり、確認作業が追いつかない専門サービス企業。
- 監視映像や事故映像から特定の出来事を素早く検索したい部門。
- 質問種別ごとの個別開発を避け、ツール追加で機能拡張したいチーム。
