---
type: guidance
title: エージェント型AI向け責任あるAIの段階的ロードマップ
title_original: 'Responsible AI for agentic AI: A phased roadmap for platform and application teams'
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- guardrails
- policy-as-code
- human-in-the-loop
components:
- Amazon Bedrock
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/responsible-ai-for-agentic-ai-a-phased-roadmap-for-platform-and-application-teams/
published_at: '2026-11-17'
---

## 概要

エージェント型AIでは推論・ツール利用・多段の行動により責任あるAIの対象範囲が広がる。基盤チームとアプリチーム向けに、AWS Responsible AI Lensの柱を3段階の成熟度モデルに対応づけた実践的ロードマップを示す。

## 設計のポイント

- 基盤チームがガードレールを整備し、アプリチームがその内側で構築する役割分担にしている。
- ガバナンス基盤→パイロット→拡大の3段階成熟度で取り組みを段階化している。
- 評価をスキル化して再利用可能にしている。

## 使いどころ

- 全社エージェント基盤のガバナンス設計を始める基盤チーム。
- 規制業種でエージェントを本番化するアプリチーム。
