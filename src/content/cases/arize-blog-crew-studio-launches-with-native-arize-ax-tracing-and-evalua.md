---
type: announcement
title: CrewAIのCrew Studioがトレースなしで最初からArize AXと連携する
title_original: Crew Studio launches with native Arize AX tracing and evaluation
company: CrewAI
industry: cross-industry
cloud: []
patterns:
- ai-agent
- eval
- llmops
components:
- CrewAI
- Crew Studio
- Arize AX
- OpenTelemetry
- OpenInference
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/crew-studio-arize-ax-tracing-evaluation/
published_at: '2026-08-13'
---

## 概要

エージェント自動構築ツールCrew StudioがArize AXとネイティブ統合し、独自の計装コードなしに最初の実行からトレースを送信できるようになったことを発表。OpenTelemetry GenAIセマンティック規約への準拠により、トレース・オンライン評価・ラベリング・実験までを一つのフィードバックループとして提供する。

## 設計のポイント

- OpenTelemetry GenAIセマンティック規約に準拠することで、カスタム計装コードなしにトレースをArize AXへ直接送信できる
- 本番トラフィックへのオンライン評価で品質問題をユーザー報告より先に検知し、フラグ付きトレースを人手のラベリングキューへ回す
- ラベリングで得たground truthデータセットを実験に使い、修正をデプロイ前に検証する『トレース→評価→改善→再デプロイ』のループを回す

## 使いどころ

- ノーコードでエージェントを構築する現場担当者と、ガバナンスを担うプラットフォームチームの両方を支援したい組織
- 本番投入後のエージェント障害調査（どのステップが失敗しコストはいくらか）を高速化したいチーム
