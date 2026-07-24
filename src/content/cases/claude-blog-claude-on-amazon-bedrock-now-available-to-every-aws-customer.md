---
type: announcement
title: Claude、Amazon Bedrockで全AWS顧客への提供開始と投資分析アシスタント事例
title_original: Claude on Amazon Bedrock now available to every AWS customer
company: Bridgewater Associates
industry: financial-services
cloud:
- aws
patterns:
- ai-agent
- human-in-the-loop
components:
- Amazon Bedrock
- AWS Lambda
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/amazon-bedrock-general-availability
published_at: '2023-09-28'
---

## 概要

AnthropicはClaudeをAmazon Bedrockで全AWS顧客に一般提供開始し、Lambda関数と連携してタスクを分解・実行するAgents for Amazon Bedrock(プレビュー)も紹介。資産運用会社Bridgewater Associatesは、基本的な指示からPythonコードを生成しグラフや表を作成する投資アナリスト向けアシスタントを構築し、不確実な場合は実行前に確認質問を行う設計にしている。

## 設計のポイント

- エージェントが複雑なタスクをステップに分解し、必要に応じて追加のヒアリングを行う
- コード生成後もアナリストがその場で編集できるようにし人とAIの役割分担を柔軟にする
- 不確実性が高い場合は実行前に確認質問を挟むガードレールを組み込む

## 使いどころ

- 反復的な仮説検証やデータ可視化を伴う金融分析業務の効率化
- コードを書きながら試行錯誤するジュニアアナリスト業務の下支え
