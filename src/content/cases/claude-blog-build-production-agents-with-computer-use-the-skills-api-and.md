---
type: announcement
title: Claude Platform、Computer Use・Skills API・Files APIが一般提供開始
title_original: Build production agents with computer use, the Skills API, and the Files API
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
components:
- Claude Platform
- Skills API
- Files API
- Computer use
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/computer-use-skills-api-files-api
published_at: '2026-08-20'
---

## 概要

Computer use・Skills API・Files APIがClaude Platformで一般提供となり、あわせてWebアプリ操作向けの新しいbrowser useツールも追加された。エージェントがスクリーンショットを見てクリック・入力・スクロールすることで自動化対象外だったソフトウェアも操作でき、Skills APIでチームの専門知識を、Files APIでドキュメントの読み書きを扱えるようになる。

## 設計のポイント

- スクリーンショットベースの操作（computer use）とWebページ構造ベースの操作（browser use）を使い分け、自動化されていないアプリとWebアプリの両方に対応する
- スキルを『タスクに応じて必要な時だけロードされる指示・スクリプト・テンプレートのフォルダ』として定義し、実行はClaudeのコード実行サンドボックスに閉じ込めてホスティング負担をなくす
- Files APIでドキュメントをID参照可能にし、リクエストごとの再送信を避けてコンテキスト効率を上げる

## 使いどころ

- 自動化APIを持たない既存ソフトウェアをエージェントに操作させたいチーム
- チーム固有の業務知識をスキルとして再利用可能な形にパッケージしたい場合
- エージェントに完成済みファイル（PDF/スプレッドシート等）を読み書きさせたいワークフロー
