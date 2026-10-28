---
type: announcement
title: 複数リポジトリ・ツールを横断するCopilotアプリのProjectsとComputer Use
title_original: GitHub Copilot app, Universe releases
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- human-in-the-loop
components:
- GitHub Copilot app
- Slack
- Figma
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-28-github-copilot-app-universe-releases
published_at: '2026-10-28'
---

## 概要

GitHub Copilotアプリにプロジェクト機能(公開プレビュー)が追加され、複数リポジトリやSlack、Figmaなどの文脈をまとめて複数エージェントに任せられる。APIの無いデスクトップアプリを操作するComputer Useも公開プレビューで提供される。

## 設計のポイント

- 目標と文脈をプロジェクト単位で束ね、必要な数のエージェントをバックグラウンドで走らせてPRなどで返す。
- Computer Useは操作前にユーザー承認を求め、管理設定で組織側が無効化できる。

## 使いどころ

- リポジトリをまたぐ機能開発や、設計・仕様作成を含む作業を一元管理したい開発チーム。
- API連携の無い業務アプリの定型操作を自動化したい場面。
