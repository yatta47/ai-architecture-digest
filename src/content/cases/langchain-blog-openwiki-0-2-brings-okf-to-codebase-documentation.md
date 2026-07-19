---
type: announcement
title: コードベースWikiにOKF構造化フォーマットを採用しエージェント検索を高速化
title_original: OpenWiki 0.2 is adopting the OKF support
industry: cross-industry
cloud: []
patterns:
- context-engineering
- document-processing
components:
- OpenWiki
- OKF
- AGENTS.md
- CLAUDE.md
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/openwiki-0-2-adds-okf-support
published_at: '2026-07-16'
---

## 概要

コードベース用Wikiを自動生成・維持するOpenWikiが、Google Cloud提案のナレッジWiki構造化規格OKFに対応した。各Wikiファイルにtitle/description/tags等のYAMLフロントマターを付与し、更新履歴を記録するlogs.mdを自動生成することで、エージェントが全文検索に頼らずタグやカテゴリで決定的に絞り込めるようにする。

## 設計のポイント

- 各ノートにYAMLフロントマター（type/title/description/tags等）を付けることで、index.mdやlogs.mdを機械的に生成できるようにする。
- 更新のたびにログを自動生成することで、エージェントが差分だけを把握でき、毎回Wiki全体を読み直す必要をなくす。
- オープンな標準規格に準拠することで、コミュニティ製のビューアやリンターなど周辺ツールとの相互運用性を確保する。

## 使いどころ

- 大規模化したコードベースWikiで、探索・更新・レビューのための構造が必要になったチーム。
- コーディングエージェントがドキュメント検索に費やすトークンと時間を削減したい開発チーム。
- タグやカテゴリでの決定的な絞り込み検索を将来的に構築したいドキュメント基盤チーム。
