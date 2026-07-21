---
type: guidance
title: ミドルウェアで組み立てるカスタムAIエージェントハーネス
title_original: How to Build a Custom Agent Harness
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- multi-agent-orchestration
- human-in-the-loop
components:
- LangChain create_agent
- Deep Agents
- Claude Agent SDK
- SummarizationMiddleware
- SubAgentMiddleware
- HumanInTheLoopMiddleware
- PromptCachingMiddleware
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-to-build-a-custom-agent-harness
published_at: '2026-06-04'
---

## 概要

LangChainは、モデルとツール呼び出しループを最小限だけ実装したcreate_agentを土台に、ミドルウェアという単位でメモリ管理・ツール管理・ガードレール・人間介入などをエージェントループの各フックに差し込む設計思想を提示している。Deep AgentsやClaude Agent SDKのような既製の重量級ハーネスでは対応しきれない業務固有のロジックやポリシーを、独立したミドルウェアとして組み合わせることでタスクに合った「ハーネス」を柔軟に構築できる点を強調する。

## 設計のポイント

- コアのエージェントループは最小限に保ち、要約・メモリ・ツール管理・状態拡張・ストリーム処理などの機能はすべてミドルウェアとして疎結合に追加できるようにする。
- ミドルウェアはモデル呼び出しの前後・ツール呼び出しの前後・起動/終了の各フックに対応させ、決定的ロジックとプロンプトに書くべきでない制御（ポリシー適用や人間承認ゲートなど）を分離する。
- ミドルウェア単位を組織内で共有可能な部品にすることで、新しいエージェントも実績のある挙動（リトライ、フォールバック、コスト制御など）を再利用できるようにする。

## 使いどころ

- 既製の重量級ハーネスでは対応しきれない独自の業務ロジックやガードレールが必要なエージェント開発チーム。
- 長時間実行するセッションでコンテキストウィンドウ超過やモデル呼び出しコストの膨張を防ぎたい場合。
- PIIの取り扱いや承認ゲートなど、モデルの判断に任せられないポリシーを毎回確実に適用したい場合。
