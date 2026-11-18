---
type: announcement
title: JetBrains版Copilot：クラウドサンドボックス・リモートアクセス・ブラウザ操作
title_original: GitHub Copilot in JetBrains, Ignite releases
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- parallel-execution
components:
- GitHub Copilot for JetBrains
- Cloud sandbox
- Browser use
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-11-17-github-copilot-in-jetbrains-ignite-releases
published_at: '2026-11-17'
---

## 概要

JetBrains版Copilotにクラウドサンドボックス、リモートアクセス、ブラウザ操作、オンデバイス音声入力が公開プレビューで追加された。クラウドサンドボックスはGitHub管理の隔離環境でセッションを実行しローカル資源を解放し並列実行を可能にする。

## 設計のポイント

- セッションを隔離されたクラウド環境で実行する。
- 複数クライアント間でセッションを共有する。

## 使いどころ

- ローカル負荷を抑えて複数のエージェントセッションを並列実行したい開発者。
