---
type: guidance
title: エージェント開発ライフサイクル(Agent DLC)：ゴールド基準で本番可否を判断する
title_original: 'From prototype to production: Engineering agents with Agent DLC'
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- eval
- llmops
- ci-cd
- ai-agent
components:
- Agent DLC
- Amazon Bedrock
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/from-prototype-to-production-engineering-agents-with-agent-dlc/
published_at: '2026-11-12'
---

## 概要

エージェントは非決定的で、プロンプトやツール説明の変更が挙動を変え、外部モデルやAPIも独立に変わるため従来のCI/CDだけでは不十分と整理する。検証可能な基準と承認済み例からなる「ゴールド基準」を軸に、2つのループで変更を判定するAgent DLCを提案する。

## 設計のポイント

- 検証可能な基準・閾値・承認例をゴールド基準として束ね、業務オーナーが承認する。
- 集計指標が網羅性の欠落を隠すため、カバレッジ別に評価する。
- 開発ループと運用ループの2つで、すべての変更を同じ基準で判定する。

## 使いどころ

- エージェントの本番リリース判定基準を整備したいチーム。
- プロンプトやモデル更新のたびに回帰評価をしたい運用担当。
- 評価の根拠を業務オーナーに示したい開発リード。
