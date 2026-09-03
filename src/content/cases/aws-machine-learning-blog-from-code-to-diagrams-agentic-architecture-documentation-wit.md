---
type: case
title: AgentCoreで.NETコードベースからアーキ図を自動生成しRAGで検索可能にする文書化パイプライン
title_original: 'From code to diagrams: Agentic architecture documentation with Amazon Bedrock AgentCore'
company: グローバルインターディーラーブローカー（金融サービス企業）
industry: financial-services
cloud:
- aws
patterns:
- ai-agent
- ci-cd
- rag
- document-processing
components:
- Amazon Bedrock AgentCore
- AWS CodePipeline
- AWS CodeCommit
- AWS CodeBuild
- Amazon Bedrock Knowledge Bases
- Amazon S3
- Amazon Titan Text Embeddings
- Strands Agents
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/from-code-to-diagrams-agentic-architecture-documentation-with-amazon-bedrock-agentcore/
published_at: '2026-09-02'
---

## 概要

電子取引プラットフォームを持つ大手インターディーラーブローカーが、AgentCore上の自律エージェントでコードコミットのたびにアーキテクチャ図（Mermaid/SVG）を自動生成し、Bedrock Knowledge Basesに取り込んで自然言語で検索可能にするCI/CD連携パイプラインを構築した事例。2026年第1四半期から本番稼働している。

## 設計のポイント

- CodeCommitへのプッシュを起点にCodePipeline/CodeBuildからAgentCoreのStrandsエージェントを呼び出し、コード変更のたびにドキュメントを自動更新する
- エージェントが図の構文検証と自己修正を繰り返す反復的リファインメントでSVG変換までを自動化する
- 生成した図のメタデータとMermaidソースをTitan Embeddingsでベクトル化しKnowledge Basesに取り込み自然言語質問に対応する
- マイクロサービス間の依存関係をドキュメント化し、コンプライアンス監査やオンボーディング時の知識断絶を防ぐ

## 使いどころ

- コードベースの変化にドキュメントが追従できず陳腐化しているレガシー資産の可視化
- セキュリティレビューや監査で最新のアーキ図が求められる規制業界
- 新規参入エンジニアがリバースエンジニアリングに時間を費やしているオンボーディング課題
