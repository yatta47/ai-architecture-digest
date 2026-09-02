---
type: case
title: Anthropic社員によるClaude TagのSlack内活用（資料化・要望集約・法務レビュー）
title_original: How Anthropic employees use Claude Tag
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
- context-engineering
components:
- Claude Tag
- Slack
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-anthropic-employees-use-claude-tag
published_at: '2026-08-28'
---

## 概要

AnthropicはSlack上で@Claudeとタグ付けして会話の文脈やメモリ、標準指示をもとにタスクを実行するClaude Tagを社内で活用している。プロダクトマーケティング担当は15件超のスレッドの議論を45分で顧客向け資料に整形し、プロダクト戦略担当はSlack全体を横断検索して機能要望や週次の障害報告を数十分で集約するなど、数日〜1週間かかる作業を大幅に短縮した。

## 設計のポイント

- Claudeにファクトチェックや根拠資料との突き合わせを追加で依頼することで、生成内容の正確性を人間が検証する工程を組み込んでいる。
- アクセス範囲を許可されたチャンネル・ドキュメントに限定し、アクセス不可の場合はその旨を利用者に伝えるスコープ制御を行っている。
- プライベートSlackチャンネルでスレッドごとにタグ付けし、Claudeが進捗チェックリストを更新しながらバックグラウンドで作業を進める運用にしている。

## 使いどころ

- 複数人が入り乱れたSlackスレッドの議論を、レビュー可能な一枚の顧客向けドキュメントに整形したい場面。
- 数ヶ月分のSlack履歴に散らばった機能要望やインシデント報告を横断的に検索・集約し、担当者へフォローアップしたい場面。
