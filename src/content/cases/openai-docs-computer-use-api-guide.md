---
type: guidance
title: 画面操作エージェント(CUA)を安全に動かす3つのハーネス構成
title_original: Computer use guide
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
components:
- Responses API
- Computer Use API
- Playwright
- Docker
outcome:
  type: risk-compliance
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/tools-computer-use
published_at: '2025-07-18'
---

## 概要

OpenAIのComputer Use(CUA)ガイドは、モデルがスクリーンショットを見てクリックやタイピングなどのUI操作を返す仕組みを、ブラウザ自動化・VM・コード実行の3種類のハーネスとして実装する方法をまとめる。いずれの構成でも隔離環境の準備と人間によるハイリスク操作の承認を前提とし、ページ内容は信頼できない入力として扱うことを求める。

## 設計のポイント

- ブラウザ拡張・ファイルシステムアクセスを無効化し、空のenvでプロセスを起動するなど、エージェントの実行環境を隔離してブラスト半径を制限する。
- 組み込みのcomputer toolによるネイティブ操作、既存Playwright/Selenium/VNCハーネスへのカスタムツール接続、コード実行環境の3パターンから要件に応じて選ぶ。
- スクリーンショットやページテキストなど画面から得た情報はすべて信頼できない入力として扱い、ユーザーの直接指示のみを権限根拠とする。
- 口座情報や医療情報など高リスクな認証済み環境には現状のCUAを向けず、重要操作の前段に人間の承認ステップを挟む。

## 使いどころ

- 既存のPlaywright/Seleniumベースの自動化基盤にAIによるUI操作判断を組み込みたいチーム。
- ブラウザ操作エージェントをプロトタイプから本番運用に近づける際に、安全なサンドボックス設計を検討している開発者。
- デスクトップ操作を含むフルVM環境でエージェントを動かす必要があるユースケース。
