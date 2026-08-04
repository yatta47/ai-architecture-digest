---
type: announcement
title: GitHubがAIエージェントでコードカバレッジ計測ワークフローを自動生成
title_original: 'Code coverage: Automatic enablement in Code Quality settings'
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- ci-cd
components:
- GitHub Code Quality
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-04-code-coverage-automatic-enablement-in-code-quality-settings
published_at: '2026-08-04'
---

## 概要

GitHubはCode Quality設定画面に、AIがリポジトリ用のコードカバレッジ計測ワークフローを自動生成する新オプションを追加した。ユーザーはワークフローを自分で書く必要がなく、エージェントがビルド・テスト実行・カバレッジレポート生成・アップロードまでを含むパイプラインをプルリクエストとして提案し、マージ前にレビューできる。現在はgithub.com上のすべてのGitHub Code Qualityユーザー向けにパブリックプレビューとして提供されている。

## 設計のポイント

- カバレッジ計測パイプラインの構築をAIエージェントに委ね、設定画面から1クリックで起動できるようにする
- 生成物は直接適用せずプルリクエストとして提示し、人がレビュー・マージするヒューマンインザループの安全策を組み込む
- 生成されるワークフローには最小権限（least-privilege）の権限設定をデフォルトで適用する

## 使いどころ

- カバレッジ計測の仕組みを持たないリポジトリで、設定手順を意識せずにパイプラインを立ち上げたいチーム
- CI設定のベストプラクティスに詳しくない開発者が、ガードレール付きでワークフローを試験導入したい場合
- GitHub Code Qualityを既に利用しているEnterprise CloudやTeamプランの組織が、カバレッジ導入の初期コストを下げたい場合
