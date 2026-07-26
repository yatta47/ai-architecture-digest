---
type: guidance
title: 『チャットで文書に質問』を超える、エージェント型文書ワークフロー(ADW)の実装指針
title_original: 'Beyond Chatbots: Adopting Agentic Document Workflows for Enterprises'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- ai-agent
- human-in-the-loop
components:
- LlamaParse
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/beyond-chatbots-adopting-agentic-document-workflows-for-enterprises
published_at: '2026-07-19'
---

## 概要

LlamaIndexは、単なる文書Q&Aを超えてPDFなど非構造化文書を実処理まで自動化する『Agentic Document Workflow(ADW)』を、Parse→Retrieve→Reason→Actの4段階で定義する。契約書のリスク分析を例に、型付きデータ契約とヒューマン・イン・ザ・ループを組み合わせた実装パターンを示す。

## 設計のポイント

- Parse（構造化抽出）→Retrieve（該当箇所の検索）→Reason（ポリシー適用・推論）→Act（下流システムへの反映）の4段階を、Pydanticなどの型付きメッセージで接続し、各段階の入出力を厳密に契約化する
- 各段階の間に人間によるレビュー・承認ポイントを設け、例外処理や品質担保に人の判断を介在させる
- 業務ロジック（例：まずパースしてから検索する）は明示的にワークフローへ組み込み、要約の生成などLLMの推論が有利な部分は自律性に委ねる
- 複数文書種別・複雑な業務ルール・システムへの書き込み・定期/大量処理のいずれかが該当する場合にのみADWを採用し、単純な検索や単発の要約には過剰実装しない

## 使いどころ

- 夜間に取引先契約書を自動レビューし、リスク条項をCLMシステムへ起票したい法務・調達部門
- 請求書とPOの突合・支払スケジューリングなど大量文書処理を自動化したいバックオフィス
- プライバシー監査や財務デューデリジェンスなど、ポリシー適用を伴う文書処理基盤を構築したいエンタープライズ
