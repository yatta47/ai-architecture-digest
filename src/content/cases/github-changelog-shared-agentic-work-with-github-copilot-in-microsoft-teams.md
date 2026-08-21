---
type: announcement
title: GitHub CopilotのエージェントセッションをMicrosoft Teamsで共同運転
title_original: Shared agentic work with GitHub Copilot in Microsoft Teams
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
components:
- GitHub Copilot
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-21-shared-agentic-work-with-github-copilot-in-microsoft-teams
published_at: '2026-08-21'
---

## 概要

Microsoft Teamsで@GitHubをメンションすると、参加者全員が見て操作を助けられるクラウドエージェントセッションが始まる。リポジトリへの書き込み権限を持つ参加者が変更をトリガーでき、ミーティングで出たアクションアイテムをその場でCopilotに引き渡し、専用コードチャンネルで進捗を追える。

## 設計のポイント

- 会議の議論からアクションアイテムを即座にエージェントへ引き渡し、会議終了前に着手させる
- 書き込み権限を持つ参加者のみが変更をトリガーできるようにしつつ、閲覧・文脈追加は参加者全員に開く権限分離を行う
- セキュアなクラウドサンドボックスでの非同期実行と、ターミナル/IDE/Copilotアプリへのシームレスな引き継ぎを両立する

## 使いどころ

- スタンドアップ等の会議で出た調査・修正タスクをその場でエージェントに着手させたいチーム
- 会議参加者全員でエージェントの作業を見守り、都度コンテキストを追加したい共同作業スタイル
- AIクレジットや予算管理のもとで組織的にクラウドエージェント利用を統制したい管理者
