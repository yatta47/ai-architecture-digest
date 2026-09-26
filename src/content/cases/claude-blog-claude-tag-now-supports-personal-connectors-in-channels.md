---
type: announcement
title: Claude TagがSlackチャンネルで個人コネクタに対応
title_original: Claude Tag now supports personal connectors in channels
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
- guardrails
components:
- Claude Tag
- Slack
- Google Drive
- GitHub
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-tag-now-supports-personal-connectors-in-channels
published_at: '2026-09-24'
---

## 概要

Claude Tagが、チャンネル内の依頼に本人の個人コネクタを使えるようになった。他のメンバーは使えず、投稿前レビューか自動投稿を選べる。管理者は共有ツール、個人コネクタのみ、ツール単位のいずれかで統制できる。個人コネクタは無人実行には使えない。

## 設計のポイント

- アクセス権をチャンネルでなく本人に紐づけ、既存のロールベース権限を活かす。
- チャンネル共有の作業は共有コネクタ（サービスアカウント）、個人分は個人コネクタと分離し、監査ログも分ける。
- 投稿前レビューと機微判定つき自動投稿を切り替えられるようにする。

## 使いどころ

- 個人のカレンダーや資料を参照しつつチームの場で協働したい場面。
- エージェントの権限を厳密に統制したい管理者。
