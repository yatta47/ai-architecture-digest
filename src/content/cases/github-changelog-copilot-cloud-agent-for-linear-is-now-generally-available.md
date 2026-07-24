---
type: announcement
title: LinearからのCopilotクラウドエージェント割り当てが一般提供開始
title_original: Copilot cloud agent for Linear is now generally available
industry: cross-industry
cloud: []
patterns:
- ai-agent
- event-driven
components:
- GitHub Copilot cloud agent
- Linear
- GitHub Actions
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-07-23-copilot-cloud-agent-for-linear-is-now-generally-available
published_at: '2026-07-23'
---

## 概要

LinearのIssueをCopilotクラウドエージェントに直接割り当てられるようになり、GitHub Actions上のエフェメラルな環境で自律的にドラフトPRを作成し、進捗をLinearのタイムラインに反映する。モデル選択やカスタムエージェント、ブランチ指定もIssue単位・ワークスペース単位で設定できる。

## 設計のポイント

- エージェントはGitHub Actions駆動のエフェメラルな独立環境で作業し、完了時にレビュー依頼を出す非同期モデルを採る
- コメントでのメンションによりセッション実行中でも新たな指示を追加できるステアリング機能を持つ
- モデル・カスタムエージェント・ベース/作業ブランチをIssue単位または組織のagent guidanceで一括設定できる

## 使いどころ

- プロジェクト管理ツール(Linear)を起点に非同期でバックグラウンドコーディングエージェントを走らせたいチーム
- チームのワークフローに合わせたカスタムエージェントをIssueベースで運用したい場合
