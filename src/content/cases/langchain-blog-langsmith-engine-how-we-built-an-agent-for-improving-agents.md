---
type: case
title: エージェントのトレースから障害パターンを見つけ改善案を自動生成するエージェント「Engine」
title_original: How We Built LangSmith Engine, Our Agent for Improving Agents
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llmops
- eval
- root-cause-analysis
components:
- LangSmith
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-we-built-langsmith-engine-our-agent-for-improving-agents
published_at: '2026-08-26'
---

## 概要

LangChainは自社エージェント運用で溜まる大量のトレースを人手でレビューする負荷を減らすため、トレースから再発する失敗パターンを見つけ根拠付きの「Issue」として整理し、評価用データセットや修正案まで提案するオーケストレーター型エージェント「LangSmith Engine」を構築した。Agent Overviewという生きたドキュメントを軸に、既存Issue・トレース要約・接続されたコードベースを入力として継続的に学習・更新する設計になっている。

## 設計のポイント

- 全トレースを毎回フルロードするのではなく、コンパクトな軌跡要約から始め、深掘りが必要な場合だけ全文を読み込むことでスケールする設計にした
- Agent Overviewという「エージェントの仕様書」を初回実行時にブートストラップし、以降の実行のたびに読み書きして更新する永続的な入力にした
- 発見した障害を単なる悪いトレースの指摘で終わらせず、オンライン評価器・データセット例・修正案という具体的な次のアクションに変換する設計にした
- 既存のIssue Boardを毎回取得することで重複検知や証跡の追加を行い、Engine自身の状態を一貫させた

## 使いどころ

- 多数のエージェントを本番運用していてトレースのレビューが人手で回らなくなったチーム
- 本番での失敗をオフラインの評価データセットや回帰テストに変換したいLLMOpsチーム
- エージェントの障害パターンを継続的に検出・修正する仕組みを内製したい開発チーム
