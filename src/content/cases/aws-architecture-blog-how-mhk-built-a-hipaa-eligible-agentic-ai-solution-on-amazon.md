---
type: case
title: MHKのHIPAA対応マルチテナント型エージェントワークフロー基盤
title_original: How MHK built a HIPAA-eligible agentic AI solution on Amazon Bedrock
company: MHK (Hearst Health)
industry: healthcare
cloud:
- aws
patterns:
- multi-agent-orchestration
- document-processing
- event-driven
- guardrails
components:
- Amazon Bedrock
- Amazon ECS
- AWS Fargate
- Spring Boot
- SmartProminence AI Orchestrator
outcome:
  type: productivity
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/how-mhk-built-a-hipaa-eligible-agentic-ai-solution-on-amazon-bedrock/
published_at: '2026-09-30'
---

## 概要

MHKは、医療文書処理のAIを用途ごとに作る負担を避けるため、設定で複数ワークフローを展開できるマルチテナントのSmartProminence AI Orchestratorを構築した。Amazon Bedrockでモデル推論を行い、オーケストレーション、検索、HIPAA固有の検証は自前で持つ。手作業レビューを90%削減し、新機能の展開が3か月以上から2週間になった。

## 設計のポイント

- ワークフロー制御を担うコントローラーとLLM処理エージェントを分離し、エージェント側を独立にスケールさせる。
- バージョン固定のワークフロー定義をDAGに解決し、条件式で実行ステップを決める。
- DBアクセスをオーケストレーションコアのAPIに限定し、データアクセス境界を強制する。
- Bedrockはモデルアクセスに限定し、ドメイン固有の検証は自前層で制御する。

## 使いどころ

- 事前承認、請求、異議申立など複数の医療業務で文書判定を自動化したい保険者向けSaaS。
- 用途ごとのコンプライアンス審査やインフラ構築を繰り返したくない規制業界の基盤チーム。
- プロンプトとスキーマ定義の登録でAI機能を素早く追加したい場面。
