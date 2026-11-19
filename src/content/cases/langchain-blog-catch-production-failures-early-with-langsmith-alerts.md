---
type: announcement
title: LangSmith Alertsでエラー率・遅延・フィードバックスコアを監視
title_original: Catch production failures early with LangSmith Alerts
company: LangChain
industry: cross-industry
cloud: []
patterns:
- llmops
- eval
components:
- LangSmith
- LangSmith Alerts
outcome:
  type: reliability
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/langsmith-alerts
published_at: '2026-11-19'
---

## 概要

LangSmithにエラー率、実行遅延、フィードバックスコアに基づくアラートが追加された。外部モデルやツールへの依存障害と、出力品質の劣化の両方を本番で早期に検知する。元記事は2025年の公開。

## 設計のポイント

- エラーと遅延に加え、ユーザーやオンライン評価のスコアも監視対象にする。
- 外部依存の障害と品質劣化という、LLMアプリ特有の二系統を見る。

## 使いどころ

- 本番のエージェントやLLMアプリを運用するチーム。
- プロンプト変更後の品質退行を早めに知りたいとき。
