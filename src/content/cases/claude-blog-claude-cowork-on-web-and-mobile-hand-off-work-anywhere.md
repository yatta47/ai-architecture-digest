---
type: announcement
title: Claude Coworkがモバイル・Webに対応、デバイスをまたいでタスクが継続実行
title_original: Claude Cowork is coming to mobile and web
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
components:
- Claude Cowork
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/cowork-web-mobile
published_at: '2026-07-07'
---

## 概要

Claude Coworkがモバイル・Web版に拡大し、セッションとファイルがデバイスをまたいで継続するようになった。デバイスがオフラインでもスケジュールタスクはバックグラウンドで進行し、人の判断が必要な箇所だけモバイル通知で確認を求める。

## 設計のポイント

- セッション状態をデバイスに紐づけず、デスクトップで開始しモバイルで確認・再開できるようにする
- スケジュールタスクはデバイスがオフラインでも実行を継続し、人の判断が必要な分岐点でのみ通知を送る
- 何かを実際に送信・確定する前には必ず人のレビューと承認を挟むガードレールを維持する

## 使いどころ

- 移動中や会議の合間にAIエージェントのタスクを確認・差し戻ししたい知識労働者
- 夜間・早朝にバッチ的な調査/資料作成タスクを走らせておきたいユーザー
