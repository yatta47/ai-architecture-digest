---
type: case
title: LangSmithの権限設定・トレース・評価を監査証跡にしたISO/IEC 42001認証取得
title_original: How We Achieved ISO 42001 with LangSmith
company: LangChain
industry: cross-industry
cloud: []
patterns:
- llmops
- eval
- human-in-the-loop
- guardrails
components:
- LangSmith
- LangSmith Fleet
- Deep Agents
- Security Agent
- Prompt and Context Hub
outcome:
  type: risk-compliance
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/ai-governance-iso-iec-42001-langsmith
published_at: '2026-11-25'
---

## 概要

LangChainはAIマネジメントシステム規格ISO/IEC 42001の認証を、LangSmithを使って取得した。エージェントの権限・承認設定と、日常のデバッグに使うトレース・評価をそのまま監査証跡にした。

## 設計のポイント

- ワークスペース権限・エージェント設定・ツール単位の自動実行/承認の3層で権限を定義し、重要操作は人の承認を必須にする。
- 評価はデータセットと評価器を固定し、空回答で通るテストを除くなど評価自体も検証する。
- 承認の中断と再開を含む実行全体をトレースに残し、後から再構成できるようにする。

## 使いどころ

- AIエージェントのガバナンスや認証対応を進める企業。
- 監査向けの証跡を開発プロセスから自然に得たいプラットフォームチーム。
