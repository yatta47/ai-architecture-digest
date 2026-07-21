---
type: announcement
title: LangGraphのチェックポイント肥大化を解消するDelta Channels
title_original: 'Delta Channels: How We''re Evolving Our Runtime for Long-Running Agents'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- llmops
components:
- LangGraph
- Deep Agents
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/delta-channels-evolving-agent-runtime
published_at: '2026-06-03'
---

## 概要

LangGraphの標準チェックポイント方式はメッセージ履歴やファイル状態を毎ステップ全量スナップショットするためO(N^2)でストレージが増大し、200ターンのコーディングエージェントでは5.3GBにも達していた。新しいDeltaChannelプリミティブは各ステップで差分のみを保存し、一定間隔（デフォルト50ステップ）ごとにフルスナップショットを書き出すことで、同じワークロードのストレージを129MB（約40倍削減）に抑えつつ、再開レイテンシもほぼ変わらない性能を実現した。

## 設計のポイント

- 累積型の状態フィールド（メッセージ・ファイル）を毎ステップ全量保存せず差分のみ保存するDeltaChannelというチャネル型を新設する
- snapshot_frequency（K）ごとにフルスナップショットを書き込み、復元時に遡る範囲を最大Kステップに限定することで再開レイテンシを一定に保つ
- 既存スレッドやinterrupt・タイムトラベルなどのAPI表面を変えずにデフォルトを差分保存へ切り替え、移行コストなしにアップグレードできるようにする
- snapshot_frequencyを調整可能なパラメータとして公開し、ストレージ削減幅と再開時の差分再生コストをワークロードに応じてトレードオフできるようにする

## 使いどころ

- 数百ステップにわたる長時間実行のコーディングエージェントやリサーチエージェントのチェックポイントコストを抑えたい場合
- ファイルシステムを使ったコンテキストオフロードで状態が肥大化しやすいエージェント基盤の運用
- 観測性・human-in-the-loop・障害復旧を犠牲にせずにエージェント実行基盤のストレージコストを削減したいプラットフォームチーム
