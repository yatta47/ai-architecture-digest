---
type: case
title: Circle KのBedrockによるDevOpsインシデント自動トリアージ
title_original: How Circle K accelerated DevOps incident triage to under 15 minutes with Amazon Bedrock
company: Circle K
industry: retail
cloud:
- aws
patterns:
- ai-agent
- root-cause-analysis
components:
- Amazon Bedrock
- Amazon Bedrock Flows
- Amazon Bedrock AgentCore
- Grafana
- Slack
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-circle-k-accelerated-devops-incident-triage-to-under-15-minutes-with-amazon-bedrock/
published_at: '2026-11-02'
---

## 概要

Circle Kは、アラート発火時に自律的に調査するエージェント型の仕組みをBedrockで構築し、構造化サマリーをSlackに届けるようにした。当初のBedrock Flows実装からAgentCoreへ移行し、平均トリアージ時間を15分未満に短縮、内部指標で67〜75%削減した。

## 設計のポイント

- アラートを起点にログやサービス状態の確認を自動化し、人は調査済みの要約から対応を始める。
- 結果をSlackに構造化して通知し、オンコールの既存の動線に乗せる。
- Flowsで始めてスケール時の課題に応じてAgentCoreへ移行する段階的な進め方を取った。

## 使いどころ

- アラートが多く、初動の調査に毎回時間がかかる運用チーム。
- 複数AWSアカウントを横断して監視している組織。
