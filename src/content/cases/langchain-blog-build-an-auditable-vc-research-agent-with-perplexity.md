---
type: case
title: 並列リサーチノードと引用根拠合成でVC投資メモを90秒生成するエージェント
title_original: Build an auditable VC research agent with the Perplexity Agent API, LangGraph, and LangSmith
company: LangChain
industry: financial-services
cloud: []
patterns:
- parallel-execution
- multi-agent-orchestration
- rag
- eval
components:
- Perplexity Agent API
- LangGraph
- LangSmith
- web_search
- finance_search
outcome:
  type: speed
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/build-an-auditable-vc-research-agent-with-the-perplexity-agent-api-langgraph-and-langsmith
published_at: '2026-08-26'
---

## 概要

VCの投資メモ作成を自動化するエージェントで、team/financials/product/marketの4つのリサーチノードをLangGraphで並列実行し、単一のツールなし合成ノードがその結果だけから7セクションの引用付きメモを組み立てる。従来は数十時間かかっていたドラフト作成を約90秒・約0.4ドルで実現し、各主張はLangSmithのトレースで元の検索結果まで遡れる。

## 設計のポイント

- team/financials/product/marketの4ノードを企業名だけを入力にLangGraphでSTARTから並列にfan-outし、各ノードに専用ツール・検索予算・プロンプトを持たせてドメインごとにコンテキストを閉じる。
- 4ノードの並列書き込みが同じstateキーに衝突しないよう、セクション名でマージするreducerを用いて集約し、LangGraphのInvalidUpdateErrorを回避する。
- 合成ノード自体はツールを持たず、リサーチノードが実際に見つけた情報のみから執筆させることで、全ての主張を出典に紐づけ監査可能にする。
- LangSmithのカスタム評価指標（一次情報源率、財務概念のカバレッジ）とコスト・レイテンシを組み合わせ、複数の検索プロバイダを同一グラフ上で比較評価する。

## 使いどころ

- 投資委員会に諮る前のファーストパス投資メモを、アナリストがゼロから書かずに叩き台として使いたいVCファンド。
- 生成された各主張を一次情報源まで遡って検証できる、監査可能性が求められるリサーチ・レポート生成業務。
- 検索プロバイダやツールの選定を勘ではなくLangSmithでの定量評価に基づいて決めたいチーム。
