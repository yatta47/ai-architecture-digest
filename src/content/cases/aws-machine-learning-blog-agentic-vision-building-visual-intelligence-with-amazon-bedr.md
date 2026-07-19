---
type: guidance
title: MCPで画像認識・生成AI・エージェントを1つのインターフェースに統合
title_original: 'Agentic vision: Building visual intelligence with Amazon Bedrock and MCP servers'
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- video-intelligence
- llm-gateway
components:
- Amazon Bedrock
- Strands Agents
- Amazon Rekognition
- Amazon OpenSearch
- Model Context Protocol (MCP)
- Amazon S3
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/agentic-vision-building-visual-intelligence-with-amazon-bedrock-and-mcp-servers/
published_at: '2026-07-15'
---

## 概要

Computer Vision・Strands Agents・Model Context Protocol（MCP）の3技術を組み合わせ、画像・動画のアップロードから物体検出・切り出し・説明生成までをMCPサーバー経由の標準化されたインターフェースで扱えるComputer Vision MCP Serverを紹介する。AIモデルごと・データソースごとに個別の連携を作る複雑さを、MCPという単一プロトコルに集約することで解消する。

## 設計のポイント

- 画像認識（Amazon Rekognition）、生成AI（Amazon Bedrock）、検索（OpenSearch）をそれぞれ独立したMCPサーバーのツールとして公開し、エージェント側は標準プロトコルだけを意識すればよい構成にする。
- IAMロールを中心としたセキュリティゲートウェイに権限管理を集中させ、クライアント側に個別の認証情報を埋め込まない。
- システムプロンプトでツールの利用パターン（切り出し→表示など）を明示し、単一エージェントが複数のCVツールを目的に応じて連鎖的に呼び出せるようにする。

## 使いどころ

- 複数のコンピュータビジョンAPIを個別に統合する手間を減らし、標準化されたインターフェースで扱いたい開発チーム。
- 画像・動画のアップロードから自然言語での質問応答まで一貫したチャットUIを提供したいアプリケーション。
- 視覚情報の認識結果をもとに、生成AIが推論・アクションまで行うマルチモーダルエージェントを構築したいケース。
