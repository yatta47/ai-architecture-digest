---
type: announcement
title: オープンソースのエージェントハーネスDeep Agentsをマネージド運用するサービスがベータ公開
title_original: Managed Deep Agents is now in Public Beta
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- unified-runtime
- eval
components:
- LangSmith
- Deep Agents
- LangSmith Sandboxes
- Harbor
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/managed-deep-agents-is-now-in-public-beta
published_at: '2026-08-07'
---

## 概要

LangChainは、オープンソースのエージェントハーネス「Deep Agents」を本番運用するためのマネージドサービス「Managed Deep Agents」をパブリックベータとして公開した。開発者はモデル・指示・ツール・サブエージェントなどエージェント固有の部分を所有しつつ、永続化・メモリ・サンドボックス・デプロイといった基盤運用をLangSmithに委ねられる。

## 設計のポイント

- エージェント定義をinstructions/identity/memory/tools/skills/evalsなどのコードファーストなプロジェクト構造に分離し、独自ロジックと共通基盤を明確に切り分ける
- スレッド単位・エージェント単位で切り替え可能なサンドボックススコープにより、会話ごとの隔離と共有ワークスペースを使い分けられるようにする
- Harborを使い、最終出力だけでなくツール呼び出しやファイル状態などエージェントが辿った過程を検証するeval基盤を組み込む

## 使いどころ

- エージェントの永続化・ストリーミング・サンドボックス基盤を自前で構築する余力がないチーム
- 長時間稼働し人間の承認待ちで一時停止・再開が必要なエージェントを本番運用したい場合
- Slack等の複数チャネルからエージェントを呼び出し、状態を跨いで維持したいプロダクト
