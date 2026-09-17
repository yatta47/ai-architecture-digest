---
type: guidance
title: Amazon Quick上のMCPツールに対する多層防御認可
title_original: Implementing defense-in-depth authorization for MCP tools on Amazon Quick
industry: cross-industry
cloud:
- aws
patterns:
- defense-in-depth
- policy-as-code
- guardrails
- llm-gateway
components:
- Amazon Quick
- Amazon Bedrock AgentCore Gateway
- AWS Lambda
- Amazon DynamoDB
- Microsoft Entra ID
- Model Context Protocol (MCP)
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/implementing-defense-in-depth-authorization-for-mcp-tools-on-amazon-quick/
published_at: '2026-09-17'
---

## 概要

Amazon Quick上のMCPツール呼び出しに対し、OIDC/JWTクレームをMFA・地理的制限・グループベースのロール・ツール権限の4ゲートで順に評価するマルチゲート認可パターンを実装する方法を解説する。AgentCore GatewayにアタッチしたLambdaインターセプターが各リクエストをビジネスロジック実行前に検査し、変更操作ごとに監査ログを残すことでコンプライアンス要件を満たす。

## 設計のポイント

- 有効なSSOトークンだけでは『認証済み=認可済み』ではないと捉え、ツール・パラメータ単位の認可レイヤーを別途設ける。
- MFA検証・地理的制限・RBAC・ツール権限の4ゲートを環境変数で個別に有効/無効化できる構成にし、コンプライアンス要件に応じて調整可能にする。
- AgentCore GatewayにアタッチしたLambda REQUESTインターセプターでビジネスロジック実行前にすべてのゲートを評価し、失敗時は403で即座に拒否する。
- 変更を伴う操作は必ず不変の監査レコードを生成し、誰が何をしたかを追跡可能にする。

## 使いどころ

- 金融・医療・行政など、MCP経由で機密データに接続する際に監査可能な粒度のアクセス制御が求められる組織。
- SSO認証だけでは不十分で、ツール・パラメータ単位の権限管理が必要なエージェント基盤。
- 多要素認証や接続元地域の制限など、条件付きアクセスポリシーをエージェントのツール呼び出しにも適用したいケース。
