---
type: case
title: DevOps Agentの調査結果から承認付き自動修復を行う Durable Functionsワークフロー
title_original: Automate remediation post AWS DevOps Agent investigation
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- root-cause-analysis
- event-driven
- human-in-the-loop
components:
- AWS DevOps Agent
- AWS Lambda Durable Functions
- Amazon EventBridge
- Amazon Bedrock
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/automate-remediation-post-aws-devops-agent-investigation/
published_at: '2026-10-07'
---

## 概要

観測専用で動くAWS DevOps Agentの根本原因分析の完了イベントをEventBridge経由で受け、Lambda Durable FunctionsとBedrockで適用可能な修復策を検証済みの形にまとめる構成を示す。最終的な変更は単一の承認操作で実行でき、MTTR短縮を狙う。

## 設計のポイント

- 調査エージェントは観測のみとし、修復は別ワークフローに分離して本番変更を統制する
- Durable Functionsのチェックポイントと中断機能で、承認待ちを含む長時間処理を状態管理コードなしに実現する
- LLMが修復ツールを選び、事前検証したうえで人の承認を挟む

## 使いどころ

- 夜間オンコールの初動対応を自動化したいSRE/運用チーム
- 自律修復を段階的に導入したい組織
