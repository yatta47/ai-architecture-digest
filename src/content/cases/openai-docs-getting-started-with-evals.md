---
type: guidance
title: ダッシュボードのDatasets機能で始めるモデル出力の評価(eval)
title_original: Getting started with evals
industry: cross-industry
cloud: []
patterns:
- eval
components:
- OpenAI Evals
- Datasets
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/evaluation-getting-started
published_at: '2025-08-13'
---

## 概要

モデル出力が期待するスタイル・内容基準を満たすかを検証するeval(評価)の始め方を解説する。ダッシュボードのDatasets機能でデータセットを作成し、実運用で見つかったエッジケースを継続的に追加していく運用を推奨している。

## 設計のポイント

- データセットを一度作って終わりにせず、実運用で見つかったエッジケースやブラインドスポットを継続的に追加する『生きた』空間として扱う
- ビジュアルなデータ追加とCSV/既存プロンプトの取り込みの両方をサポートし、evalの立ち上げコストを下げる

## 使いどころ

- LLMアプリの出力品質をプロンプト変更前後で比較検証したいチーム
- 投資メモ生成のような具体的なユースケースでeval運用を初めて構築する開発者
