---
type: announcement
title: 'GitHub Copilotの週次アップデート: セッション管理とマルチモデル可視化の強化'
title_original: GitHub Copilot weekly releases — August 3
company: GitHub
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
- multilingual-localization
- ai-agent
components:
- GitHub Copilot
- GitHub Copilot CLI
- VS Code
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-07-github-copilot-weekly-releases-august-3
published_at: '2026-08-07'
---

## 概要

GitHub Copilotのデスクトップアプリ・CLI・VS Codeにまたがる週次アップデートで、リクエストごとの使用モデル表示、CLIでの並行セッション管理・独立ワークツリー作成、VS Codeでの多言語オンデバイス音声入力などが追加された。作業を中断せずに文脈を保ったままレビューや並行探索を行えるようにする更新群。

## 設計のポイント

- 完了したリクエストごとに使用モデルやAIクレジット消費を表示し、マルチモデル運用の透明性を高める。
- CLIにセッションサイドバーと/worktreeコマンドを追加し、メインの作業を止めずに並行会話や独立ワークスペースを扱えるようにする。
- 音声入力を多言語対応のオンデバイスモデルに切り替え、音声データを端末外に出さずにプライバシーを担保する。

## 使いどころ

- 複数の会話やタスクを並行して進めたい開発者が、作業コンテキストを保ったままセッションを切り替えたい場合。
- レビュー中に本流を止めずに関連質問を投げたいペアプログラミング的なワークフロー。
- 音声入力や多言語チームでのローカライズが必要な開発環境。
