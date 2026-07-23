---
type: guidance
title: Chat CompletionsからResponses APIへの移行判断基準
title_original: Responses vs. Chat Completions
industry: cross-industry
cloud: []
patterns:
- ai-agent
- cost-optimization
components:
- Responses API
- Chat Completions
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/responses-vs-chat-completions
published_at: '2025-07-21'
---

## 概要

Responses APIはChat Completionsの進化形であり、Web検索・File Search・Computer Use・Code Interpreter・Remote MCPといった組み込みツールと、マルチターンのステートフルな会話管理をネイティブに備えるとして、新規プロジェクトでの採用を推奨する。内部評価ではGPT-5系モデルとの組み合わせでSWE-benchが3%向上し、プロンプトキャッシュの効率改善により40〜80%のコスト削減が確認されている。

## 設計のポイント

- store: trueにより過去の推論・ツール呼び出しコンテキストをターンをまたいで保持できるため、精度とキャッシュ効率が上がる。
- 1回のAPI呼び出し内でモデルが複数の組み込みツールや自作関数を自律的に呼び出すエージェントループがデフォルトで有効になる。
- 既存のChat Completions実装は引き続きサポートされるが、新規実装ではResponses APIを起点に設計する。

## 使いどころ

- これから新規にLLMアプリを設計するチームがAPI選定で悩んでいる場合。
- 複数ツール呼び出しやマルチターンの文脈保持が必要なエージェント的アプリケーション。
