---
type: guidance
title: 小売・CPG向け『月曜朝会』をエージェントが自動化する意思決定基盤
title_original: 'The New Monday Morning Report: How Generative AI Can Deliver the Insights Your Executives Need'
industry: retail
cloud:
- multi-cloud
patterns:
- ai-agent
- text-to-sql
- data-federation
- business-intelligence-resilience
components:
- Genie Ontology
- Unity AI Gateway
- Delta Sharing
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/new-monday-morning-report-how-generative-ai-can-deliver-insights-your-executives-need
published_at: '2026-08-03'
---

## 概要

小売とCPGの合同会議は毎週の数字合わせに時間を溶かし、決定に至らない『儀式』化しやすい。Databricksは自社・取引先データをGenie Ontologyで統合しUnity AI Gatewayでガバナンスを効かせ、Delta Sharingで社外データも取り込んだ上で、エージェントが夜間に数千SKU×店舗を走査し、優先度付きの推奨アクションを翌朝提示するアーキテクチャを提案する。

## 設計のポイント

- Delta Sharingで自社と取引先のデータをコピーせずに同じガバナンス配下で共有し、双方が同じ数字を見られるようにする
- エージェントが人手では回りきれない粒度（数百万のアイテム×店舗の組合せ）を毎晩スキャンし、影響度順にウォッチ項目を絞り込んで提示する
- 自然言語インターフェースをガバナンス済みデータの上に直接載せ、SQLやチケット無しでその場で追加質問に答えられるようにする
- レポート（読むだけ）→儀式（合意なき議論）→意思決定システム（承認/編集で完結）という成熟度モデルを設計目標に据える

## 使いどころ

- メーカーと小売の合同事業計画（JBP）で毎週のデータ突合に時間を取られているチーム
- 在庫欠品や需要予測のズレを早期に検知して発注・販促を修正したいオペレーション部門
- 数千SKU規模の店舗横断モニタリングを人手のダッシュボード監視から脱却させたいケース
