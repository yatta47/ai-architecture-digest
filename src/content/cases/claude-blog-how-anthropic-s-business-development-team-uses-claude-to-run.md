---
type: case
title: スキルとスケジュールタスクで営業インバウンド/アウトバウンドを回すClaude Cowork活用
title_original: How Anthropic's business development team uses Claude to run inbound and outbound at scale
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
- memory-consolidation
components:
- Claude Cowork
- Salesforce
- Gmail
- Google Calendar
- Gong
- Apollo
- Common Room
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-anthropics-business-development-team-uses-claude-to-run-inbound-and-outbound-at-scale
published_at: '2026-08-07'
---

## 概要

Anthropicの営業開発(BD)チームは、Claude Coworkのスキルとスケジュールタスクで受信箱対応・アカウント調査・CRM更新・商談コーチングを自動化した。毎時実行の受信箱スキルは社内ナレッジベースと担当者の文体を使って返信を下書きし、夜間の調査スキルはSalesforceやGongなど複数ツールを横断してアカウントごとのブリーフを作成、Salesforce更新は根拠付きで提案され担当者が承認する仕組みにした。

## 設計のポイント

- よくある質問と回答をまとめたナレッジベースをClaudeが作成・継続的に鮮度チェックし、返信ドラフトの根拠として使う設計にした。
- Salesforceの更新など影響の大きい操作は根拠付きで提案してから人間が承認するhuman-in-the-loopにし、却下理由も記録して同じ提案を繰り返さないようにした。
- 各担当者の執筆スタイルを学習する『voiceスキル』を作り、返信ドラフトを個人の文体に合わせた。
- 小さなメモリファイル/台帳を保持させることで、毎晩のアカウント調査が重複作業をせず前回からの差分に集中できるようにした。

## 使いどころ

- 毎日同じような問い合わせへの返信作成や口座調査に時間を取られている営業・BDR組織。
- CRM更新や商談ステージ変更など、正確性が重要な操作を人手承認込みで自動化したいセールスオペレーション担当者。
- 大量のアカウントを抱え、優先順位付けや商談機会の発見を毎晩自動化したいアカウントエグゼクティブ。
