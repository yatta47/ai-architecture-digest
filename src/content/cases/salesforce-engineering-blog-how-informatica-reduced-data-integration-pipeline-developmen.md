---
type: case
title: 自然言語でデータ統合パイプラインを生成するInformatica CoPilot
title_original: How Informatica Reduced Data Integration Pipeline Development From Days to Minutes
company: Informatica
industry: cross-industry
cloud: []
patterns:
- llmops
- fine-tuning
- context-engineering
- guardrails
components:
- OpenAI
- Snowflake
- Salesforce
outcome:
  type: speed
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/how-informatica-reduced-data-integration-pipeline-development-from-days-to-minutes/
published_at: '2026-07-09'
---

## 概要

Informaticaは自然言語でデータ統合パイプラインを生成するCoPilotを開発し、従来は数日から数週間かかっていたパイプライン開発を数分に短縮した。当初は自前でファインチューニングしたモデルを使用していたが、OpenAIモデルの精度が上回るようになり移行し、プロンプトエンジニアリング・グラウンディング・出力検証を組み合わせて信頼性を担保した。公開後、顧客は約1万件のパイプラインと2万5千件以上の式生成リクエストを生成し、生成結果の受け入れ率は約60〜80%に達した。

## 設計のポイント

- 自前のファインチューニング済みモデルから、精度で上回るOpenAIの汎用モデルへ段階的に移行した
- モデルの挙動を直接制御できない分、プロンプトエンジニアリングとグラウンディングでスキーマやメタデータの文脈を補って精度を担保した
- 生成が確率的であるため単一ケースの検証ではなく、リグレッションを防ぐための広いテストカバレッジで検証プロセスを再設計した
- 生成された式やオブジェクト名は人手による確認・修正を前提とし、既存パイプラインへの変換の追加挿入にも対応した

## 使いどころ

- スキーマやフィールドマッピングの専門知識がなくても自然言語の指示でETL/データ統合パイプラインを組みたい業務ユーザー
- Snowflake・Salesforceなど複数システム間のデータ移動・変換の開発期間を数日から数分へ短縮したい統合エンジニアリングチーム
- 既存パイプラインに変換ロジックを会話的な指示で追加・拡張したい場合
