---
type: announcement
title: Claudeがファイル生成・編集に対応、専用コンピュータ環境で表計算・文書・PDFを直接作成
title_original: Claude can now create and edit files
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- document-processing
components:
- Claude.ai
- Claude Desktop
- Google Drive
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/create-files
published_at: '2025-09-09'
---

## 概要

Claude.aiとデスクトップアプリに、Excelスプレッドシート・Word文書・PowerPoint・PDFを直接生成・編集できる機能が追加された。Claudeに与えられた専用のコンピュータ環境でコードを書き実行することで、テキスト応答やアーティファクトだけでなく、そのまま使えるファイルとして成果物を返せるようになる。Max/Team/Enterpriseプランでプレビュー提供され、後にネットワーク・データ送信制御を備えて一般提供された。

## 設計のポイント

- 生成物をチャット内テキストではなくファイル(スプレッドシート/文書/スライド/PDF)として出力することで、そのまま業務に使える成果物に変換する
- Claude専用のプライベートなコンピュータ実行環境を与え、コード生成と実行を組み合わせてファイル作成・分析タスクを完結させる
- アップロードされたデータやPDF・メモなど異なる入力形式から、目的のフォーマット(スライドや文書など)へのクロスフォーマット変換を可能にする
- インターネットアクセスを伴う機能であるためネットワーク・送信データの制御やチャットの監視を運用上の注意点として明示する

## 使いどころ

- 生データを渡すだけでクレンジング・統計分析・グラフ・示唆コメント付きの分析レポートを得たい業務ユーザー
- シナリオ分析付きの財務モデルやダッシュボード付きプロジェクト管理表など、定型フォーマットの表計算作成を自動化したい担当者
- PDFレポートからスライド、議事録メモから整形済み文書、請求書から集計済み表など、資料のフォーマット変換をまとめて行いたいケース
- プログラミングや統計の専門知識がなくても、会話だけで高度な多段階の資料作成プロジェクトを進めたいチーム
