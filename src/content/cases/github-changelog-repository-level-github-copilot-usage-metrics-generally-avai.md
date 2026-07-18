---
type: announcement
title: GitHub Copilotの利用状況をリポジトリ単位で計測するメトリクスAPIが一般提供に
title_original: Repository-level GitHub Copilot usage metrics generally available
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llmops
components:
- GitHub Copilot
- Copilot coding agent
- Copilot code review
- GitHub Copilot usage metrics REST API
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-07-17-repository-level-github-copilot-usage-metrics-generally-available
published_at: '2026-07-17'
---

## 概要

GitHub Copilotの利用状況メトリクスREST APIに、リポジトリ単位・日次のレポートを返す2つのエンドポイント（エンタープライズ用と組織用）が追加され一般提供となった。Copilotコーディングエージェントが作成・マージしたプルリクエスト数や、CopilotコードレビューがレビューしたPR数とコメント種別ごとの提案数を取得できる。

## 設計のポイント

- 利用計測を組織・ユーザー単位からリポジトリ×日付の粒度に落とし込み、どのリポジトリでAIが実際にPR活動を駆動しているかを可視化する
- 閲覧をView Copilot Metrics権限に紐づけ、粒度を上げつつアクセス制御を担保する
- 利用メトリクスポリシーの有効化を前提とし、計測の土台を確保する

## 使いどころ

- AI導入の効果測定を進めたい組織
- AI-readinessレポートを整備したい組織
- 効果の高いリポジトリに的を絞ってCopilot活用の展開を進めたい場面
