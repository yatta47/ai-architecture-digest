---
type: announcement
title: エージェント向けプロアクティブメモリ『OpenWiki Brains』
title_original: Introducing OpenWiki Brains, general-purpose wiki memory for agents
company: LangChain
industry: cross-industry
cloud:
- on-prem
patterns:
- ai-agent
- context-engineering
- memory-consolidation
- document-processing
components:
- OpenWiki
- Gmail
- Notion
- Git
- Twitter/X
- Hacker News
- Web search
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/introducing-openwiki-brains-general-purpose-wiki-memory-for-agents
published_at: '2026-07-13'
---

## 概要

LangChainがOpenWiki 0.1.0で、Gmail・Notion・Gitリポジトリ・Twitter/X・Hacker News・Web検索などのコネクタから情報を能動的に収集し、ローカルのMarkdownウィキとして構造化・自動更新する『OpenWiki Brains』を発表した。従来の内蔵メモリがユーザーが明示的に伝えた情報しか記憶できない受動的な仕組みだったのに対し、Personal Brainはユーザーが指定した関心事に沿って各ソースを能動的に探索しウィキへ書き込むプロアクティブなメモリを提供する。

## 設計のポイント

- ウィキはローカルマシン上で稼働し、常駐サーバーを立てずにスケジュールジョブでコネクタから情報を取得・反映するだけで鮮度を保てる設計にしている。
- Gmail/Twitter/Hacker News/Gitのように決定的に取得できるコネクタと、Notionやweb検索のようにゴールを与えてエージェントに探索させる必要があるコネクタを区別して扱っている。
- セットアップ時にウィキが何を優先して残すべきかのプロンプトを設定させ、取り込み時の情報選別基準を明確化している。
- コード用のCode Brainと汎用ワークコンテキスト用のPersonal Brainを分離し、それぞれ異なるプロンプト・コネクタ・更新ワークフローを持たせている。

## 使いどころ

- 研究・プロジェクト管理・顧客対応など、コードベース以外の散在したコンテキスト(メール・Notion・SNS)をエージェントに継続的に把握させたい個人や小規模チーム。
- セッションのたびに同じ背景情報をコピペしたり都度検索させたりする手間を省き、エージェントに常に最新の作業コンテキストを持たせたい場合。
- コーディングエージェント向けにリポジトリ構造やコーディング規約を自動生成・維持するCode Brainとして、オンボーディングや大規模リポジトリの理解を助けたい場合。
