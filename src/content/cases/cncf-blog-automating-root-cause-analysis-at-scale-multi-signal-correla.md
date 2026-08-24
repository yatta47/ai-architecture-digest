---
type: case
title: メトリクス・ログ・トレースを相関させ根本原因を自動仮説化するAtlassianのRCA基盤
title_original: 'Automating Root Cause Analysis at Scale: Multi-Signal Correlation for Cloud-Native Incident Response'
company: Atlassian
industry: cross-industry
cloud: []
patterns:
- root-cause-analysis
- event-driven
components:
- OpenTelemetry
outcome:
  type: speed
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/08/24/automating-root-cause-analysis-at-scale-multi-signal-correlation-for-cloud-native-incident-response/
published_at: '2026-08-24'
---

## 概要

Atlassianは、数百のマイクロサービスにまたがる本番障害の根本原因分析を「信号種別(メトリクス/ログ/トレース)・時間・トポロジ」の3次元相関問題として自動化するシステムを構築した。各シグナルから独立に異常を検出して共通スキーマに正規化し、時間的な近接度スコアとサービス依存グラフを組み合わせてランク付けされた根本原因仮説を生成する。同一障害連鎖の重複検出をシーケンスフィンガープリンティングで抑制し、オンコールエンジニアが仮説検証から着手できるようにする。

## 設計のポイント

- メトリクス・ログ・トレースそれぞれに独立したプラガブルな異常検出器を用意し、正規化された共通スキーマの異常イベントとして相関エンジンに渡すことで検出手法を後から差し替え可能にする
- サービス依存グラフでまず障害範囲(ブラストラディウス)を絞り込んでから異常検出を実行し、分析対象を数百から数十サービスに削減する
- 時間窓でのスライディング相関に加え、同一因果連鎖の再発をシーケンスフィンガープリンティングで検出し重複仮説の氾濫を防ぐ
- sinkノード(最も異常度が高いサービス)を起点に依存グラフを遡ることで、時間的相関だけでなく因果の向きを推定する

## 使いどころ

- 数百規模のマイクロサービスを複数リージョン・複数クラウドで運用し、オンコール負荷を減らしたい組織
- 経験の浅いエンジニアでもベテランと同等の速度で障害の仮説形成ができるようにしたい場合
