---
type: guidance
title: FSx for ONTAP上のファイルをAmazon Quickでガバナンス付き週次レポート化
title_original: Governed reports with Amazon Quick Desktop and Amazon FSx for NetApp ONTAP
industry: cross-industry
cloud:
- aws
patterns:
- rag
- ai-agent
- document-processing
- human-in-the-loop
components:
- Amazon Quick Desktop
- Amazon Quick skills
- Amazon FSx for NetApp ONTAP
- Amazon S3 access points
- Slack
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/governed-reports-with-amazon-quick-desktop-and-amazon-fsx-for-netapp-ontap/
published_at: '2026-08-25'
---

## 概要

AWSのブログでは、既存のファイルサーバー(FSx for ONTAP)上の業務ファイルをS3アクセスポイント経由でAmazon Quickに限定公開し、AIアシスタント「Weekly Business Reporting Assistant」が引用付きの週次レポートやSlack向け要約を生成する構成を紹介する。ソースファイルはFSx側の既存の権限管理下に置いたまま、承認済みフォルダのみをナレッジベース化することでガバナンスを保ちつつAI活用を進める。生成後のSlack投稿は人間のレビューを経てから送信される。

## 設計のポイント

- 業務ファイルは既存のストレージ(FSx for ONTAP)に残したまま、S3アクセスポイントとIAMで読み取り範囲を承認済みフォルダのみに限定する
- スキルという再利用可能なワークフロー定義で、情報源・出力形式・引用ルール・確認タイミングを固定化し、毎回の対話品質を安定させる
- 生成物をそのまま外部に送らず、Slack投稿前に人間のレビュー・承認ステップを挟む
- 個人ナレッジグラフ(My context)と、承認済み情報源のみで構成するナレッジベースを役割分担させ、事実の根拠は常にガバナンスされた側に置く

## 使いどころ

- オペレーションレビューや週次ビジネスレビューなど、決まった様式の社内レポートを毎週手作業で作っているチーム
- 既存のファイルサーバーの権限体系を崩さずに生成AIを導入したい情報システム/データガバナンス担当
- レポート内の数値や記述の根拠(引用元文書)を常に追跡したい経営層向け報告フロー
