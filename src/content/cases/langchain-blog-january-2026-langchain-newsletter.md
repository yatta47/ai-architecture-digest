---
type: announcement
title: LangSmith Agent Builder GA提供開始と本番トレース起点のエージェント評価基盤強化
title_original: 'Company Announcements January 2026: LangChain Newsletter'
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llmops
- eval
- memory-consolidation
components:
- LangSmith
- LangSmith Agent Builder
- LangChain JS
- deepagents
- Chat LangChain
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/january-2026-langchain-newsletter
published_at: '2026-08-26'
---

## 概要

LangChainが2026年1月のアップデートとして、自然言語からプロンプト・ツール選択・サブエージェント構成を自動生成するLangSmith Agent Builderの一般提供開始を発表した。あわせて、実験結果のサイドバイサイド比較やトレースから利用パターン・失敗モードを自動検知するInsights Agentのセルフホスト対応など、本番トレースを評価に直結させる観測性・評価まわりの機能強化が行われている。LangChain JSやdeepagentsではツール呼び出しの堅牢性やサブエージェントの進捗可視化も改善された。

## 設計のポイント

- 本番トレースをそのまま評価用のライブなテストケースとして扱い、トレーシングと評価を分離せず単一ワークフローに統合する
- エージェントの長期記憶を専用DBではなくMarkdown/JSONファイルというシンプルな形式で永続化する
- 自然言語の指示からプロンプト・ツール選択・サブエージェント構成・スキルを自動生成し、エージェント設計の初期構築を代行する
- サブエージェントの進捗をメッセージストリームとして可視化し、誰が何をしているかをリアルタイムに追跡できるようにする

## 使いどころ

- 本番運用中のエージェントの振る舞いパターンや失敗モードを継続的にモニタリングしたいチーム
- セキュリティ要件からセルフホスト環境でLangSmithの観測性・分析機能を使いたい企業
- コードを書かずに自然言語でエージェントのプロトタイプを素早く組み立てたい非エンジニア・市民開発者
- 複数モデルや実験構成を比較しながら回帰・改善を素早く検知したいML/エージェント開発チーム
