---
type: case
title: Cornerstone OnDemandのOrion AI：階層型マルチエージェントによるDB診断の自動化
title_original: How Cornerstone OnDemand cut database diagnosis by 78% with Amazon Bedrock
company: Cornerstone OnDemand
industry: cross-industry
cloud:
- aws
patterns:
- multi-agent-orchestration
- ai-agent
- root-cause-analysis
- human-in-the-loop
components:
- Amazon Bedrock
- Strands Agents
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-cornerstone-ondemand-cut-database-diagnosis-by-78-with-amazon-bedrock/
published_at: '2026-10-07'
---

## 概要

CornerstoneはBedrockとStrands Agentsで、メタオーケストレーターが専門の子エージェントに委譲するハブ&スポーク型のOrion AIを構築した。データベース診断が45分から10分へと78%短縮され、3名のチームが6か月で提供した。

## 設計のポイント

- 統括エージェントが監視・診断・ライフサイクル運用などの専門エージェントへ委譲する
- 運用担当者が普段使うWebアプリ上で質問と承認を完結させる
- データプライバシーと既存運用ツールとの統合を設計原則にする

## 使いどころ

- DBやインフラ運用の障害対応を効率化したいDataOps/SREチーム
- 重複アラートと手作業の調整を減らしたい場面
