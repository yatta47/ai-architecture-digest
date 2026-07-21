---
type: guidance
title: 非エンジニアの日常業務をエージェントに委任するClaude Coworkの始め方
title_original: Best practices for getting started with Claude Cowork
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- out-of-band-inference
- human-in-the-loop
components:
- Claude Cowork
- Claude Code
- Claude Design
- Slack
- Gmail
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/best-practices-for-getting-started-with-claude-cowork
published_at: '2026-06-03'
---

## 概要

Anthropicのグロースマーケティングリードが、Chat・Claude Cowork・Claude Codeの使い分けを整理し、日常のナレッジワークをどう委任すべきかを解説する。Claude Coworkはデスクトップアプリからフォルダやアプリ(Slack、Gmailなど)に接続し、多段階の作業をアウトカム指定だけで完了できるエージェント型ワークスペースであり、著者自身が毎朝6時に実行するメール・Slackのデイリーブリーフィングや、広告費のペーシング管理といった実例を紹介する。

## 設計のポイント

- 入力が複数(複数ファイル・フォルダ・複数アプリ連携)で、出力が共有・再利用可能な成果物になるタスクをClaude Cowork向けの候補として選ぶ。
- 同じタスクを繰り返す場合はスケジュール実行(例: 毎朝6時のデイリーブリーフィング)に落とし込み、完成した成果物だけを確認する運用にする。
- 発注者自身が『何が良い出力か』を把握しているタスクに限定し、短時間で成果物の正誤を判断できる状態を保つことで丸投げ時の手戻りを防ぐ。
- Chat・Claude Cowork・Claude Codeは同じモデル基盤上の別ワークスペースであり、即答が欲しいか成果物への委任かでツールを使い分ける。

## 使いどころ

- SlackやEmailに情報が埋もれがちな非エンジニアが、毎日のメール・チャンネル要約とインシデント検知を自動化したい場面。
- パフォーマンスマーケティング担当者が、各広告チャネルの日次支出データを手作業でスプレッドシートに転記・集計している定型業務を自動化したい場面。
- コーディング知識のない非技術者が、複数ファイル・複数アプリにまたがる資料作成(デッキ作成やCMS更新など)をエージェントに任せたい場面。
- エンジニア以外のチームが、Claude Codeと同じ基盤を使いながらコードを書かずに業務プロセスを自動化したい場面。
