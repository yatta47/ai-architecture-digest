---
type: announcement
title: LangSmith Engine v2によるエージェントのレッドチーミングと修正の自動検証
title_original: 'LangSmith Engine v2: Red teaming and automated testing'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- llmops
- eval
- root-cause-analysis
- ai-agent
components:
- LangSmith Engine
- LangSmith Deployment
- LangSmith
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/langsmith-engine-v2-redteam
published_at: '2026-09-24'
---

## 概要

LangSmith Engine v2は、本番トレースから問題を検出・グループ化するエージェントで、新たにレッドチーミング、非効率な軌跡や指標傾向の検出、提案した修正の事前自動検証を備える。修正は失敗の再現とテストを繰り返してから提示され、ワンクリックでPRにできる。

## 設計のポイント

- 本番トレースとリポジトリから目的と挙動を把握し、未発生の弱点を先回りして検証する。
- 問題を根本原因・修正案・評価用の正解例・監視とセットで1つのキューに集約する。
- 修正案は失敗を再現し、修正・再テスト・調整を繰り返してから人のレビューに回す。
- セルフホスト向けにBYOKを提供し、トレースをVPC内に留めたまま推論できるようにする。

## 使いどころ

- 本番エージェントの不具合をユーザーに影響する前に見つけたい開発チーム。
- トークンの無駄やレイテンシ劣化を継続的に監視したい場合。
- 修正のオフライン検証の手間を減らしてリリースを速めたい場合。
