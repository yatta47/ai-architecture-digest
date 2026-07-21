---
type: case
title: Lyft、LangGraph/LangSmithで非エンジニアも自走できるセルフサーブAIエージェント基盤を構築
title_original: How Lyft Built a Self-Serve AI Agent Platform for Customer Support with LangGraph and LangSmith
company: Lyft
industry: logistics
cloud:
- aws
patterns:
- ai-agent
- multi-agent-orchestration
- llmops
- eval
components:
- LangGraph
- LangSmith
- Amazon DynamoDB
outcome:
  type: speed
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/lyft-built-a-self-serve-ai-agent-platform-for-customer-support-with-langgraph-and-langsmith
published_at: '2026-06-25'
---

## 概要

Lyftはカスタマーサポート向けに、LangGraphのルーター型マルチエージェント構成とLangSmithによる評価・トレーシングを組み合わせたセルフサーブ基盤を構築した。ドメインエキスパートがプロンプトとJSON設定だけでエージェントを定義できる「Configurable Agent」層により、MLEを介さずにエージェント開発サイクルを約6か月から数週間に短縮した。高度な処理が必要な領域は専門家が手作業で構築する「Specialized Agent」として残し、安全性と品質を両立している。

## 設計のポイント

- メタエージェントが意図を分類しCommand(goto=...)でルーティングするルーター型マルチエージェント構成にする
- 複雑・高リスクな業務はMLEが手動実装するSpecialized Agent、定型業務はプロンプト+JSON設定で動的生成するConfigurable Agentに分離する
- 安全性チェックはCommand(goto=[...])のfan-outでLLM推論前に並列実行し、応答生成をブロックせず担保する
- LangGraphのBaseCheckpointSaverを実装したカスタムDynamoDBSaverで会話状態を永続化し、複数ターンの対話や再現・デバッグを可能にする

## 使いどころ

- 非技術者（オペレーション担当・VoCリード・プロダクトマネージャー）自身がプロンプトと設定でエージェントを定義・改善したい場合
- カスタマーサポートのように多様な意図に応じて専門エージェントへ振り分ける必要がある大規模対話システム
- LLM-as-a-judgeによる自動評価とトレーシングで、非エンジニアが作ったエージェントでも品質基準を維持したい場合
