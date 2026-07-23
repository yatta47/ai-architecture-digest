---
type: guidance
title: 'OpenAI Agents SDK(Python): マルチエージェントワークフロー構築フレームワーク'
title_original: OpenAI Agents SDK (Python)
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- voice-agent
- guardrails
components:
- OpenAI Agents SDK
- Pydantic
- MCP
outcome:
  type: productivity
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://github.com/openai/openai-agents-python
published_at: '2025-07-18'
---

## 概要

OpenAI Agents SDKは、指示・ツール・ガードレール・ハンドオフを備えたLLMエージェントを軽量に構築できるプロバイダー非依存のPythonフレームワーク。サンドボックスエージェント、テキストエージェント、リアルタイム音声エージェントの3つの実行モードをサポートし、セッション管理やトレーシングが組み込まれている。

## 設計のポイント

- SandboxAgentでファイル操作・コマンド実行・ワークスペース状態の保持が必要な長時間タスクに対応する
- Agents as tools/handoffsパターンで特定タスクを他エージェントに委譲するマルチエージェント構成を組める
- ガードレールで入出力の安全性チェックを設定でき、human in the loopの仕組みも組み込まれている
- 100以上のLLMプロバイダに対応し、OpenAI以外のモデルでも同じフレームワークを使い回せる

## 使いどころ

- 複数の専門エージェントを協調させるワークフローをPythonで構築したい開発者
- ファイル操作を伴う長時間の自律タスクをサンドボックス内で安全に実行したい場合
- 低遅延の音声エージェントを同じフレームワークで一貫して構築したいチーム
