---
type: announcement
title: GitHub Copilotコードレビューにファイアウォール・カスタム指示・ランナー個別設定を追加
title_original: Copilot code review customization and configurability improvements
industry: cross-industry
cloud: []
patterns:
- ci-cd
- guardrails
- policy-as-code
components:
- GitHub Copilot code review
- GitHub Copilot cloud agent
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-07-17-copilot-code-review-customization-and-configurability-improvements
published_at: '2026-07-17'
---

## 概要

GitHub Copilotのコードレビュー機能が、ヘッドブランチからのカスタム指示読み込みや複数形式のカスタム指示ファイル対応、レビュー専用のファイアウォールとランナー設定、copilot-code-review.ymlによるセットアップ手順のカスタマイズに対応し、管理者と開発者がレビュー環境をより細かく制御できるようになった。

## 設計のポイント

- カスタム指示をベースブランチではなくヘッドブランチから読み込み、マージ前のフィーチャーブランチ上で指示の変更を検証できるようにする
- copilot-instructions.md・REVIEW.md・AGENTS.md・CLAUDE.mdなど複数形式のカスタム指示ファイルを自動的に読み取る
- Copilotコードレビュー専用のファイアウォールをCopilotクラウドエージェントとは独立に既定で有効化し、レビュー実行時のネットワークアクセスを制限する
- copilot-code-review.ymlでレビュー専用のセットアップ手順を定義し、無ければ既存のcopilot-setup-steps.ymlにフォールバックする

## 使いどころ

- AIコードレビューの挙動やネットワークアクセスをリポジトリ・組織単位で細かくガバナンスしたい管理者
- レビュー用カスタム指示をフィーチャーブランチ上で試行錯誤したい開発チーム
- レビューエージェントとクラウドエージェントでランナー環境を分離したいプラットフォームチーム
