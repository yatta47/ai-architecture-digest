---
type: guidance
title: コーディングエージェントのリクエストをBedrock上でNeMo Switchyardにより最適モデルへルーティング
title_original: Route coding agent requests to the right model on Amazon Bedrock with NVIDIA NeMo Switchyard
company: AWS / NVIDIA
industry: cross-industry
cloud:
- aws
patterns:
- multi-model-routing
- llm-gateway
- cost-optimization
components:
- Amazon Bedrock
- NVIDIA NeMo Switchyard
- LiteLLM
- AWS CDK
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/route-coding-agent-requests-to-the-right-model-on-amazon-bedrock-with-nvidia-nemo-switchyard/
published_at: '2026-11-13'
---

## 概要

LiteLLMゲートウェイにSwitchyardのルーティングプラグインを載せ、Amazon Bedrock上のモデルへコーディングエージェントのリクエストを振り分けるサンプル。評価指標をトークン単価ではなく「解決タスクあたりコスト」とし、ステージルーティングとランダムルーティングをベンチマークする。

## 設計のポイント

- ツール実行履歴を見て2候補モデルから選ぶステージルーティングで、タスク段階に応じたモデル使い分けを行う。
- 評価指標を解決タスクあたりコスト（総コスト÷テスト合格数）にし、再試行や未完了のコストも含める。
- LiteLLMをLLMゲートウェイとして置き、ルーティング戦略を差し替え可能にする。

## 使いどころ

- Claude CodeやCodex CLIなどのエージェント利用コストを最適化したいプラットフォームチーム。
- モデルルーティングをA/Bで自社ワークロードに対し評価したい場合。
