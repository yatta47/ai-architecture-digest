---
type: case
title: DiDiのAmazon Bedrockによるコンタクトセンター品質管理AI
title_original: How DiDi built intelligent contact center QA with Amazon Bedrock
company: DiDi
industry: cross-industry
cloud:
- aws
patterns:
- eval
- guardrails
- context-engineering
components:
- Amazon Bedrock
- Amazon Bedrock Guardrails
- Amazon VPC
- AWS PrivateLink
- AWS IAM
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-didi-built-intelligent-contact-center-qa-with-amazon-bedrock/
published_at: '2026-09-08'
---

## 概要

DiDi International Business GroupがAWSと共同で、不透明なサードパーティQAソリューションから、Amazon Bedrock上の自前で透明性のあるコンタクトセンターQAシステムに移行した。意図検証・コンプライアンス評価・VOC分析の3パイプラインを構築し、各LLM呼び出しに渡す情報を厳密に絞る精密なコンテキスト管理により、意図検証精度を38%から86%に改善した。

## 設計のポイント

- 各LLM呼び出しに渡す情報を必要最小限に絞る「precise context management」を精度向上の中心原則とする
- Bedrock GuardrailsでPIIマスキングとグラウンディングチェックを行い、ハルシネーション判定を抑制する
- ルールで判定可能な項目はLLM判定後にプログラムによる後検証層で生の会話に対して再チェックする

## 使いどころ

- 複数言語・複数事業ラインでQAルールが乱立し保守コストが増大しているコンタクトセンター
- サードパーティQAツールの判断根拠が不透明で監査証跡を残したい企業
