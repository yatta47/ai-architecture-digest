---
type: guidance
title: 履歴書抽出・Generative UI・会話アシスタントで見るStructured Outputsの実装例3選
title_original: Structured Outputs Sample Apps
company: OpenAI
industry: cross-industry
cloud: []
patterns:
- structured-outputs
components:
- Structured Outputs
- Next.js
outcome:
  type: productivity
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://github.com/openai/openai-structured-outputs-samples
published_at: '2025-07-18'
---

## 概要

Structured Outputsのサンプルアプリ集で、履歴書の情報抽出、スキーマに基づくUIコンポーネントの動的生成(Generative UI)、ツール呼び出しとGenerative UIを組み合わせたマルチターン会話アシスタントという3つの実装パターンをNext.jsで示す。

## 設計のポイント

- 抽出・生成UI・会話アシスタントという難易度の異なる3段階のサンプルを用意し、Structured Outputsの適用範囲を段階的に理解できるようにする。
- Generative UIサンプルでは、モデルが返すスキーマ準拠のJSONをそのままUIコンポーネントのpropsにマッピングし、動的なUI生成を実現する。

## 使いどころ

- 非構造テキストからの情報抽出をStructured Outputsで実装したい場合。
- モデル出力からUIコンポーネントを動的に組み立てるGenerative UIパターンを試したい場合。
