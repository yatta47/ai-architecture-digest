---
type: guidance
title: Evalsが見逃す本番エージェントの軌跡的失敗をArize Signalで発見する
title_original: How to find and debug agent failures your evals are missing
company: Arize
industry: cross-industry
cloud: []
patterns:
- eval
- llmops
- root-cause-analysis
- human-in-the-loop
components:
- Arize AX
- Signal
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/how-to-find-and-debug-agent-failures-your-evals-are-missing/
published_at: '2026-09-17'
---

## 概要

Arizeは、既知のリスクしか検知できない従来のeval・監視の限界を補うAIワーカー「Signal」を紹介している。Signalは本番のエージェント実行トレースを定期的にレビューし、ツール引数の誤り・無駄なリトライ・実行されていないのに完了したと見える結果など、事前に想定されていなかった再発パターンをグルーピングして根本原因・影響・エビデンス付きの調査レポートにまとめる。発見された問題は回帰データセットや専用エバリュエータへと昇格させ、次のリリース前のテストに組み込む運用ループを提案する。

## 設計のポイント

- 出力だけを採点するアウトプット判定ではなく、ツール呼び出しや状態変化を含む実行トレース全体を評価対象にする
- コード評価・LLM-as-a-Judge・Agent-as-a-Judge・Signalを役割の異なるレイヤーとして併用し、既知/未知の失敗を分業して扱う
- 類似トレースを横断的にグルーピングし、単発インシデントではなく再発パターンとして優先度付けする
- 発見された失敗を代表例として回帰データセットに保存し、専用テストへ昇格させて継続的に監視対象を広げる

## 使いどころ

- レイテンシやステータスコードは正常でも、実際には意図した処理が完了していないエージェント障害を検知したいチーム
- 数百万件規模のトレースから人手でパターンを見つけるのが非現実的な本番エージェント運用
- eval網羅範囲を継続的に拡張し、未知の失敗モードをリリース前テストに反映させたいAIプラットフォームチーム
- 既知の失敗は軽量な自動チェックに任せ、未知の失敗発見にリソースを集中させたい運用体制
