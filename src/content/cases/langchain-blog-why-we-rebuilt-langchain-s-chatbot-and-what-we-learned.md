---
type: case
title: LangChainチャットボット刷新：質問の複雑さで使い分ける2種類のエージェント構成
title_original: Why We Rebuilt LangChain's Chatbot and What We Learned
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- context-engineering
- llmops
components:
- LangChain
- LangGraph
- LangSmith
- chat.langchain.com
- createAgent
- Deep Agent
- Claude Haiku 4.5
- GPT-4o Mini
- GPT-4o-nano
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/rebuilding-chat-langchain
published_at: '2026-08-26'
---

## 概要

LangChainは社内エンジニアがドキュメント・ナレッジベース・コードベースを手動で行き来していたデバッグ習慣をDeep Agentとして自動化し、その学びを公開チャットボットchat.langchain.comの再構築に活用した。単純な質問には計画フェーズのないcreateAgentと軽量モデルで数秒応答し、コード調査が必要な複雑な質問にはドキュメント/ナレッジベース/コードベース検索を担当する専門サブエージェントを持つDeep Agentで数分かけて深く調査する、という2アーキテクチャの使い分けを実現した。

## 設計のポイント

- 単純なドキュメントQ&Aには計画・オーケストレーションのないcreateAgentを採用し、Claude Haiku 4.5など高速なモデルと組み合わせて3〜6回のツール呼び出しで15秒以内に応答させる。
- コード調査を伴う複雑な質問には、ドキュメント検索・ナレッジベース検索・コードベース検索をそれぞれ担当する独立したサブエージェントを持つDeep Agentを使い、各サブエージェントが結果を絞り込んでからオーケストレータに渡すことでメインエージェントのコンテキスト過多を防ぐ。
- LangSmithで全会話をトレースし、不要なツール呼び出しやプロンプトの改善点を特定した上で、評価スイートによるA/Bテストで速度と精度を両立させる。
- ベクトル検索によるチャンク化・埋め込み・再インデックスに依存する従来のRAG構成から、ドキュメント原文とコードベースを直接参照する構成に切り替えることで、引用の信頼性を高める。

## 使いどころ

- 社内サポートエンジニアが本番障害を調査する際に、公式ドキュメント・過去の類似問い合わせ・実装コードの3系統を横断して根拠付きの回答を得たい場面。
- 公開ドキュメントQ&Aボットを運営し、ベクトルDBのチャンク化や再インデックスの運用負荷を減らしつつ回答の引用精度を上げたい開発者向けプロダクトチーム。
- 質問の難易度に応じて『即答の速さ』と『深掘り調査の正確さ』のどちらを優先するかをアーキテクチャレベルで切り替えたいカスタマーサポート/開発者支援エージェントの設計者。
