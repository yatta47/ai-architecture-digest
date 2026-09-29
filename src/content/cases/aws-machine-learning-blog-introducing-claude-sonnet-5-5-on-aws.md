---
type: announcement
title: Claude Sonnet 5.5がAmazon Bedrockで利用可能に
title_original: Introducing Claude Sonnet 5.5 on AWS
company: Anthropic
industry: cross-industry
cloud:
- aws
patterns:
- multi-model-routing
- ai-agent
- cost-optimization
components:
- Claude Sonnet 5.5
- Claude Opus 5.5
- Amazon Bedrock
- Amazon Bedrock Guardrails
- AWS IAM
- AWS CloudTrail
- Amazon CloudWatch
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-claude-sonnet-5-5-on-aws/
published_at: '2026-09-28'
---

## 概要

Claude Sonnet 5.5がAmazon BedrockとClaude Platform on AWSで提供開始された。範囲が明確な作業を低コストかつ高速にこなすモデルで、判断が要る作業はOpus 5.5、方針が定まった実行はSonnet 5.5という使い分けを提案している。

## 設計のポイント

- 判断を要する作業と範囲が明確な作業でモデルを分けて役割分担する。
- 常時稼働の監視やSQL生成のように継続的・大規模な処理に低コストなモデルを充てる。
- IAM・CloudTrail・Guardrailsなど既存のAWS統制の下で利用する。

## 使いどころ

- アラート一次対応や常時監視エージェントを運用するチーム。
- IDE内のコーディング支援を上限予算付きで展開したい組織。
- Opus系とSonnet系の使い分けを設計する担当者。
