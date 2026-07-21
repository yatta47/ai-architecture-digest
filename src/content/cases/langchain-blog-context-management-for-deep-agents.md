---
type: guidance
title: Deep Agents SDKのファイルシステムオフロードと段階的要約によるコンテキスト圧縮
title_original: Context Management for Deep Agents
industry: cross-industry
cloud: []
patterns:
- context-engineering
- memory-consolidation
components:
- Deep Agents SDK
- Claude Sonnet 4.5
outcome:
  type: reliability
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/context-management-for-deepagents
published_at: '2026-06-16'
---

## 概要

LangChainのDeep Agents SDKが、長時間タスクでのコンテキスト肥大化(コンテキスト・ロット)を防ぐための3段階のコンテキスト圧縮――大きなツール結果のファイルシステムへのオフロード、古いツール入力の切り詰め、閾値超過時の要約――を実装。要約時も元の会話全文をファイルシステムに保存し、後から検索復元できるようにする。

## 設計のポイント

- 大きすぎるツール結果は都度ファイルシステムにオフロードし、会話履歴にはプレビューとパスだけ残す
- コンテキストが閾値(85%等)を超えたら古いツール呼び出し引数を切り詰め、必要な情報のみ要約して保持する
- 要約時はセッション意図・成果物・次のステップを構造化して残し、元の会話全文はファイルシステムに保全して後から検索可能にする

## 使いどころ

- 長時間・多ステップにわたるエージェントタスクでコンテキストウィンドウを圧迫させたくない場合
- 要約後も過去の詳細情報を検索・復元できるようにしたいエージェント基盤
