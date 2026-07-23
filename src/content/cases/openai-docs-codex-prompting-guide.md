---
type: guidance
title: コーディングエージェントCodexのためのプロンプト設計ガイド
title_original: Codex Prompting Guide
company: OpenAI
industry: cross-industry
cloud: []
patterns:
- ai-agent
- prompt-optimization
components:
- gpt-5.3-codex
- Codex CLI
- apply_patch
outcome:
  type: productivity
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide/
published_at: '2026-02-25'
---

## 概要

自律的に長時間コーディングを続けるgpt-5.3-codexモデルから最大の性能を引き出すためのプロンプト設計指針を解説する。推奨システムプロンプトのひな形、ツール優先順位の明示、途中経過報告の削除など、既存のエージェントハーネスを移行する際の具体的な変更点を示す。

## 設計のポイント

- 計画や途中経過を都度報告させるプロンプトを外し、タスク完了までノンストップで自律実行させることで作業の中断を防ぐ
- 検索やファイル読み込みなど専用ツールが存在する操作は生シェルコマンドより優先させ、並列化できるツール呼び出しは逐次実行せず並列にする
- エラーを握りつぶす広範なtry/catchを禁止し、根本原因への対応と型安全性の維持をプロンプトレベルで明示的に要求する

## 使いどころ

- 既存のGPT-5系プロンプトをCodexチューニングモデル向けに移行したいエージェント開発チーム
- 数時間にわたる自律的なコーディングタスクをコンパクション機能を使って実行させたい場合
