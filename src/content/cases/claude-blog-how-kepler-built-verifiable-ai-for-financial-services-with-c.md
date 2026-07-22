---
type: case
title: Kepler:2600万件超のSEC提出書類を出典まで検証可能なAIで解析する金融リサーチ基盤
title_original: How Kepler built verifiable AI for financial services with Claude
company: Kepler
industry: financial-services
cloud:
- aws
patterns:
- document-processing
- context-engineering
- human-in-the-loop
- multi-model-routing
components:
- Claude
- AWS
- Rust
- Python
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-kepler-built-verifiable-ai-for-financial-services-with-claude
published_at: '2026-04-30'
---

## 概要

2025年創業のKeplerは、SEC提出書類2600万件超・企業14,000社超・27市場をわずか3か月でインデックスし、アナリストが自然言語で質問すると出典の提出書類・ページ・行項目まで遡って検証可能な回答を返す金融リサーチ基盤Kepler Financeを構築した。Claudeを解釈・推論のステージに据えつつ、比率計算など正確性が求められる操作は決定論的な実行環境に委譲し、独自の財務オントロジーで用語の曖昧さを解消している。

## 設計のポイント

- Claudeを推論・解釈のステージとして使い、計算や指標算出など厳密な正確性が要求される処理は決定論的な実行環境に委譲する
- 財務概念を厳密な定義・数式にマッピングする独自オントロジーを構築し、指標の曖昧さを解消する
- ワークフローを複数ステージのパイプラインに分解し、ステージの難易度に応じて異なるClaudeモデルを割り当てる
- 用語や前提が曖昧な場合はモデルに処理を止めさせてアナリストに判断を委ねるhuman-in-the-loopを設計する

## 使いどころ

- 規制産業で監査可能性が求められるAIリサーチツールを構築したい金融機関やスタートアップ
- 自然言語の質問を多段階の計算・データ参照に分解し、数値の出典まで追跡可能にしたい場合
