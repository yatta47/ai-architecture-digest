---
type: guidance
title: Amazon Quick Automateで作るRFI回答書の自動抽出ワークフロー
title_original: Build an end-to-end RFI questionnaire workflow using Amazon Quick Automate
industry: cross-industry
cloud:
- aws
patterns:
- multi-agent-orchestration
- document-processing
- ai-agent
components:
- Amazon Quick Automate
- Amazon S3
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-an-end-to-end-rfi-questionnaire-workflow-using-amazon-quick-automate/
published_at: '2026-09-10'
---

## 概要

多段タブで構成される複雑なRFI（情報提供依頼）回答書をS3から取り込み、自然言語の指示だけで質問・カテゴリ・回答種別を抽出してCSVに構造化するワークフローをAmazon Quick Automateで構築する方法を解説する。会話形式でワークフローを反復修正し、検証後にリージョン間で昇格できる。

## 設計のポイント

- 処理ロジックをコードではなく自然言語プロンプトで記述し、フォーマット変更にも指示の書き換えだけで追従できるようにする
- S3コネクタと自動化グループを分離して権限を管理し、IAMロールで最小権限アクセスを付与する
- 検証環境で動作確認したワークフローをインポート/エクスポートで本番アカウント・リージョンへ昇格する段階的リリースを採用する

## 使いどころ

- 多様なフォーマットで届く大量の定型文書を毎回人手で構造化しているバックオフィス業務
- カスタムコードを書かずに自然言語だけでデータ抽出パイプラインを立ち上げたいチーム
