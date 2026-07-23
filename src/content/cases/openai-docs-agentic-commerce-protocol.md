---
type: guidance
title: AIエージェント商取引プロトコル(ACP)の構築ガイド
title_original: Build with the Agentic Commerce Protocol
company: OpenAI
industry: retail
cloud: []
patterns:
- ai-agent
components:
- Agentic Commerce Protocol
outcome:
  type: revenue
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/commerce/
published_at: '2025-09-29'
---

## 概要

本ページはOpenAIが提供するAgentic Commerce Protocol(ACP)の導入ドキュメントで、AIエージェントが商品を発見・購入できるようにするための基本resourcesをまとめている。ガイド付きウォークスルーとサンプルペイロードで最初の統合を素早く立ち上げ、商品コピー・バリエーションモデリング・アトリビューションに関するベストプラクティスでフィード品質を高める構成になっている。

## 設計のポイント

- 最初の統合はガイド付きウォークスルーとサンプルペイロードを用意し、実装の立ち上げコストを下げる。
- 商品フィードの品質(商品コピー・バリエーションモデリング)を別建ての指針として整理し、AIエージェントが正確に商品を解釈できるようにする。
- 購入経路のアトリビューションを設計要素として明示し、エージェント経由の取引を追跡可能にする。

## 使いどころ

- 自社の商品をAIショッピングエージェントに露出させたい小売・ECサイト運営者。
- ACPへの最初の統合を短期間で実装したい開発者。
- エージェント経由の商品フィード品質やコンバージョン計測を改善したいコマース担当者。
