---
type: case
title: レガシー保険基幹システムをAgentCore Browser ToolとStrands Agentsで自動操作する
title_original: Automate legacy web applications with Amazon Bedrock AgentCore Browser Tool
industry: financial-services
cloud:
- aws
patterns:
- ai-agent
- human-in-the-loop
components:
- Amazon Bedrock AgentCore Browser Tool
- Strands Agents
- Amazon Bedrock
- AWS IAM
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/automate-legacy-web-applications-with-amazon-bedrock-agentcore-browser-tool/
published_at: '2026-08-13'
---

## 概要

保険会社の基幹業務システムのようにAPIを持たないレガシーWebアプリを、Amazon Bedrock AgentCore Browser ToolとStrands Agentsで自動操作するリファレンス実装。Playwright経由のCDP接続でブラウザをクラウド上のマネージドChromiumとして提供し、IAMベースのセッション分離と監査証跡で規制業界の要件も満たす。

## 設計のポイント

- PlaywrightのCDP接続でマネージドChromiumを操作し、UI刷新なしに数十年前のレガシー画面をそのまま自動化する
- セッションごとにIAMで隔離し、全操作の監査証跡を残すことでHIPAA/GDPR等の規制要件に対応する
- 単純作業から複雑なマルチステップ承認フローまで、Strands Agentsによるモデル駆動オーケストレーションで段階的にスケールする

## 使いどころ

- 保険・製造・小売・金融など、レガシーな社内システムをRPAで自動化しきれない企業
- MFAや独自SSO、動的なセッショントークンなど従来型RPAが苦手とする認証を伴う業務
