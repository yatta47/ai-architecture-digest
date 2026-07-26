---
type: guidance
title: エージェント設計：自律性と構造をどう配分するか
title_original: 'Bending without Breaking: Optimal Design Patterns for Effective Agents'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
- event-driven
components:
- LlamaIndex Workflows
outcome:
  type: reliability
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/bending-without-breaking-optimal-design-patterns-for-effective-agents
published_at: '2026-07-19'
---

## 概要

LlamaIndexは、Anthropicの『Building Effective Agents』・12 Factor Agents・OpenAIの実践ガイドを踏まえ、完全自律のエージェントと厳密なDAG構造の中間にあるハイブリッド設計こそが実用的だと論じる。同社のイベント駆動オーケストレーション基盤『Workflows』を軸に、構造を与えるべき場面と自律性に委ねるべき場面を整理する。

## 設計のポイント

- 入力フォーマットが既知の処理・課金など不可逆で重大な業務ロジック・構造化出力が必要な箇所は、決定的な処理フローとして固定する
- 契約書やメールなど非構造化データの解釈、例外だらけの判断、状況が急変するタスクはLLMの自律的判断に委ねる
- イベント駆動のWorkflowsで各ステップを関数として実装し、分岐・ループ・ファンアウトを組み合わせることで、決定的経路とLLM主導の経路を1つの実行系に混在させる
- 重要な意思決定にはヒューマン・イン・ザ・ループを組み込み、エラー処理やデバッグのしやすさを維持する

## 使いどころ

- エージェントの信頼性・デバッグ性を保ちながら開発したいプロダクトチーム
- 返金判断など『際どい』業務ロジックを一部自動化したいカスタマーサポート部門
- 契約書・請求書など非構造化文書を扱うエンタープライズ向けエージェント開発者
