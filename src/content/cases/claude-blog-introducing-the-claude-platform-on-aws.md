---
type: announcement
title: AWS経由でフル機能のClaude Platformを利用できる新提供形態
title_original: Introducing the Claude Platform on AWS
company: Anthropic
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- llmops
- llm-gateway
components:
- Claude Platform
- AWS IAM
- AWS CloudTrail
- Claude Managed Agents
- Amazon Bedrock
- Claude Console
- MCP connector
- Claude Opus 4.7
- Claude Sonnet 4.6
- Claude Haiku 4.5
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-platform-on-aws
published_at: '2026-05-11'
---

## 概要

AnthropicはAWS上でネイティブAPIと同等の全機能を提供する「Claude Platform on AWS」を一般提供開始した。認証はAWS IAM、監査ログはCloudTrail、請求は既存のAWSコミットメントに充当できる単一請求書で行われ、Claude Managed AgentsやMCPコネクタなどの最新ベータ機能もネイティブAPIと同日にリリースされる。データ処理主体をAWS境界内に留めたい場合はAmazon Bedrock、フル機能とAWS運用モデルの両立を求める場合はClaude Platform on AWSという使い分けが提示されている。

## 設計のポイント

- AWS IAMによる認証とCloudTrailによる監査ログ統合で、既存のAWS運用・権限管理の枠組みをそのまま利用できるようにした
- 課金をAWSの単一請求書に一本化し、既存のAWSコミットメントに全額充当できるようにした
- 新機能・ベータ機能をネイティブClaude APIと同日にリリースすることで機能パリティを維持する設計とした
- データ処理主体（Anthropic運用かAWS運用か）によってClaude Platform on AWSとAmazon Bedrockを使い分けられるようにした

## 使いどころ

- AWSの調達・IAM権限・請求の仕組みを維持したまま最新のClaude API機能をフルに使いたいAWSヘビーユーザー企業
- エージェント基盤（Claude Managed Agents）やMCP接続などを本番規模でAWS上に構築したいチーム
- 厳格なリージョンデータ常在要件がありAWS境界内でのデータ処理が必須の企業は、代わりにAmazon Bedrockを選択する
