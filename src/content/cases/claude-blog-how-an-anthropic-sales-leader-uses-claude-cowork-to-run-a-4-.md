---
type: case
title: Claude Coworkで4,000件の顧客アカウントを一晩でスコアリングする営業支援基盤
title_original: How an Anthropic sales leader uses Claude Cowork to run a 4,000-account book
company: Anthropic
industry: cross-industry
cloud:
- gcp
patterns:
- ai-agent
- human-in-the-loop
- decision-execution
components:
- Claude Cowork
- Claude Code
- Salesforce
- BigQuery
- Google Calendar
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-an-anthropic-sales-leader-uses-claude-cowork-to-run-a-4-000-account-book
published_at: '2026-05-20'
---

## 概要

Anthropicの米国ミッドマーケット営業責任者Travis Bryant氏が、Claude Coworkを使って日々の顧客商談準備・週次フォーキャストの集計・四半期ごとの4,000アカウントのテリトリースコアリングを自動化した事例。従来数百時間を要していたアカウントスコアリングを、5軸のルーブリックをClaudeと定義した上で一晩のオーバーナイト実行で完了させ、結果をインタラクティブなダッシュボードとして営業担当者に配布している。

## 設計のポイント

- 毎朝実行されるスケジュールタスク(スキル)がカレンダーの会議室予約漏れを検知して自動予約し、商談前にSalesforceとBigQueryのデータをブリーフとして用意する。
- 評価軸(ルーブリック)をClaudeと一緒に定義し、テスト範囲で試して出力を確認しながら重み付けを調整するイテレーティブな運用パターンを取る。
- Claudeが提案し人間が承認してから外部システムに反映するヒューマン・イン・ザ・ループを組み込み、Salesforce更新などの実行を安全にする。
- スコアリング結果をテリトリー別インタラクティブダッシュボードに変換し、根拠(rationale)や類似事例をホバーで参照できるようにして営業担当が使えるツールに落とし込む。

## 使いどころ

- 日次の顧客商談準備や週次フォーキャストなど、繰り返し発生する定型データ集約・整形作業の自動化。
- 数千アカウント規模のテリトリー/アカウントスコアリングなど、従来は複数部門が数百時間かけていた分析作業を一晩で終わらせたいとき。
- TAM試算や競合比較、コストベンチマークなど、人手不足で先送りされてきた大規模調査プロジェクト。
- 非エンジニアの営業リーダーが、コマンドラインを使わずに自然言語でエージェントに継続的なタスクを任せたいとき。
