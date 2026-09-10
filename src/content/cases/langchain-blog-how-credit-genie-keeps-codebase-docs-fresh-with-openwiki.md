---
type: case
title: Credit GenieがOpenWikiでコードベースドキュメントを自動維持
title_original: How Credit Genie uses OpenWiki to keep codebase knowledge fresh, searchable, and automated
company: Credit Genie
industry: financial-services
cloud: []
patterns:
- ai-agent
- context-engineering
- document-processing
components:
- OpenWiki
- LangChain
- GitHub Pages
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-credit-genie-uses-openwiki-to-keep-codebase-knowledge-fresh-searchable-and-automated
published_at: '2026-09-10'
---

## 概要

金融ウェルネスアプリのCredit Genieは、拡大するコードベースでドキュメントが陳腐化し知識が属人化する課題に対し、LangChainのオープンソースリポジトリドキュメント生成エージェントOpenWikiを導入した。コード変更に応じて自動生成・更新されるドキュメントをGitHub Pages上の自社ポータルに集約し、人間のエンジニアだけでなくコーディングエージェントも参照できるようにした。

## 設計のポイント

- ドキュメント生成をコードの変更に連動させ、手動更新の運用コストをゼロに近づける
- 人間向けの検索可能なWebポータルと、コーディングエージェントが参照するopenwiki/フォルダの両方に同じ情報源を提供する
- 複数リポジトリのドキュメントを1つの自己サービス型ポータルに集約し『制度的知識の保険』として機能させる

## 使いどころ

- 急成長でコードベースが拡大し、担当者ごとに知識が分散してしまったエンジニアリング組織
- コーディングエージェントが正しいコンテキストを得られず誤った実装をしてしまう課題を抱えるチーム
