---
type: announcement
title: LangSmithがOpenTelemetry形式のトレース取り込みに対応
title_original: Introducing OpenTelemetry support for LangSmith
company: LangChain
industry: cross-industry
cloud: []
patterns:
- llmops
components:
- LangSmith
- OpenTelemetry
- OpenLLMetry
- Traceloop
- Vercel AI SDK
outcome:
  type: reliability
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/opentelemetry-langsmith
published_at: '2026-06-15'
---

## 概要

LangSmithのAPI層がOpenTelemetry形式のトレースを直接取り込めるようになった。OpenLLMetryのセマンティック規約に対応し、標準的なOTelエクスポーターやTraceloop SDK、Vercel AI SDKなど複数の経路からLLM/ベクトルDB/フレームワークの計装をそのままLangSmithに送れる。

## 設計のポイント

- 既存のOpenTelemetry互換SDK・エクスポーターをLangSmithのOTELエンドポイントに向けるだけで計装を再利用できるようにする
- 生成AI向けのセマンティック規約(OpenLLMetry)に対応し、LLM/ベクトルDB/フレームワーク横断で属性名を統一する
- 標準Pythonクライアント・Traceloop SDK・Vercel AI SDKなど複数の統合パスを用意し、既存スタックからの移行コストを下げる

## 使いどころ

- 既存の分散トレーシング基盤やOTel計装をすでに持っているチームがLangSmithにも同じデータを流したい場合
- LangChain以外のフレームワークやOpenAI SDK直呼び出しで構築したLLMアプリのトレースもLangSmithに集約したいチーム
