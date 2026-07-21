---
type: case
title: Klarnaが8500万ユーザー規模のカスタマーサポートをLangGraph/LangSmithのマルチエージェントAIで刷新
title_original: How Klarna's AI assistant redefined customer support at scale for 85 million active users
company: Klarna
industry: financial-services
cloud: []
patterns:
- multi-agent-orchestration
- context-engineering
- eval
- prompt-optimization
components:
- LangGraph
- LangSmith
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/customers-klarna
published_at: '2026-06-25'
---

## 概要

決済・ショッピングサービスを展開するKlarnaは、8500万人以上のユーザーからの決済・返金・エスカレーション対応を担うAIアシスタントを、LangGraphによる制御可能なマルチエージェント構成とLangSmithによるテスト駆動運用で刷新した。動的なプロンプト調整とLLM評価に基づく継続的な改善サイクルにより、社員700人分に相当する業務量をこなしつつ、応答精度とコスト効率を両立させている。

## 設計のポイント

- LangGraphでリクエストのルーティングと処理を担う制御可能なマルチエージェントアーキテクチャを構築し、レイテンシ低減と運用コスト削減を両立する
- シナリオごとにプロンプトを動的に切り替えるコンテキスト認識型の設計により、トークンコストとレイテンシを抑えつつ関連性の高い応答を維持する
- LangSmithでエージェントの挙動をステップ単位で可視化するテスト駆動開発を採用し、LLM評価とプロンプト反復で性能を継続的に検証・改善する
- メタプロンプティングによるプロンプト最適化ワークフローを取り入れ、改善案の提示から応答品質への影響確認までをループ化する

## 使いどころ

- 数千万ユーザー規模で決済・返金など多部門にまたがるエスカレーション対応を自動化したいカスタマーサポート組織
- 応答品質を維持しながらレイテンシとトークンコストを削減したいAIアシスタント運用チーム
- プロンプト変更やエージェント挙動の影響をエビデンスベースで検証・改善したいLLMOps担当者
