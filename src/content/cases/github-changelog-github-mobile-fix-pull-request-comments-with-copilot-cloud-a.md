---
type: announcement
title: GitHub Mobile、PRレビューコメントからワンタップでCopilotクラウドエージェントに修正依頼
title_original: 'GitHub Mobile: Fix pull request comments with Copilot cloud agent'
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
components:
- GitHub Copilot
- GitHub Mobile
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-07-17-github-mobile-fix-pull-request-comments-with-copilot-cloud-agent
published_at: '2026-07-17'
---

## 概要

GitHub Mobile のプルリクエスト画面とレビューコメントに「Fix with Copilot」ボタンを追加し、モバイルからでもプロンプトを自分で書かずに Copilot cloud agent へ修正を依頼できるようにした。外出先やコードレビュー中でもワンタップで修正に着手できるようにし、レビュー対応によるPR停滞を減らす狙いがある。iOS/Android の GitHub Mobile 最新版で利用可能。

## 設計のポイント

- レビューコメントという『修正指示が既に自然言語で存在する』場所にエントリーポイントを置き、プロンプト作成の手間を省く
- PR全体ビューと個別コメントの両方にボタンを配置し、レビューの粒度に応じて起点を選べるようにする
- モバイル端末からの指示をクラウド上のエージェント実行に委譲し、端末側の実行力に依存しない構成にする

## 使いどころ

- 外出先やモバイル中心の開発者がレビュー指摘への対応を素早く始めたい場面
- レビューアからの細かい指摘をエージェントにそのまま渡して手戻りを減らしたいチーム
