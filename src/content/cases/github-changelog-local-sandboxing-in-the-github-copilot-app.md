---
type: announcement
title: GitHub Copilotアプリのローカルサンドボックス(ファイル・ネットワーク・認証情報の制限)
title_original: Local sandboxing in the GitHub Copilot app
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- defense-in-depth
- policy-as-code
components:
- GitHub Copilot app
- GitHub CLI
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-23-local-sandboxing-in-the-github-copilot-app
published_at: '2026-09-23'
---

## 概要

GitHub Copilotアプリで、ローカルのセッションに対しファイルシステム・ネットワーク・認証情報へのアクセスをプロジェクト単位で制限するローカルサンドボックスがパブリックプレビューになった。OSが要求ポリシーを強制できない場合はサンドボックス無しで実行せずエラーにする。

## 設計のポイント

- ファイルシステム、ネットワーク、Git/GitHub CLI認証情報の3軸でプロジェクトごとにポリシーを宣言している。
- エンタープライズ管理設定でより厳しい実効ポリシーを上書きできる構成にしている。
- 強制不能時は無防備に実行せず失敗させるフェイルクローズ設計にしている。

## 使いどころ

- エージェントの意図しないコマンド実行の影響範囲を絞りたい開発チーム。
- 機密ディレクトリや認証情報を持つ開発端末でエージェントを使う組織。
- 管理者が組織横断でエージェント権限を統制したい場面。
