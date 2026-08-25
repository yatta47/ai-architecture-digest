---
type: case
title: Claude CodeでBigQueryの営業データから営業担当ごとに自動パーソナライズした週次ダイジェストを生成
title_original: How an Anthropic Field Marketer Uses Claude Code to Send Weekly Personalized Updates to Every Sales Rep
company: Anthropic
industry: cross-industry
cloud:
- gcp
patterns:
- ai-agent
- context-engineering
- data-federation
- human-in-the-loop
components:
- Claude Code
- BigQuery
- HubSpot
- Salesforce
- Clay
- Slack
outcome:
  type: revenue
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-an-anthropic-field-marketer-uses-claude-code-to-send-weekly-personalized-updates-to-every-sales-rep
published_at: '2026-08-24'
---

## 概要

Anthropicのフィールドマーケターは、毎週手作業でスライド化していた営業向け更新情報を、Claude CodeとMCP経由で接続したBigQuery（HubSpot/Clay/Salesforceを統合するデータの正)から、営業担当ごとにパーソナライズしたSlackダイジェストとして自動生成する仕組みに置き換えた。実際の展開とフィードバックを重ねる中でプロンプトに『URLを捏造しない』『イベント対象者と担当者の役職を照合する』などのルールを追記していき、最終的に全営業チームへ展開してエグゼクティブディナーの登録数を1週間で倍増させた。

## 設計のポイント

- 非エンジニアのマーケターが『技術的でない自分をプロダクトマネージャーとして扱ってほしい』と明示し、口頭説明の書き起こしで業務コンテキストをClaudeに渡すところから始めている
- 実運用でのフィードバック(誤ったURL生成、対象者不一致、シート列の並び替えなど)を1つずつ具体的なプロンプトルールに変換し、9個のコンテンツルールへ育てていった
- 列名を『C列を見よ』と固定指定せず『イベントURLの列を見よ』のように意味で指定し、ソースシートの列順変更に強くしている
- ペルソナ(営業担当/マネージャー/BDR)ごとにテンプレートとCRM上の紐付けロジックだけを差し替え、プロンプト構造とルールは使い回している

## 使いどころ

- 複数のCRM/データソースにまたがる情報を、受け手ごとにパーソナライズした定型レポートとして毎週配信したいマーケティング/営業支援チーム
- 非エンジニアがClaude Codeを使って自分の反復業務を自動化する際の、プロンプト改善の進め方（フィードバックをルール化していく）の実例として
- 同じプロンプト構造を役割の異なるチーム（BDR、CS、アライアンス）へ横展開したい場合
