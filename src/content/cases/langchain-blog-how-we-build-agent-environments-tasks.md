---
type: case
title: LangChainの『スペック駆動』2段階パイプラインによるエージェント評価タスク自動生成
title_original: How We Build Agent Environments & Tasks
company: LangChain
industry: cross-industry
cloud: []
patterns:
- eval
- spec-driven-development
- ai-agent
- multi-agent-orchestration
components:
- Harbor
- eval-engineering skill
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/building-agent-environments-and-tasks
published_at: '2026-08-25'
---

## 概要

LangChainは、エージェント評価用のベンチマークタスクを量産するために、トレース・コード・人手入力から『スペック(自然言語の詳細仕様)』を作る工程と、そのスペックからタスク＆環境を生成する『Spec2Task』工程の2段階パイプラインを構築した。プロジェクト横断の再利用知識は『world spec』としてスクリプトや定義ごと切り出し、コーディングエージェントがリポジトリ走査やトレース分析を通じて最初のタスクを作りながらworld specを反復的に育てていく。

## 設計のポイント

- 『何を評価すべきか決める』工程と『実際にタスクを構築する』工程を分離し、前者に人間のレビューを集中させ後者はエージェントで並列自動化する
- タスク固有ではない再利用可能な知識（スキーマ、モックすべきAPI、採点関数など）を『world spec』として明示的に切り出し、スペック作成とタスク生成の両方から参照する
- world specはいきなり完成させず、最初の1〜3タスクをコーディングエージェントと一緒に作りながら反復的に汎化させていく
- 人間が読みやすいMarkdownのスペックを中間表現にすることで、コードやデータそのものより差分レビュー・バージョン管理・チーム間共有をしやすくする

## 使いどころ

- 多数のエージェント評価タスク・ベンチマークをスケールして作りたいAIプラットフォーム/evalチーム
- 実運用トレースの中からユーザーが実際に依頼しているパターンを抽出し、評価データセットに反映したい場合
- GTMエージェントやコードレビューエージェントなど、複数の異なるエージェント用途で評価基盤を横展開したいチーム
