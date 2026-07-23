---
type: guidance
title: マルチエージェント・オーケストレーションパターンの選び方
title_original: AI agent orchestration patterns
industry: cross-industry
cloud:
- azure
patterns:
- multi-agent-orchestration
- ai-agent
components: []
outcome:
  type: quality
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
published_at: '2026-02-12'
---

## 概要

Azure Architecture Centerによるマルチエージェント・オーケストレーションのガイド。単一モデル呼び出し、ツール付き単一エージェント、マルチエージェント編成という複雑さの段階を示し、要件を満たす最小限のレベルを選ぶことを推奨する。代表パターンである逐次(シーケンシャル)オーケストレーションを取り上げ、各エージェントが前段の出力を処理するパイプライン構成が契約書生成のような線形依存を持つワークフローに適することを解説している。

## 設計のポイント

- 必要な複雑さのレベルに留め、プロンプトエンジニアリングだけで解決できるならエージェント化しない
- 単一エージェント+ツールをエンタープライズのデフォルトとし、無限ループ防止のため反復回数の上限を設定する
- マルチエージェント化はドメイン横断・セキュリティ境界分離・並列特化が必要な場合にのみ採用し正当化する
- 逐次オーケストレーションは並列化できず段階的な品質向上（ドラフト→レビュー→仕上げ）が必要な場合に選ぶ

## 使いどころ

- 契約書生成など、ドラフト作成・レビュー・仕上げの明確な線形依存を持つ文書処理ワークフロー
- 単一エージェントではツール過多やプロンプト複雑化で対応しきれない複数ドメイン横断タスク
- 各エージェントに異なるセキュリティ境界を設ける必要があるワークロード
- 並列化不可能で各段階の可用性・性能特性が事前に把握できているシステム
