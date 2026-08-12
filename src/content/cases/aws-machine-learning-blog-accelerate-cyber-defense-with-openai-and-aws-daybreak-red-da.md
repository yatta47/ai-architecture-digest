---
type: announcement
title: Bedrock上の専用サイバー防御モデル(Daybreak Red/Blue)
title_original: 'Accelerate cyber defense with OpenAI and AWS: Daybreak Red & Daybreak Blue now available to eligible customers
  on Amazon Bedrock'
company: AWS
industry: other
cloud:
- aws
patterns:
- guardrails
- confidential-computing
components:
- Amazon Bedrock
- GPT-5.6 Cyber
- GPT-5.6 Sol
- AWS KMS
- AWS IAM
- AWS CloudTrail
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/accelerate-cyber-defense-with-openai-and-aws-daybreak-red-daybreak-blue-now-available-to-eligible-customers-on-amazon-bedrock/
published_at: '2026-08-11'
---

## 概要

AWSとOpenAIは、脆弱性研究向けに拒否閾値を下げたDaybreak Red(GPT-5.6 Cyber)と、一般的な防御作業向けのDaybreak Blue(GPT-5.6 Sol)をAmazon Bedrockで提供開始した。ゼロオペレータアクセス(ZOA)やKMS暗号化、IAM/CloudTrailによる統制のもとで動作し、機微なソースコードや脆弱性情報を環境外に出さずに脆弱性の発見から修正までを高速化する。

## 設計のポイント

- 用途に応じて拒否閾値の異なる2モデル(Blue=一般防御、Red=高度な脆弱性研究)を分け、ユースケースの文脈でデュアルユースの曖昧さを解消した。
- Bedrockの次世代推論エンジンでゼロオペレータアクセス(ZOA)をチップレベルで強制し、AWS運用者自身もプロンプト・応答にアクセスできない設計にした。
- IAMポリシー・CloudTrailログ・VPCエンドポイント・KMS暗号化・組織レベルのデータ境界ポリシーを組み合わせ、機微情報が環境外に出ない統制にした。

## 使いどころ

- 自社コードベースの脆弱性調査・エクスプロイト再現・修正開発を、機微情報を外部に出さず加速したいセキュリティチーム。
- 権限のある研究者にのみ低い拒否閾値のモデルアクセスを与え、それ以外には通常の安全側モデルを使わせたいセキュリティ運用者。
- 既存のAWSガバナンス(IAM/KMS/CloudTrail)をそのままAIワークロードにも適用したい規制業界のセキュリティチーム。
