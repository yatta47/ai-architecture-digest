---
type: announcement
title: BedrockのClaudeで構造化出力が全モデルに対応
title_original: Structured outputs for Anthropic Claude models on Amazon Bedrock
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- guardrails
- document-processing
- ai-agent
components:
- Amazon Bedrock
- Anthropic Claude
- Boto3
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/structured-outputs-for-anthropic-claude-models-on-amazon-bedrock/
published_at: '2026-10-19'
---

## 概要

Amazon Bedrockが全Claudeモデルで構造化出力に対応し、bedrock-runtimeとbedrock-mantleの両エンドポイントでスキーマ準拠のJSONを得られる。制約付きデコーディングで生成時にスキーマを強制するため、独自パースやリトライが不要になる。

## 設計のポイント

- 制約付きデコーディングでスキーマ違反のトークンを生成させず、出力形式を確率的から決定的にする。
- JSONスキーマ出力とstrictなツール利用を併用し、エージェントのパラメータも検証する。

## 使いどころ

- 決算書や契約書、臨床記録などから必須項目を確実に抽出する処理。
- サポートチケットの意図・感情・エンティティをデータモデルに沿って振り分ける場面。
