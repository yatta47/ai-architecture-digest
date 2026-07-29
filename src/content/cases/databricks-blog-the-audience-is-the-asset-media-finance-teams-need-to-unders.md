---
type: opinion
title: メディア企業の財務チームがオーディエンス価値を把握するためのオントロジー駆動AIコワーカー
title_original: 'The audience is the asset: media finance teams need to understand them to protect margin'
industry: media
cloud: []
patterns:
- text-to-sql
- context-engineering
- ai-agent
- human-in-the-loop
components:
- Genie
outcome:
  type: revenue
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/audience-asset-media-finance-teams-need-understand-them-protect-margin
published_at: '2026-07-28'
---

## 概要

メディア企業の財務部門は、サブスクリプション・広告・コンテンツ投資といった複数チャネルにまたがるオーディエンスの価値を正確に把握する必要があるが、数字が組織を通過するうちに文脈が失われやすい。Databricksは、ビジネスの意味を保持し続ける「オントロジー」を土台に自然言語の質問へ根拠付きで回答するAIコワーカー「Genie」を提示し、DIRECTVでは数百人のアナリストが1200以上の顧客属性を自然言語で照会している。すべての回答が情報源に遡れ、権限とコストがガバナンスされた状態を保ちつつ、最終判断は人間が下す設計になっている。

## 設計のポイント

- 単発の検索ではなく、ビジネスの意味を保持し続ける「オントロジー」を土台にAIの回答を根拠付ける。
- 高コストなライブ検索ループを避け、ガバナンスされたオントロジー参照によりトークンコストを抑える。
- すべての回答をデータソースまでトレース可能にし、権限とコストを一元管理してガバナンスを担保する。
- 最終判断は人間が下すhuman-in-the-loop設計とし、AIは意思決定の材料提示に留める。

## 使いどころ

- メディア企業の財務チームがオーディエンス別・チャネル別の収益貢献を自然言語で素早く把握したい場合。
- マーケティングや運用チームがコンテンツ予算の投資回収状況を継続的にモニタリングしたい場合。
- 大量の顧客属性データを分析専門でないビジネスユーザーが自ら照会したい場合。
