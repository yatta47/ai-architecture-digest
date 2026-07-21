---
type: guidance
title: Amazon CognitoとNakamaを繋ぐゲームサーバー向け二重トークン認証基盤
title_original: Dual-token authentication for Nakama game servers with Amazon Cognito on AWS
ai_relevant: false
industry: other
cloud:
- aws
patterns: []
components: []
outcome:
  type: reliability
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/dual-token-authentication-for-nakama-game-servers-with-amazon-cognito-on-aws/
published_at: '2026-06-29'
---

## 概要

ゲームサーバーNakamaにAmazon Cognitoを組み合わせ、プレイヤーIDを管理するCognitoトークンとゲームセッションを管理するNakamaトークンを、互いに独立したまま橋渡しする二重トークン認証パターンを実装した。CloudFrontを単一のHTTPS入口とし、ALBでHTTP APIのルートを許可リスト化、NLBでWebSocketをTCPパススルーするdefault-closedのルーティング層を構築し、認証のためのリダイレクトやゲームプレイの中断を発生させない設計としている。
