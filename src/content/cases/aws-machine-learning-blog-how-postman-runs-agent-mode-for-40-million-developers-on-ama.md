---
type: case
title: 4,000万開発者向けPostman Agent Modeのツール絞り込みとBedrock運用
title_original: How Postman runs Agent Mode for 40 million developers on Amazon Bedrock
company: Postman
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- context-engineering
- guardrails
- human-in-the-loop
- cost-optimization
components:
- Amazon Bedrock
- Amazon Bedrock Guardrails
- ClickHouse
- Postman Agent Mode
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-postman-runs-agent-mode-for-40-million-developers-on-amazon-bedrock/
published_at: '2026-10-09'
---

## 概要

PostmanはAPI開発プラットフォームにAgent Modeを組み込み、Amazon Bedrock上で4,000万人規模に提供している。ツールが40個を超えると選択ミスが増えるため、ツール埋め込みのベクトル検索で170超を約15に絞りサブエージェントに渡す設計に至った。

## 設計のポイント

- ツールカタログもコンテキスト予算とみなし、ベクトルDBでタスクごとに関連ツールだけを動的に公開する。
- 細かいツールを増やす代わりに、スキーマを渡してSQLを生成させる単一クエリツールに集約する。
- ツールをUIの開閉状態から切り離し、データに対して直接操作できるようにする。
- 状態を変更する操作はユーザー承認を必須にし、GuardrailsでPIIをLLM到達前にマスクする。

## 使いどころ

- 既存の成熟した製品にエージェントを後付けする開発チーム。
- ツール数が増えて選択精度が落ちているエージェント運用者。
- クロスリージョン推論やゼロデータ保持を要件とする企業。
