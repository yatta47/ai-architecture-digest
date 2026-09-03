---
type: case
title: 6エージェント階層構成で個別移行支援計画を作る特別支援教育向けAI「Trinity」
title_original: 'Trinity: Agentic AI-powered transition planning for students with disabilities'
company: University Startups / g/d/n/a
industry: public-sector
cloud:
- aws
patterns:
- multi-agent-orchestration
- rag
- guardrails
- voice-agent
components:
- Amazon Bedrock
- Claude 3.5 Sonnet
- Amazon Bedrock Guardrails
- Amazon API Gateway
- AWS Lambda
- Amazon DynamoDB
- Amazon Polly
- Amazon Transcribe
- Amazon Cognito
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/trinity-agentic-ai-powered-transition-planning-for-students-with-disabilities/
published_at: '2026-09-02'
---

## 概要

障害のある生徒の進路移行計画（IEP）作成を支援する会話型AI「Trinity」が、単一LLMでの構成では検索精度・指導トーン・法令準拠が競合し幻覚が発生した課題を受け、6エージェントの階層構成（オーケストレーター＋5つの専門エージェント）へ再設計した事例。HIPAA/FERPA準拠のサーバーレスアーキテクチャで複数州・複数国への展開を進めている。

## 設計のポイント

- 単一プロンプトに複数ドメイン（受入・進路探索・コンプライアンス・計画作成）を詰め込むと1つの失敗が全体のセッションを壊すため、責務ごとにエージェントを分離する
- 大学・就労・職業訓練など各ドメイン専用のKnowledge Baseを持つ専門エージェントを配置し検索の精度を高める
- 推薦フェーズと計画生成フェーズの2段階パイプラインに分け、選択確定後にオーケストレーターが各エージェントの出力を統合する
- Amazon Bedrock Guardrailsで幻覚低減とコンテンツフィルタリングを行い、HIPAA/FERPA要件に沿ったフィールド単位暗号化とロールベースアクセス制御を基盤から組み込む

## 使いどころ

- 法令に沿った個別教育計画の作成を効率化したい特別支援教育機関
- 音声入出力（Polly/Transcribe）で幅広い障害特性の生徒にアクセシブルなAI対話を提供する場面
- 単一LLMでは精度が不十分な複数ドメインにまたがる推薦業務の再設計
