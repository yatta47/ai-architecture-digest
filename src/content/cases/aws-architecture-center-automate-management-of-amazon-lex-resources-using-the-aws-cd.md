---
type: guidance
title: Amazon Lexボットの開発・デプロイをIaCとCI/CDで自動化するワークフロー
title_original: Streamline Amazon Lex bot development and deployment by using an automated workflow
industry: cross-industry
cloud:
- aws
patterns:
- ci-cd
- voice-agent
components:
- Amazon Lex
- AWS CodePipeline
- AWS CloudFormation
- AWS CDK
- AWS CLI
- AWS SDK for Python (Boto3)
- Git
data_sources:
- ボット定義(IaC)
- 会話フロー設定
outcome:
  type: productivity
source_id: aws-architecture-center
source_name: AWS Architecture Center
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/streamline-amazon-lex-bot-development-and-deployment-using-an-automated-workflow.html?did=pg_card&trk=pg_card
published_at: '2024-10-29'
---

## 概要

Amazon Lexの会話ボット開発を、IaC（AWS CDK / CloudFormation）とCodePipelineによるCI/CDで自動化するパターン。開発者はLexコンソールで直感的にボットを構築・テストし、その定義をGitで版管理しながら、開発・テスト・本番の各環境へ段階的にプロモートする。フィーチャー単位に『チケットボット』を分岐して並行開発し、リベース・検証・マージを経てメインボットへ統合することで、機能提供の速度とチーム生産性を高める。

## 設計のポイント

各機能をメインボットのコピーである『チケットボット』として隔離し、エクスポート→メインからのリベース→再インポート検証→PRマージ→チケットボット削除という一連の流れをパイプライン化する設計が再利用可能。ボット定義をLexサービス内に閉じ込めず、Gitで管理して監査証跡と開発者単位の変更追跡を確保する点、および開発・本番・DevOpsを分けたマルチアカウント構成でクロスアカウントのプロモーションを標準化する点が要となる。

## 使いどころ

複数の開発者・機能・環境をまたいでLexボットを継続的に開発・運用するチームに有効で、手作業のバージョン昇格やコンソール依存による属人化・監査性の欠如を解消したい場面で効く。
