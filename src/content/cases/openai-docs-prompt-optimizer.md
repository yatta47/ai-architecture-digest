---
type: guidance
title: データセットの評価結果からプロンプトを自動改善するプロンプトオプティマイザ
title_original: Prompt optimizer
industry: cross-industry
cloud: []
patterns:
- prompt-optimization
- eval
components:
- Datasets
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/prompt-optimizer
published_at: '2025-08-13'
---

## 概要

ダッシュボード上のチャット型インターフェースで、プロンプトを現行のベストプラクティスに沿って自動最適化するプロンプトオプティマイザを解説する。評価データセットのアノテーションやグレーダー結果と組み合わせることで改善を自動化する。

## 設計のポイント

- Good/Badのアノテーションと具体的な批評コメント、グレーダー結果の3種のシグナルをプロンプト改善の入力として使う
- 望ましいプロンプトの性質を正確に捉えるグレーダーを事前に用意し、最適化の目的関数として機能させる

## 使いどころ

- 手作業でのプロンプトチューニングを評価データ駆動の反復プロセスに置き換えたいチーム
- 既存のevalデータセットを活用してプロンプト改善を自動化したい開発者
