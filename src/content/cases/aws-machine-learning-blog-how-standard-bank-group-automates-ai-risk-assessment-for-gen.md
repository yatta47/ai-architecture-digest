---
type: case
title: スタンダードバンクの生成AIリスク評価の自動化
title_original: How Standard Bank Group automates AI risk assessment for generative AI
company: Standard Bank Group
industry: financial-services
cloud:
- aws
patterns:
- eval
- guardrails
- policy-as-code
- human-in-the-loop
components:
- Amazon Bedrock
- AWS Step Functions
- Amazon S3
- AWS Well-Architected Tool
- AWS IAM
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-standard-bank-group-automates-ai-risk-assessment-for-generative-ai/
published_at: '2026-11-20'
---

## 概要

スタンダードバンクは、生成AIユースケースを国際標準と自社方針に照らして採点する評価を自動化した。証拠収集とテストをAWS上で自動化し、結果を既存の承認ゲートに入力する。

## 設計のポイント

- 新しい方針を作らず、既存のモデルリスク管理と変更リスクの承認プロセスに自動評価を接続する。
- Step Functionsで取り込みから評価、レポートまでを統制し、Bedrock上のLLM-as-a-judgeが証拠を基準と照合する。
- 文書やテスト結果は自社アカウントのS3内に留め、最終承認はリスク委員会が行う。

## 使いどころ

- 生成AIユースケースの審査待ちを短縮したいとき。
- 金融などの規制業種でAIガバナンスの証拠を一貫して集めたいとき。
- 委員会判断を同じ形式の証拠で行いたいとき。
