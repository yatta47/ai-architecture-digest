---
type: guidance
title: CognitoユーザーIDでQuickSightビジュアルをReactに個別埋め込みする構成
title_original: Embed Quick Sight visuals using Cognito user authentication
ai_relevant: false
company: AWS
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/embed-quick-sight-visuals-using-cognito-user-authentication/
published_at: '2026-09-03'
---

## 概要

Amazon CognitoでユーザーごとのJWT認証を行い、Amazon QuickSightのビジュアルをReactアプリにビジュアル単位で埋め込むサーバーレス構成を解説する記事。Lambdaがユーザー同期と権限付きの埋め込みURL生成を担う4層アーキテクチャを紹介する。
