---
type: announcement
title: Claude Codeデスクトップに統合されたプレビュー・レビュー・自動マージ
title_original: Bringing automated preview, review, and merge to Claude Code on desktop
industry: cross-industry
cloud: []
patterns:
- ci-cd
- ai-agent
components:
- Claude Code
- GitHub CLI
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/preview-review-and-merge-with-claude-code
published_at: '2026-02-20'
---

## 概要

Claude Codeのデスクトップアプリに、開発サーバーのプレビュー表示、diffへのインラインレビューコメント、CIチェックの監視と自動修正・自動マージ、CLI/デスクトップ/モバイル間でのセッション引き継ぎ機能を追加した発表。コーディングからPRマージまでの開発ループを1つのアプリ内で完結させる。

## 設計のポイント

- Claudeがアプリのプレビュー画面とコンソールログを直接読み取り、ブラウザとの手動な行き来を無くして反復修正させる
- PRのCIチェック失敗をGitHub CLI経由で監視し、自動修正・自動マージまでバックグラウンドで完結させる

## 使いどころ

- コーディング後のレビューとCI待ちの間に他の作業へ切り替えたい開発者が、待ち時間を減らしたい場合
- CLI・デスクトップ・モバイルを行き来しながら同じ開発セッションを継続したいエンジニア
