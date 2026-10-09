---
type: case
title: KDD Cup 2026 Data Agents準優勝の制約付きハーネス設計
title_original: 'Building Reliable Data Analytics Agents: Lessons from the KDD Cup'
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- ai-agent
- text-to-sql
- context-engineering
- eval
components:
- SQLite
- NVIDIA Nemotron
- KDD Cup 2026
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/building-reliable-data-analytics-agents-lessons-from-the-kdd-cup/
published_at: '2026-10-08'
---

## 概要

NVIDIA KGMONチームは、固定の小型LLMを使うKDD Cupで、データを単一のSQLiteに統一しschema()とsql()だけを公開するハーネスで準優勝した。事前のスキーマ調査、文書抽出の分離、実行トレースの検査エージェントで信頼性を高めた。

## 設計のポイント

- 構造化データを1つのクエリ面に正規化し、ツールを少数に絞って選択ミスを減らす。
- メインのループ前にスキーマやJOINキーを調べて渡し、探索ターンと誤りを減らす。
- 長い文書は別のゼロ温度LLM呼び出しで抽出し、生の文章をメイン文脈に入れない。
- 実行トレースを検査エージェントで分類し、失敗原因からハーネスを改善する。

## 使いどころ

- 小型オープンモデルでデータ分析エージェントを組むチーム。
- 複数形式のデータにまたがる質問応答の信頼性を上げたい分析基盤担当者。
