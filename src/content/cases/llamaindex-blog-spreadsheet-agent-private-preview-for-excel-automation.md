---
type: announcement
title: 強化学習でスプレッドシート構造を解析するExcel自動化エージェント
title_original: Introducing the Spreadsheet Agent in Private Preview
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- reinforcement-learning
- document-processing
- ai-agent
components:
- LlamaIndex Spreadsheet Agent
- GPT-4.1
- GPT-4o
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-the-spreadsheet-agent-in-private-preview
published_at: '2026-07-19'
---

## 概要

監査・税務・保険等で大量に発生する複雑なExcelファイルの正規化と質問応答を、テキスト化やコードインタプリタに頼らず解決する『Spreadsheet Agent』のプライベートプレビューを発表。強化学習でシート内の暗黙的な構造（結合セル・見出しの位置関係など）をセマンティックマップ化し、専用ツールを持つサブエージェントが計算・変換を行うアーキテクチャにより、OpenAI Code Interpreterを上回る96.1%の精度を達成した。

## 設計のポイント

- スプレッドシートをテキストやCSVに単純変換せず、視覚的レイアウトを踏まえた『パース→推論』の2段階アーキテクチャにする
- 構造解析自体を強化学習の問題として学習させ、条件分岐の積み重ねに頼らない頑健な構造理解を実現する
- 汎用LLM推論に計算を任せず、算術・集計専用ツールを持つサブエージェントに正確な計算を担わせて精度を確保する

## 使いどころ

- 監査法人や保険業界など、大量かつフォーマットが不揃いなExcelファイルを扱う業務担当者
- コード生成やRAGでは精度が出ない複雑な財務スプレッドシートの自動処理を検討している場合
