---
type: guidance
title: Agents SDKにおける入力・出力・ツールガードレールの設計
title_original: Guardrails
industry: cross-industry
cloud: []
patterns:
- guardrails
- ai-agent
components:
- OpenAI Agents SDK
outcome:
  type: risk-compliance
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://openai.github.io/openai-agents-python/guardrails/
published_at: '2025-07-21'
---

## 概要

高性能だが低速・高コストなモデルを使うエージェントに対し、安価で高速なモデルによる入力ガードレールを前段に配置することで、悪意あるリクエストを検知した時点で高コストモデルの実行を止められるという設計を解説する。入力・出力・ツールという3種のガードレールがワークフロー内のどの境界で実行されるかが整理されている。

## 設計のポイント

- 入力ガードレールはチェーンの最初のエージェントのみ、出力ガードレールは最終出力を生成するエージェントのみで実行されるという適用範囲の違いを理解して設計する。
- マネージャーやハンドオフを含むワークフローではエージェント単位の入出力ガードレールだけでなく、関数ツール呼び出し単位のツールガードレールを併用する。
- ブロッキング型ガードレールを使えば、悪意ある入力を検知した時点で高コストモデルの実行前に処理を止めてコストを節約できる。

## 使いどころ

- 高コストな推論モデルを使うエージェントで悪用リクエストによる無駄な課金を防ぎたい場合。
- ハンドオフや複数エージェントを跨ぐワークフローでツール呼び出し単位の安全性検査が必要な場合。
