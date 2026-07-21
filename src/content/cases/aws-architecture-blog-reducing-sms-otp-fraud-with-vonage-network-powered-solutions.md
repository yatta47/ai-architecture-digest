---
type: case
title: SMS OTPに代えてモバイル回線網のリアルタイム信号で本人確認するVonageとAmazon Cognitoの不正対策基盤
title_original: Reducing SMS OTP fraud with Vonage network-powered solutions and Amazon Cognito
ai_relevant: false
company: Vonage
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/reducing-sms-otp-fraud-with-vonage-network-powered-solutions-and-amazon-cognito/
published_at: '2026-06-17'
---

## 概要

SMSワンタイムパスコードは認証完了率が約8割にとどまり、SIMスワップやSS7傍受、ソーシャルエンジニアリングによるアカウント乗っ取りにも弱い。VonageはEricsson傘下のモバイル回線事業者ネットワークから得られるリアルタイム信号（SIMスワップ検知、加入者情報照合など）とサイレント認証を組み合わせ、Amazon CognitoのCUSTOM_AUTHフローと統合することで、ユーザー操作なしに5秒未満で本人確認を完結させる仕組みを提供する。
