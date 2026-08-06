---
type: case
title: 自動運転データパイプラインの定型問い合わせをAgentCoreのAIサポートエージェントが90%高速化
title_original: How Mobileye transformed support operations using Amazon Bedrock AgentCore
company: Mobileye
industry: manufacturing
cloud:
- aws
patterns:
- ai-agent
- llm-gateway
components:
- Amazon Bedrock AgentCore
- Amazon Bedrock AgentCore Runtime
- Amazon Bedrock AgentCore Observability
- AWS Secrets Manager
- Model Context Protocol
- Anthropic Claude
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-mobileye-transformed-support-operations-using-amazon-bedrock-agentcore/
published_at: '2026-08-05'
---

## 概要

自動運転向けチップを手がけるMobileyeは、1日数千件のドライブ記録セッションに関する定型的な状況確認問い合わせ（従来15クリック超の手作業）を、Amazon Bedrock AgentCore上のAIサポートエージェントに置き換えた。社内LLM GatewayとMCP経由でオンプレの処理基盤に実時間アクセスし、応答時間を90%短縮・分類精度95%超を達成、その後は全社向けのセルフサービスAgentCore基盤へと発展させた。

## 設計のポイント

- 静的なスクリプトやルールベースの決定木では対応しきれない問い合わせパターンの多様性に対し、文脈理解ができるAIエージェントを選ぶ判断基準を明確にする
- MCPでエージェントに社内処理基盤のAPIへのリアルタイムアクセスを与え、単なる分類器ではなく状態を調査する『調査官』として機能させる
- オンプレのチケットシステムとAWS側のエージェント実行環境を、ローカルオーケストレーターを介したハイブリッド構成で橋渡しし、既存システムを移行せずに統合する
- AgentCore Observabilityでツール呼び出しを含むエージェントの推論過程をエンドツーエンドで追跡し、デバッグと反復のサイクルを短縮する

## 使いどころ

- 多システムを横断する定型的な状況確認業務に、熟練エンジニアの工数が奪われている運用チームとして
- オンプレの基幹システムとクラウド上のAIエージェントを、セキュリティ・コンプライアンスを崩さず統合したい場合として
- 1つのユースケースで得た知見をもとに、全社向けセルフサービスのエージェント基盤へ展開していきたい組織として
