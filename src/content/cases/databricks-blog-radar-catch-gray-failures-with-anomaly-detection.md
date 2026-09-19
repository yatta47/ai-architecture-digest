---
type: case
title: 異常検知パイプラインRADARでグレー障害を早期発見する
title_original: 'RADAR: Catch Gray Failures with Anomaly Detection'
company: Databricks
industry: cross-industry
cloud: []
patterns:
- root-cause-analysis
- event-driven
components:
- AI/BI Genie
outcome:
  type: reliability
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/radar-catch-gray-failures-anomaly-detection
published_at: '2026-09-19'
---

## 概要

Databricksは、ダッシュボードが正常に見えても一部の顧客だけが静かに失敗する「グレー障害」を検知するため、信頼性メトリクス収集・異常検知・アラート・根本原因分析の4段階からなるRADARというパイプラインを自社運用している。教師なしストリーミング異常検知モデルSPOTでエラー率の急増を検知し、AI/BI Genieが背景にあるダッシュボードで根本原因調査を支援する。自社適用により障害発見までの時間を95%短縮し、90%超の精度を達成した。

## 設計のポイント

- エラー件数だけでなく影響ユーザー数もエラーコード・リージョン別の時系列として記録し、部分的な障害を検知しやすくする
- 閾値の手動チューニングを避けるため、過去14日間から『正常』を学習する教師なしストリーミング異常検知モデル（SPOT）を採用する
- アラート層でコンテキスト付与・重複除去・担当チームへのルーティングを行い、オンコールの疲弊を防ぐ
- 根本原因分析にAIアシスタント連携のダッシュボードを紐づけ、調査時間を短縮する

## 使いどころ

- 決済や課金など、一部の顧客だけが静かに失敗する障害を顧客からの報告より先に検知したいSRE/プラットフォームチーム
- エラー率・コンバージョン率・モデル精度など任意の指標に同じ異常検知パターンを転用したい組織
- オンコール担当が大量のアラートに埋もれず、重要な異常だけに集中したい場合
