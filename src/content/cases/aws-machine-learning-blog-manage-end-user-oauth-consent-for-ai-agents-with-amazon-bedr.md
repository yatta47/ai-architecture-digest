---
type: guidance
title: AgentCore IdentityのConsentポータルでエージェントのOAuth同意とセッションバインディングを管理
title_original: Manage end-user OAuth consent for AI agents with Amazon Bedrock AgentCore
industry: cross-industry
cloud:
- aws
patterns:
- agent-identity
- ai-agent
components:
- Amazon Bedrock AgentCore
- AgentCore Identity
- AgentCore Gateway
- GitHub
- Slack
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/manage-end-user-oauth-consent-for-ai-agents-with-amazon-bedrock-agentcore/
published_at: '2026-09-14'
---

## 概要

Amazon Bedrock AgentCore IdentityにConsentポータル機能が追加され、エージェントがユーザーに代わってGitHubやSlackなどの外部サービスにアクセスする際のOAuth同意取得とセッションバインディングをマネージドに提供。従来は認可URL提示・コールバックホスティング・セッション管理を自前で構築する必要があった。

## 設計のポイント

- 企業のIdPで認証したユーザーが個別プロバイダ(GitHub/Slack等)へのアクセスを都度同意し、トークンはAgentCore Identityのトークンボールトに安全に保管される
- IDE/MCPクライアント(Kiro, Claude Code, Cursor, VS Code)からの利用を想定し、一度同意すれば以降のツール呼び出しは保存済みトークンを再利用する
- 管理者はIAMポリシーでポータルリソースの作成権限を最小化し、実行ロールを分離する

## 使いどころ

- AIコーディングアシスタントなどのエージェントにユーザー個別の権限でGitHub/Slack等へのアクセスを許可したい開発者体験チーム
- 独自のセッションバインディング基盤を構築したくない組織
