---
type: announcement
title: 'Managed Deep Agents 0.8: ユーザー単位の認証・メモリとHTTPチャネル'
title_original: 'Managed Deep Agents v0.8: new auth, memory, and channels'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- memory-consolidation
- guardrails
components:
- Managed Deep Agents
- Deep Agents
- LangSmith Context Hub
- Slack
- Parallel
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/langsmith-managed-deep-agents-whats-new
published_at: '2026-09-24'
---

## 概要

Managed Deep Agents 0.8は、ユーザー所有の認証情報、ユーザー単位のメモリ、HTTPチャネル、Slackのファイル転送、Parallel製のWeb検索ツールを追加した。エージェントの本番運用に必要な基盤をコード中心のプロジェクトとして提供する。

## 設計のポイント

- メモリをエージェント共有層とユーザー層に分け、実行元ごとの既定ポリシーで複数人の会話への個人情報漏えいを防ぐ。
- 認証情報を名前付きの接続として管理し、ユーザーまたはエージェント単位でスコープする。
- エージェントの要素を宣言ファイルのディレクトリ構成にまとめ、Context Hubで指示やスキルをバージョン管理する。
- Webhook対応のHTTPチャネルで、社内ツールや顧客ポータルにエージェントを組み込める。

## 使いどころ

- 営業支援など、複数ユーザーが使う社内エージェントで個人の好みを保持したい場合。
- 顧客機密を守りつつ、本番チャットをエージェントとして運用したい場合。
- 認証・チャネル・権限管理の基盤構築に工数をかけたくないチーム。
