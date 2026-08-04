---
type: announcement
title: IssueやPRのコメントをトリガーにCopilotクラウドエージェントを自動起動する仕組み
title_original: Trigger Copilot automations with comments
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- event-driven
- human-in-the-loop
components:
- GitHub Copilot
- Copilot cloud agent
- GitHub Copilot Automations
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-03-trigger-copilot-automations-with-comments
published_at: '2026-08-03'
---

## 概要

GitHubは、IssueやPull Requestへのコメント投稿をトリガーにCopilotのクラウドエージェント自動化を起動できる機能を追加した。ドキュメント生成、エラー調査、リファクタリング用フォローアップIssueの作成など、特定のコメント文言を設定することで人間の指示をエージェント実行に変換できる。Copilot Pro/Pro+/Max/Business/Enterprise利用者が対象で、Business/Enterpriseでは管理者によるクラウドエージェントポリシーの有効化が必要。

## 設計のポイント

- コメントのテキスト内容をトリガー条件として設定し、特定のフレーズが投稿された時のみエージェントを起動する仕組みにしている
- IssueコメントとPRコメントの両方をイベントソースとして扱い、コンテキストに応じた自動化(調査・生成・タスク起票)を切り替えられる
- リポジトリのAgentsタブ内Automationsサイドバーで設定を一元管理し、GUIから有効化できるようにしている
- Enterprise/Business向けには管理者ポリシーによるガードレールを設け、無制限なエージェント実行を防いでいる

## 使いどころ

- コードレビュー中にPRへコメントするだけでドキュメントを自動生成・更新したい開発チーム
- Issueに貼られたスタックトレースやエラーログを起点に自動調査を始めたい運用担当者
- リファクタリングや技術的負債の指摘コメントから自動的にフォローアップIssueを起票したいプロジェクト管理者
