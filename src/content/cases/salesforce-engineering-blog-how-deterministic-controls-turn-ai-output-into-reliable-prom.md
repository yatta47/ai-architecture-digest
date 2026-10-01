---
type: case
title: Agent Graphで決定的に制御するPrompt Builderのテンプレート自動生成
title_original: How Deterministic Controls Turn AI Output into Reliable Prompt Templates
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- ai-agent
- guardrails
- context-engineering
- human-in-the-loop
components:
- Salesforce Prompt Builder
- Agentforce
- Agent Graph
- Einstein Search
outcome:
  type: productivity
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/how-deterministic-controls-turn-ai-output-into-reliable-prompt-templates/
published_at: '2026-09-30'
---

## 概要

SalesforceのPrompt BuilderのAssistive Authoringで、自然言語の依頼から根拠付きプロンプトテンプレートを1分未満で生成する仕組みの事例。Agent Graphのルーターと専門ノード、4つのバックエンドツールで、ルーティング、レコードID、出力契約をLLMに任せず決定的に制御している。熟練管理者で25分以上かかった作業が約25倍速くなったとされる。

## 設計のポイント

- ルーターが生成・改良・非作成入力の3つのサブエージェントへ振り分け、LLMの意図表明を決定的ガードで検証してから遷移する。
- LLMには安定した開発者名で内容を生成させ、サーバ側のtranspose層でIDを再付与して不透明な識別子の破損を防ぐ。
- テンプレートメタデータをセンチネルタグで囲み、クライアントはタグ内のみ取り出して解析し、失敗時は推測せずエラーにする。
- beforeReasoningフックで根拠を事前取得し、モデル判断とツール往復を減らして遅延を下げる。

## 使いどころ

- 非決定的なLLMを業務システムに組み込み、ID整合性や出力形式を保証したい場面。
- 自由入力欄から複数の処理経路へ分岐するエージェントの設計。
- 管理者承認を挟みつつ生成を自動化するノーコード系ツール。
