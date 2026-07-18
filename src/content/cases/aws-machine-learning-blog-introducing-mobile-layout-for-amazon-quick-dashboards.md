---
type: announcement
title: Amazon Quickダッシュボードをスマホで自動最適表示するモバイルレイアウト
title_original: Introducing Mobile Layout for Amazon Quick dashboards
industry: cross-industry
cloud:
- aws
patterns:
- responsive-rendering
- business-intelligence-resilience
components:
- Amazon Quick
- Amazon Quick mobile app
- Free Form dashboards
data_sources:
- KPI
- 業務メトリクス
- チャート
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-mobile-layout-for-amazon-quick-dashboards/
published_at: '2026-07-17'
---

## 概要

Amazon QuickのFree Formダッシュボードに、スマホ・タブレットで自動的に1カラムの縦スクロール表示へ切り替わる「モバイルレイアウト」が追加された。端末のビューポートサイズを検知してモバイル表示とデスクトップ表示を切り替え、作成者・管理者・閲覧者いずれも設定やマイグレーションは不要。ピンチ操作や横スクロールなしで、既存ダッシュボードにそのままモバイルからアクセスできる。

## 設計のポイント

- 単一ソースからビューポート幅でレンダリングモードを切り替え、デスクトップ用キャンバスを別途作らない適応表示にする。
- 重なり合うビジュアルはGroup単位でまとめ、モバイルでも意図した重ね表示（KPIバナーなど）を保持する。
- 最小272px・最大高キャップのガードレールでアスペクト比を維持し、凡例・軸ラベルの可読性を担保する。

## 使いどころ

- 朝会での売上確認や会議合間のパイプライン確認など、定型データを短時間で繰り返し見る現場に効く
- 移動中や外出先で運用監視を続けたい人に有効
- デスクトップ設計のダッシュボードを、モバイルで日常的に閲覧する運用に向く
