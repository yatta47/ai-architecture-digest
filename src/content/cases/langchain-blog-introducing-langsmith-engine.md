---
type: announcement
title: 本番トレースを自動クラスタリングして原因診断・修正PR生成・eval追加までを行うAIエージェント改善エンジン
title_original: Introducing LangSmith Engine
company: LangChain
industry: cross-industry
cloud: []
patterns:
- llmops
- eval
- root-cause-analysis
- ai-agent
components:
- LangSmith
- LangSmith Engine
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/introducing-langsmith-engine
published_at: '2026-06-25'
---

## 概要

LangChainは、本番環境のエージェントトレースを継続的に監視し、失敗パターンを名前付きの課題としてクラスタリングするLangSmith Engineを発表した。リポジトリと連携することでコードに基づく根本原因診断を行い、修正PR・専用のオンライン評価者・オフラインeval用データセットを自動で生成する。開発者はレビューとマージを行うだけでよく、既存のLangSmithのトレース・評価基盤にそのまま組み込まれる。

## 設計のポイント

- 個々の失敗トレースを個別に見るのではなく、複数トレースを名前付きの『課題』としてクラスタリングし重大度と発生時期で優先順位付けする
- 修正PRを提案するだけでなく、その問題に特化したオンライン評価者を同時に生成し、再発時に自動で課題を再浮上させる
- 本番で発生した失敗トレースをそのままオフラインeval用データセットの正解データとして取り込み、テストスイートを継続的に強化する
- 新規のトレーシング/評価基盤を追加せず、既存のLangSmithの仕組みの上にエージェントとして重ねることで導入コストを下げる

## 使いどころ

- 本番トレース量が多く、目視でのパターン発見や根本原因の特定が困難になっているエージェント運用チーム
- 修正の都度、評価カバレッジが追いつかず同じ不具合が再発しやすいチーム
- カスタマーサポートボットなど、ユーザーフィードバックや評価スコアの悪化から不具合の兆候を早期に検知したい場面
- コードリポジトリと接続し、自動生成された修正PRのレビュー・マージだけで改善サイクルを回したいチーム
