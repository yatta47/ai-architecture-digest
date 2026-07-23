---
type: guidance
title: Ollamaでgpt-oss-20b/120bをローカル実行し、Agents SDKとも連携する手順
title_original: How to run gpt-oss locally with Ollama
industry: cross-industry
cloud:
- on-prem
patterns:
- inference-optimization
- ai-agent
components:
- gpt-oss-20b
- gpt-oss-120b
- Ollama
- Agents SDK
outcome:
  type: cost
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/cookbook/articles/gpt-oss/run-locally-ollama/
published_at: '2025-08-05'
---

## 概要

コンシューマー向けPCやMacでgpt-oss-20b/120bをOllama経由でローカル実行するための手順を解説する。オフラインチャット、OpenAI互換API経由の呼び出し、Agents SDKとの連携までをカバーする。

## 設計のポイント

- MXFP4量子化済みモデルをそのまま配布し、追加の量子化作業なしにコンシューマーハードウェアで動かせるようにする
- OpenAI互換のChat Completions APIを公開することで、既存のOpenAI向けクライアントコードをほぼそのまま流用できるようにする

## 使いどころ

- オフラインまたはプライベートな環境でLLMを試したい個人・小規模チーム
- 既存のOpenAI向けエージェントコードをローカルモデルに切り替えて検証したい開発者
