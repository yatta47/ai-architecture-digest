---
type: case
title: Intuitのエージェント型災害復旧アシスタントEWOK Agent
title_original: How Intuit built an agentic disaster recovery assistant with Amazon Bedrock
company: Intuit
industry: financial-services
cloud:
- aws
patterns:
- ai-agent
- disaster-recovery
- decision-execution
components:
- Amazon Bedrock
- Amazon Bedrock Guardrails
- Amazon Bedrock Converse API
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-intuit-built-an-agentic-disaster-recovery-assistant-with-amazon-bedrock/
published_at: '2026-09-04'
---

## 概要

Intuitは数千のマイクロサービスにまたがる災害復旧のフェイルオーバー可否判断が熟練エンジニアの暗黙知に依存していた課題に対し、Amazon Bedrock上に構築したEWOK Agentが自然言語のリクエストを解釈し、既存の実行基盤EWOKに対して検証済みでポリシーに沿った復旧実行を指示するエージェントを構築し、8か月運用している。

## 設計のポイント

- モデルが何をすべきか判断し、決定論的なEWOKがどう実行するかを担うという境界を明確に分離する
- 復旧知識をタイプ付きの「スキル」としてコード化し、Bedrock Converse APIのツール呼び出しでスキルをツールにコンパイルする薄いレイヤーを挟む
- Amazon Bedrock Guardrailsとデータの非学習利用・暗号化を組み合わせ、本番の金融システムを操作するエージェントに必要な安全策を確保する

## 使いどころ

- 数千のマイクロサービスにまたがる複雑なフェイルオーバー判断をオンコールエンジニアの暗黙知に頼らず標準化したい組織
- チェンジフリーズ期間中の例外処理などエッジケース対応の判断をエージェントに任せつつ実行は既存の決定論的システムに委ねたい場合
