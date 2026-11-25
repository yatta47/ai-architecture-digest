---
type: guidance
title: Azure Container Apps動的セッションでLLM生成コードを隔離実行する
title_original: Secure code execution in LlamaIndex with Azure Container Apps dynamic sessions
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- guardrails
- defense-in-depth
components:
- Azure Container Apps dynamic sessions
- LlamaIndex
- Azure OpenAI
- ReActAgent
outcome:
  type: risk-compliance
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/secure-code-execution-in-llamaindex-with-azure-container-apps-dynamic-sessions
published_at: '2024-05-21'
---

## 概要

LLMが生成したコードを、Azure Container Appsの動的セッションで隔離実行するLlamaIndexツールの使い方。エージェントに安全なコード実行能力を与える。

## 設計のポイント

- 生成コードの危険性は事前判定に頼らず、ホストから隔離したサンドボックスで実行する。
- セッションプールの管理エンドポイントを介してツールとして接続する。
- 中間データはローカル保存先を指定して回収する。

## 使いどころ

- 計算やデータ処理をコード実行で行うエージェントを作る開発者。
- 生成コード実行の隔離方式を選ぶセキュリティ担当。
