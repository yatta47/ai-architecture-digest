---
type: case
title: 社内向けエージェントを支える「カンパニーハーネス」の5要素
title_original: The five components of building a "company harness"
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- memory-consolidation
- human-in-the-loop
components:
- Slack
- LangSmith Sandboxes
- Managed Deep Agents
- GitHub
- Salesforce
- Notion
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/components-building-company-harness
published_at: '2026-10-25'
---

## 概要

LangChainがGTM、エンジニアリング、マーケティング向けに作った社内エージェント3種に共通する構成を、5つの要素にまとめた記事。Slack上での提供、本人代行と固定資格情報を使い分けるID設計、二層のメモリ、サンドボックスでのコード実行、スケジュール実行が柱である。

## 設計のポイント

- ツールごとに、呼び出した本人の権限で動く方式とエージェント固有の資格情報で動く方式を使い分け、共有チャンネルでは一部ツールを無効にする。
- メモリを全体用とユーザー用の二層に分け、保存先をエージェント自身に判断させる。
- サンドボックスの外でエージェントを動かして中へ接続し、シークレットプロキシで認証付きのサービスへ安全に接続する。
- 実行の多くをスケジュール起動にし、常時稼働のアンビエントエージェントとして運用する。

## 使いどころ

- Slackなど既存の業務ツール上で社内エージェントを展開したい企業。
- 営業、開発、マーケティングの各チームで共通基盤を使ってエージェントを作る場面。
- エージェントが誰の権限で何を実行するかを整理したいプラットフォームチーム。
