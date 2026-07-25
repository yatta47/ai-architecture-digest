---
type: guidance
title: OpenTelemetryで実現する多段階ドキュメントエージェントの可観測性
title_original: Observability in Agentic Document Workflows
industry: financial-services
cloud: []
patterns:
- document-processing
- ai-agent
- root-cause-analysis
components:
- LlamaIndex Agent Workflows
- LlamaExtract
- LlamaClassify
- OpenTelemetry
- Jaeger
- llamactl
outcome:
  type: reliability
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/observability-in-agentic-document-workflows
published_at: '2026-07-19'
---

## 概要

損益計算書・貸借対照表・キャッシュフロー計算書を分類・抽出・検証する財務文書パイプラインを例に、LlamaIndex Agent WorkflowsにOpenTelemetryとJaegerによるトレーシングを組み込み可観測性を確保する方法を解説している。非決定的なAI判断が絡む多段階処理では、print文によるデバッグではなく構造化されたトレースが不可欠だとしている。

## 設計のポイント

- ステップごとにイベントを発行するイベント駆動アーキテクチャがOpenTelemetryのspan/traceモデルに自然に対応し計装しやすい
- 分類→抽出→検証→振り分けの各ステップをトレースし、どの段階で判断ミスやデータ欠落が起きたかを可視化する
- カスタムイベントトレースを追加することで、業務固有の粒度でのモニタリングを可能にする

## 使いどころ

- 請求書・財務諸表など多段階のAI判断を伴うドキュメントパイプラインを本番運用しデバッグ性を高めたいチーム
- 分類ミスや抽出漏れの原因究明を非決定的なLLM処理の中で行う必要がある場合
