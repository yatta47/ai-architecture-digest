---
type: case
title: LangSmith LLM Gatewayで実現したコーディングエージェント支出の予測可能化
title_original: How We Made Coding Agent Spend Predictable
company: LangChain
industry: cross-industry
cloud: []
patterns:
- llm-gateway
- cost-optimization
components:
- LangSmith LLM Gateway
- Claude Code
- Codex
- LangChain Deep Agents
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-we-made-coding-agent-spend-predictable
published_at: '2026-06-15'
---

## 概要

全社的にコーディングエージェント利用が急拡大したLangChainが、LangSmith LLM Gatewayを構築し組織/ワークスペース/ユーザー/APIキー単位で予算上限を設定。Claude CodeやCodex等の主要エージェント呼び出しを中央のGateway経由に統一し、支出の可視化と暴走支出の防止を両立した。

## 設計のポイント

- 組織/ワークスペース/ユーザー/APIキーの複数階層で予算を設定し、コーディングエージェントの暴走支出を防ぐ
- 全社のコーディングエージェント呼び出しを中央集権的なLLM Gatewayに通し、MDM経由で個別セットアップなしに展開する
- 上限に達したら止めるだけでなく、閾値前のアラートと監査可能な予算引き上げフローを用意し業務を止めないようにする

## 使いどころ

- 複数チームがコーディングエージェントを使い支出が見えにくくなっている組織
- モデル料金体系が複雑でコスト計算が陳腐化しやすい環境
