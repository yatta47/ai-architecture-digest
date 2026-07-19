---
type: case
title: ScienceSoftのHIPAA準拠AI音声予約スケジューラ
title_original: ScienceSoft's HIPAA-compliant AI voice scheduler built on AWS
company: ScienceSoft
industry: healthcare
cloud:
- aws
patterns:
- voice-agent
- guardrails
- defense-in-depth
components:
- Amazon Nova Sonic
- Amazon Bedrock Guardrails
- Amazon Chime SDK
- Amazon ECS
- AWS Fargate
- AWS Secrets Manager
- AWS Security Hub
- AWS CloudTrail
- Amazon CloudWatch
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/sciencesofts-hipaa-compliant-ai-voice-scheduler-built-on-aws/
published_at: '2026-07-14'
---

## 概要

ScienceSoftはAmazon Nova SonicとAmazon Bedrock Guardrailsを組み合わせ、HIPAA準拠のAI音声予約アシスタントを構築。患者の電話予約対応を自動化しつつ、プライバシー・コンプライアンス・偏りのない対応を担保する。

## 設計のポイント

- HIPAA準拠のVPC内で音声処理からEHR/CRM連携まで完結させ、オンプレシステムとはVPN経由で連携する。
- Bedrock Guardrailsを全会話のリアルタイムフィルタとして機能させ、話題制限・PIIマスキング・医療助言の禁止を透過的に強制する。
- Nova SonicのSpeech-to-Speech処理をコンテナ化しECS/Fargateで水平スケールさせ、高コール量に対応する。

## 使いどころ

- 電話予約対応の人員コストとコール放棄率(約30%)を削減したい医療機関。
- 患者データを扱う音声AIでコンプライアンスと信頼性を両立したい組織。
