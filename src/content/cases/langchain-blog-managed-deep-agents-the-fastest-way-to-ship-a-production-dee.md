---
type: announcement
title: LangChain、長時間稼働エージェントの実行基盤「Managed Deep Agents」をパブリックベータ提供
title_original: Introducing Managed Deep Agents
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- memory-consolidation
- human-in-the-loop
- llmops
components:
- LangSmith
- Deep Agents
- Context Hub
- LangSmith Engine
outcome:
  type: speed
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/introducing-managed-deep-agents
published_at: '2026-08-07'
---

## 概要

LangChainは、オープンソースのDeep Agentsハーネスに永続的な実行基盤を提供するAPIファーストのホスト型ランタイム「Managed Deep Agents」をパブリックベータで公開した。エージェント定義は自社リポジトリに保持しつつ、スレッド・チェックポイント・ストリーミング・サンドボックス実行・トレーシングといった運用レイヤーをLangSmith側で肩代わりする。

## 設計のポイント

- エージェント定義（AGENTS.md・skills・subagents・tools.json）と実行ランタイムを分離し、定義はリポジトリで管理しつつ運用はLangSmithに委ねる設計にした。
- Context Hubにより、実行間で永続化される作業コンテキストをエージェントに持たせ、プロンプトに書いた内容だけでなく実際の利用実績から学習・更新できるようにした。
- tools.json経由でツールごとにHuman-in-the-loopを有効化でき、サンドボックス実行と組み合わせてコード・シェル・ファイル操作を安全に任せられるようにした。
- 全ての実行をLangSmithで自動トレースし、既存のLLMオブザーバビリティのワークフローをそのままマネージドランタイムに接続した。

## 使いどころ

- 長時間・複数セッションにまたがるサポートトリアージやリサーチエージェントを、自前でランタイムを構築せずに運用したいチーム。
- コード実行やファイル操作を伴うエージェントに、再開可能な実行基盤とサンドボックスを持たせたい開発チーム。
- エージェントの挙動を実利用データから継続的に改善したいが、その基盤（記憶・トレーシング・承認フロー）を自作したくない場合。
