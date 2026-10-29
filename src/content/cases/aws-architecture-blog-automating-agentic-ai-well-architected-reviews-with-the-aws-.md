---
type: case
title: 'Smarsh: Agentic AI LensのレビューをClaudeスキルで自動化'
title_original: Automating agentic AI Well-Architected reviews with the AWS Agentic AI Lens
company: Smarsh
industry: financial-services
cloud:
- aws
patterns:
- ai-agent
- eval
- policy-as-code
components:
- Claude
- Amazon Bedrock AgentCore
- AWS Well-Architected Framework
- GitHub
outcome:
  type: speed
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/automating-agentic-ai-well-architected-reviews-with-the-aws-agentic-ai-lens/
published_at: '2026-10-28'
---

## 概要

コミュニケーション・アーカイブ事業のSmarshは、AWS Well-ArchitectedのAgentic AI Lensの150のベストプラクティスを評価するClaudeスキルを自作した。GitHubリポジトリから証拠を集め、レビューのワークブックを数日ではなく数時間で作成する。

## 設計のポイント

- レンズをそのまま読むだけでなく、実行可能なスキルにしてリポジトリの証拠に基づく評価にする。
- 評価対象の全ベストプラクティスを網羅し、結果をワークブックにまとめる。
- スキル自体も検証し、結果をAWSアカウントチームとの議論に使う。

## 使いどころ

- 規制業種で、エージェント基盤を顧客提供前にレビューする必要がある組織。
- Well-Architectedレビューの工数を減らしたいアーキテクト。
