---
type: guidance
title: 履歴書束から構造化データを抽出するバックオフィスエージェントの構築
title_original: Building Back-Office Agents with LlamaCloud and LlamaAgents
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- ai-agent
- multi-agent-orchestration
- human-in-the-loop
components:
- LlamaParse
- LlamaSplit
- LlamaClassify
- LlamaExtract
- LlamaAgents Workflows
- Pydantic
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/building-back-office-agents-with-llamacloud-and-llamaagents
published_at: '2026-07-19'
---

## 概要

LlamaIndexが、請求書・履歴書・契約書など複数文書が連結されたPDFを対象に、LlamaSplitでページ分割、LlamaExtractでPydanticスキーマに沿った構造化抽出、LlamaAgents Workflowsでオーケストレーションする一連のバックオフィス自動化アーキテクチャを解説している。100ページの履歴書束から個々の候補者データを抽出する具体例で実装手順を示す。

## 設計のポイント

- 人間向けに整形された多様なレイアウトの文書をLLMが処理できる形式に変換してから処理する
- LlamaSplitでカテゴリ定義に基づきページ範囲を検出し、複数文書が混在したPDFを個別文書に分割する
- 抽出したいフィールドをPydanticスキーマとして明示し、信頼度スコア付きで構造化データを取得する
- ファンアウト/ファンイン・自己反省・human-in-the-loopなどのワークフローパターンをLlamaAgentsで組み合わせて並列処理する

## 使いどころ

- 大量の請求書・購入注文書を分割・検証・部門ルーティングしたい経理/購買部門
- 数百件規模の履歴書束から候補者データを構造化抽出したいHR/採用チーム
- 契約種別の分類や非標準条項の検出を自動化したい法務チーム
