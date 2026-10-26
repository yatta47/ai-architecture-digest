---
type: guidance
title: Bedrock上のOpenAIモデルでエージェントのプロンプトキャッシュを効かせる設計
title_original: 'Groundhog Day for AI agents: Prompt caching patterns for using OpenAI models on Amazon Bedrock'
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- context-engineering
- cost-optimization
- ai-agent
- inference-optimization
components:
- Amazon Bedrock
- OpenAI models on Bedrock
- Responses API
- Model Context Protocol
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/groundhog-day-for-ai-agents-prompt-caching-patterns-for-using-openai-models-on-amazon-bedrock/
published_at: '2026-10-26'
---

## 概要

エージェントは毎ターン、ツール定義・指示・履歴をすべてモデルへ再送するため、ターンが進むほど入力トークン費用が膨らむ。Amazon Bedrock上のOpenAIモデルで、明示(prompt_cache_breakpoint)と暗黙のキャッシュを併用し、静的な接頭辞を再利用するパターンを段階的に解説する。

## 設計のポイント

- ツール定義と指示のような静的部分を先頭に置き、明示ブレークポイントまでをキャッシュして複数セッション・サブエージェントで共有する。
- 日付・ユーザー名・リクエストIDなど変動する値はキャッシュ対象の後ろへ置き、ツール一覧のシリアライズ順も固定して完全一致を保つ。
- 会話履歴の増加部分は暗黙キャッシュに任せ、明示と暗黙を併用して再利用可能な起点と自動管理を両立する。
- prompt_cache_keyで共有対象のリクエストを束ね、TTLを指定して運用する。

## 使いどころ

- コーディングエージェントなど長いセッションで入力トークン費用を抑えたいチーム。
- 同じツール群と指示を共有するサブエージェントを多数起動するマルチエージェント構成。
- Bedrock上でOpenAIモデルを使う本番エージェントのコストと応答性を改善したい場面。
