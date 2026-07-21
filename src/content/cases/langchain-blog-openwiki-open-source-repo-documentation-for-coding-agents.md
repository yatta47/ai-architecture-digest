---
type: announcement
title: リポジトリのドキュメントを自動生成・自動更新してコーディングエージェントに供給するOpenWiki
title_original: Introducing OpenWiki, an open source agent for repo documentation
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- document-processing
- context-engineering
- ci-cd
components:
- OpenWiki
- DeepAgents
- LangSmith
- GitHub Actions
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/introducing-openwiki-an-open-source-agent-for-repo-documentation
published_at: '2026-07-02'
---

## 概要

LangChainは、コードベース向けのドキュメント（wiki）を自動生成し、コーディングエージェントに接続するオープンソースのエージェント兼CLI「OpenWiki」を公開した。DeepAgents上に構築されており、生成したwikiへの参照をAGENTS.mdやCLAUDE.mdなどのエージェント指示ファイルに追記することで、エージェントが必要なときだけ詳細なコンテキストを取得できるようにする。GitHub Actionでの定期実行によりコミット差分を追跡してwikiを継続的に更新する仕組みも備える。

## 設計のポイント

- リポジトリ全体のwiki本文をエージェント指示ファイル（AGENTS.md/CLAUDE.md）に埋め込まず、参照リンクだけを追記することで、大規模リポジトリでも毎回の実行コンテキストを肥大化させない。
- GitHub Actionを日次などのスケジュールで実行し、直近のコミット以降のgit diffだけを解析して差分更新することで、ドキュメントの陳腐化を防ぎつつ更新コストを抑える。
- DeepAgents上に構築しLangSmithへのトレーシングを標準対応させることで、ドキュメント生成・更新エージェントが実際に何をしたかを事後検証できるようにする。
- OpenRouterの無料モデルをデフォルトにしつつOpenAI/Anthropic/Fireworks/Basetenなど複数のモデルプロバイダーを選択可能にし、コストと品質のトレードオフを利用者に委ねる。

## 使いどころ

- 大規模かつ変更頻度の高いリポジトリで、コーディングエージェントに正確な構造理解を持たせたいが手動でドキュメントを書き続ける余裕がないチーム。
- AGENTS.md/CLAUDE.mdは運用しているが、詳細なコンテキストをどう供給するか設計できていないエージェント活用チーム。
- エージェントの意思決定を後から追跡・検証したい、LangSmithなど既存の可観測性基盤を持つ開発チーム。
