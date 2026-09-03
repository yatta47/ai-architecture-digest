---
type: case
title: Schneider Electric・Vodafone・monday.comに学ぶエージェント運用基盤の作り方
title_original: 'Scaling Agents in Europe & The Middle East: Lessons from Schneider Electric, Vodafone, and monday.com'
company: Schneider Electric / Vodafone / monday.com
industry: cross-industry
cloud:
- multi-cloud
patterns:
- llmops
- multi-agent-orchestration
- eval
- guardrails
components:
- LangSmith
- LangGraph
- LangSmith Fleet
outcome:
  type: reliability
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/scaling-agents-in-europe-the-middle-east-lessons-from-schneider-electric-vodafone-and-monday-com
published_at: '2026-09-03'
---

## 概要

欧州・中東地域で複数のエージェントを本番運用する3社の事例を紹介する記事。Schneider Electricは350人規模のAIハブでLangSmithによるLLMOpsを60以上のエージェントに適用し、monday.comは単一の汎用エージェントからサブエージェント群への再設計を行い、VodafoneはLangGraph上に2つの本番アシスタントを構築しLangSmithで監視している。共通するのは個別エージェントではなく中央のプラットフォーム層への投資という傾向。

## 設計のポイント

- 単発のエージェント構築ではなく、観測性・評価・デプロイを支える中央プラットフォーム層に投資し乱立するPoCを本番導線に統合する
- ツールを増やすほどエージェントの精度が落ちるという知見から、単一の汎用エージェントを責務分離したサブエージェント＋サンドボックス構成に再設計する
- LLMゲートウェイを導入し、ユーザー・モデル・トークン・支出・ポリシーを横断して可視化してから自律性を広げる
- 非エンジニアがガードレール付きでエージェントを設定できるようローコード基盤を用意しつつ、実用化されたものはエンジニアが本格実装する

## 使いどころ

- 数十件のエージェントPoCが散在し本番導線がない大企業のAI基盤整備
- 規制の厳しい書類・バックオフィス業務（請求書・保険金請求・調達）へのエージェント適用
- 監査義務のあるリスク・コンプライアンス・セキュリティ運用でのアナリスト負荷削減
