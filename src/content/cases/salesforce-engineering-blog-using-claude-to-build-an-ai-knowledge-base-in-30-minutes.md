---
type: case
title: Claudeに散在ドキュメントを読み込ませ30分でチーム版ナレッジベースを構築
title_original: Using Claude to build an AI knowledge base in 30 minutes
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- context-engineering
- memory-consolidation
- document-processing
components:
- Claude
- Claude Skills
outcome:
  type: productivity
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/using-claude-to-build-an-ai-knowledge-base-in-30-minutes/
published_at: '2026-07-16'
---

## 概要

SalesforceのAgentic Searchチームは、設計文書やSlackスレッドなど散在するソースをClaudeに読み込ませ、概念・人物ごとにクロスリンクされたMarkdownノート群「Derived Knowledge Base」を生成する手法を1月から社内で運用してきた。ベクトルDBや厳密なオントロジーを必要とせず、ソースは不変のまま、エージェントが書くノートだけが継続的に洗練されていく設計により、毎回のオンボーディングやAIセッションで同じ理解を再構築するコストを排除する。

## 設計のポイント

- ソース文書は不変（immutable）として保持し、Claudeが生成する「概念」「人物」ノートだけが編集・進化する対象にすることで、情報の信頼性と鮮度を両立する。
- 固定のカテゴリ・タグ体系を事前設計せず、ノート間のリンクを自然言語のまま蓄積させることで、部分的・条件付きで曖昧な実世界の関係性を無理に単純化しない。
- ingest（取り込み）・derive（ノート生成）・query（質問）・refine（改善）の4動詞にワークフローを分解し、Claude Skillsとして繰り返し実行可能にする。
- RAGの代替ではなく前段の層として位置づけ、まず合成済みの高品質なコンテキストを参照させ、必要な場合のみ原典に潜らせる。

## 使いどころ

- 新規メンバーのオンボーディングのたびに同じ背景説明を繰り返している開発チーム。
- AIエージェントが毎セッション同じソースドキュメントを読み直してコンテキストを再構築し、トークンと時間を浪費しているケース。
- ベクトルDBや知識グラフを運用するコストをかけずに、まず軽量にチームのナレッジ基盤を立ち上げたい場合。
