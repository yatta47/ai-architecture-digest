---
type: announcement
title: Arize AXにJev-as-a-Judgeが統合され、本番トレースを軽量評価
title_original: Evaluate production traces with Jev-as-a-Judge directly in Arize AX
company: Arize AI
industry: cross-industry
cloud: []
patterns:
- eval
- llmops
- guardrails
components:
- Arize AX
- TypeSafe AI Jev
- Claude Opus 5
outcome:
  type: cost
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/arize-ax-jev-as-a-judge/
published_at: '2026-09-28'
---

## 概要

Arize AXがTypeSafe AIの決定モデルJevと統合し、真偽・選択・スコアの質問で本番トレースを評価できるようになった。幻覚検知の検証では、閾値を調整したJevがClaude Opus 5と同じ87%の精度を約300分の1のコスト・23倍の速度で示したが、既定の閾値では大きく劣った。

## 設計のポイント

- 基準が明確で結果が固定の評価には決定モデルを使い、説明が要る場合はLLM判定、調査が要る場合はエージェント判定と使い分ける。
- 人手ラベルで閾値を調整してから展開する。
- 評価コストを下げて、より多くの本番トラフィックを評価する。

## 使いどころ

- 本番エージェントの品質を大量のトレースで監視したい運用チーム。
- LLM判定のコストや遅延が課題の評価基盤担当者。
- 低遅延のガードレールを検討している開発者。
