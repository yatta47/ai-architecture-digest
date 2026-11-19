---
type: announcement
title: ghコマンドでPRイベントをポーリングなしに待つ(エージェント向けEvent Streams)
title_original: Wait for pull request events with GitHub CLI
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- event-driven
components:
- GitHub CLI
- GitHub Event Streams
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-11-18-wait-for-pull-request-events-with-github-cli
published_at: '2026-11-19'
---

## 概要

gh v2.105.0のgh event listenで、PRのレビュー提出・状態変化・チェック完了などを1コマンドで待てるようになった(プレビュー)。ループのポーリングを置き換え、エージェントのコマンド提案にも組み込まれている。

## 設計のポイント

- ポーリングをイベントサブスクリプションに置き換え、エージェントループの無駄を減らす。
- 既定で最初のイベントで終了し、スクリプトやエージェントに組み込みやすい。
- 関連コマンドが自動でgh event listenを案内し、エージェントが発見できる。

## 使いどころ

- PRレビューやCI完了を待つコーディングエージェントを作るとき。
- CIスクリプトでポーリングを減らしたいとき。
