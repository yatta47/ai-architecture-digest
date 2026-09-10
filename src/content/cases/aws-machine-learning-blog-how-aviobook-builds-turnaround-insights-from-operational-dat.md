---
type: case
title: AvioBookが構築した航空機ターンアラウンド分析エージェント
title_original: How AvioBook builds turnaround insights from operational data with Amazon Bedrock AgentCore
company: AvioBook
industry: logistics
cloud:
- aws
patterns:
- ai-agent
- multi-agent-orchestration
- document-processing
components:
- Amazon Bedrock AgentCore
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-aviobook-uses-generative-ai-to-drive-airline-turnaround-insights/
published_at: '2026-09-10'
---

## 概要

Thales Group傘下のAvioBookは、航空機の到着から次の出発までの『ターンアラウンド』に関わる自動イベントとチャットログをAmazon Bedrock AgentCore上のマルチエージェント構成で分析し、運航管理者やディスパッチャーが自然言語で質問すると根拠付きで直接回答するConnected Analyticsを構築した。1分あたり約20ドルとされるゲート遅延コストの削減を狙う。

## 設計のポイント

- 役割ごとに専用エージェントを2つ用意し、それぞれがフライトルームのイベントとチャットログを突き合わせて根拠付きの回答を返す
- 自動送信されたイベントデータと、現場担当者の会話ログという『硬いデータ』と『柔らかいデータ』の両方を横断して参照する
- 遅延コードだけでは説明が半分しか伝わらない実態を踏まえ、根本原因の再構成を対話型の分析に委ねる

## 使いどころ

- 定型的な遅延コードだけでは実態を追いきれない、現場ログとイベントデータが分散した運用オペレーション
- 監査や振り返りのたびに人が過去ログを手作業で掘り返している業務プロセス
