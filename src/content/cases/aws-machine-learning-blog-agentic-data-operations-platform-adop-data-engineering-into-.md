---
type: guidance
title: エージェント型データ運用基盤(ADOP)でデータ取り込みを時間単位に短縮
title_original: 'Agentic Data Operations Platform (ADOP): Data engineering into hours'
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- multi-agent-orchestration
- ci-cd
- policy-as-code
components:
- Amazon Bedrock
- AWS Glue
- Claude Code
- AWS Step Functions
- Amazon CloudWatch
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/agentic-data-operations-platform-adop-data-engineering-into-hours/
published_at: '2026-08-21'
---

## 概要

AWSが提唱するADOPは、データオンボーディングをAIエージェントに担わせつつ、生成物はCI/CDでデプロイする『開発はエージェント、本番は決定的アーティファクト』という設計を採る。ETL・品質チェック・意味レイヤ定義・コンプライアンス制御をサブエージェントが分担し、数週間かかる新規データソース接続を数時間に短縮する。

## 設計のポイント

- 本番実行時にはLLMを呼ばず、エージェントが生成したPySpark/SQL/Airflow DAG等の決定的アーティファクトのみを動かすことで監査性とコストの予測可能性を確保する
- 組織の設計標準を『Decision Engine』としてエージェントに埋め込み、汎用コーディングツールで生じがちなアーキテクチャのばらつきを抑える
- Cedarベースの認可ポリシーとツールルーティングルールでサブエージェントの権限を制約するガードレール層を設ける
- 全エージェント判断をAgentTraceで意図・使用ツール・結果・コストまでトレースし、CloudWatchやOpenTelemetryへ出力して監査可能にする

## 使いどころ

- データエンジニアリングチームが新規データソースのオンボーディングに数週間かかっている場合の高速化
- 規制業種でコンプライアンス確認を後工程のゲートではなく取り込み時のインラインな制御にしたい場合
- Claude Code・Kiro・Cursor・Codexなど複数のAIコーディングツールを同じアーキテクチャ規約の下で使わせたい基盤チーム
