---
type: announcement
title: 文書の該当箇所を自動引用するAnthropic APIのCitations機能
title_original: Introducing Citations on the Anthropic API
industry: cross-industry
cloud: []
patterns:
- rag
- document-processing
components:
- Claude 3.5 Sonnet
- Claude 3.5 Haiku
- Amazon Bedrock
- Vertex AI
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/introducing-citations-api
published_at: '2025-06-23'
---

## 概要

Anthropic APIに、Claudeが回答生成に使った原文の該当パッセージを自動的に引用する「Citations」機能が追加された。プロンプトエンジニアリングに頼らずハルシネーションを抑え出典を明示できるようになり、Thomson ReutersのCoCounselやEndexの金融リサーチAIエージェントで採用されている。

## 設計のポイント

- ソース文書を文単位にチャンク化してモデルに渡し、生成した主張ごとに元文への参照を自動付与する
- 引用に使われた出力トークンは課金対象外にすることで、出典明示のコスト負担を軽減する

## 使いどころ

- 長文文書の要約で各要点の出典を明確にしたい場合
- 複数文書にまたがる複雑なQ&Aで回答の根拠を追跡可能にしたい法務・金融分野のアプリケーション
