---
type: case
title: ハッカソンで生成AIをアイデアから本番実装へ加速させたDHI Groupの採用募集プラットフォーム統合
title_original: How DHI Group accelerates generative AI workloads from idea to production using hackathons
company: DHI Group
industry: other
cloud:
- aws
patterns:
- ai-agent
- multi-agent-orchestration
- llm-gateway
- memory-consolidation
components:
- Amazon Bedrock AgentCore
- AWS Lambda
- Amazon OpenSearch Service
- Amazon Bedrock
- Model Context Protocol (MCP)
- AWS IAM
- Amazon VPC
- NAT Gateway
- Strands
- Kiro
outcome:
  type: productivity
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/how-dhi-group-accelerates-generative-ai-workloads-from-idea-to-production-using-hackathons/
published_at: '2026-09-17'
---

## 概要

採用サービス企業DHI GroupはAWSと共同で「Hackathon Acceleration Package」という研修＋3日間ハッカソンの枠組みを実施し、生成AIのPoCが量産で終わる課題を克服して本番投入までを加速した。優勝チームはClearanceJobsとAgileATSを統合するエージェント型システムを構築し、Amazon Bedrock AgentCoreが提供するエージェントランタイムとMCPゲートウェイを介してAWS Lambda上のMCPサーバーをツールとして呼び出し、候補者検索やGitHubプロフィール補強を自然言語の会話フローで自動化した。

## 設計のポイント

- MCPでシステムの機能を離散的なツールとして公開し、エージェントに発見・呼び出しさせる
- AgentCore GatewayでIAM認証付きのツール検出・ルーティングを一元化する
- セッションメモリで複数ステップにまたがる文脈と選好を保持し、対話的なオーケストレーションを実現する
- 研修とハッカソンをセットにしたHAP形式で技術検証と組織のAIリテラシー向上を同時に進める

## 使いどころ

- 複数システムにまたがる情報を自然言語で横断検索・操作したいリクルーター向けインターフェース
- PoCが量産で終わりがちな組織が、技術検証と実装スキル習得を同時に進めたい場面
- レガシーな複数システムをエージェント層で統合し単一の対話インターフェースにまとめたいケース
