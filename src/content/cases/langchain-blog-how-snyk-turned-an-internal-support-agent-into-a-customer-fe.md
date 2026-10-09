---
type: case
title: 社内サポート用エージェントをSnyk Assistとして製品機能化
title_original: How Snyk turned an internal support agent into a customer feature
company: Snyk
industry: cross-industry
cloud: []
patterns:
- ai-agent
- eval
- guardrails
- unified-runtime
components:
- LangChain
- LangGraph
- LangSmith
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-snyk-turned-an-internal-support-agent-into-a-customer-feature
published_at: '2026-10-09'
---

## 概要

Snykは社内サポートの振り分け用エージェントを、サポートポータル、さらにコア製品へと段階的に展開し、全有償顧客向けのSnyk Assistにした。単一のLangGraphランタイムをSlack・Web・APIに共通で使い、権限内の情報だけを返す設計とLangSmith評価で品質を担保した。

## 設計のポイント

- 同じエージェントランタイムのまま、社内、ポータル、製品と公開面だけを段階的に広げる。
- ユーザー権限を超える情報を返さないことを製品要件として扱い、権限制御を設計に組み込む。
- トレースを評価セットに取り込み、基準を満たさない変更は出荷しない。
- 問い合わせ起票や機能要望の記録など、会話から実行できるアクションを持たせる。

## 使いどころ

- 顧客向けのAI機能を、まず社内で検証してから展開したいSaaS事業者。
- 権限管理が厳しい製品にエージェントを組み込む開発チーム。
