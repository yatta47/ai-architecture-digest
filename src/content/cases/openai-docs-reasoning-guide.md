---
type: guidance
title: 推論トークンで多段階タスクを解くGPT-5.5/5.6系モデルの使い方
title_original: Reasoning models
industry: cross-industry
cloud: []
patterns:
- reasoning-computation-separation
components:
- GPT-5.5
- gpt-5.6
- Responses API
- Codex CLI
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/reasoning?api-mode=responses
published_at: '2025-08-03'
---

## 概要

応答生成前に内部で推論トークンを消費するGPT-5.5系の推論モデルの使い方を解説する。複雑な問題解決・コーディング・科学的推論・多段階エージェントワークフローに適しており、Responses APIとの組み合わせで最も高い性能を発揮するとしている。

## 設計のポイント

- コストとレイテンシの要件に応じてgpt-5.6-sol/terra/lunaのように推論モデルの階層を使い分ける
- Chat CompletionsではなくResponses APIを使うことで、推論モデル本来の性能を引き出す
- reasoning effortパラメータで推論の深さとレイテンシのトレードオフを明示的に制御する

## 使いどころ

- 複雑なコーディング・多段階の意思決定を要するエージェントを構築したい開発者
- Codex CLIのような軽量コーディングエージェントの基盤モデルを選定したいチーム
