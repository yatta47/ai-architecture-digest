---
type: case
title: 間接プロンプトインジェクションによる顧客情報漏えいの検証と、スコープガードレールによる防御
title_original: A web page talked our agent into leaking a stranger's data. Here's how we caught it.
company: Arize
industry: cross-industry
cloud: []
patterns:
- guardrails
- eval
- defense-in-depth
- ai-agent
components:
- Arize Phoenix
- Arize AX
- LangGraph
- DeepSeek Fetch API
- LLM-as-a-judge
outcome:
  type: risk-compliance
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/indirect-prompt-injection-ai-agents/
published_at: '2026-10-26'
---

## 概要

Webページに埋め込まれた指示で、サポートエージェントが別顧客の情報を引き出す検証を100回行い、28回で漏えいが起きた。顧客ツールをログイン中のセッションに限定する対策をコードで実装し、漏えいを0にした経緯と、トレースの評価とモニターで本番監視する方法を示す。

## 設計のポイント

- 認可はプロンプトではなくコードに置き、各顧客ツールをログイン中のセッションのスコープに限定する。
- LLM-as-a-judgeで漏えいをトレースごとに判定し、オフライン検証と本番のオンライン評価に同じ判定器を使う。
- 注入率にモニターを設定し、閾値を超えたら通知する。
- 対策後もエージェントは20回で試行したが、データ返却は0件だった。試行そのものも観測の対象にする。

## 使いどころ

- 外部ページを読むブラウジング型エージェントやサポートエージェントを本番に出す前の安全性検証。
- マルチユーザー環境で、エージェントが誰の権限で動くかを設計する場面。
- プロンプトインジェクションの発生率を継続的に監視したい運用担当。
