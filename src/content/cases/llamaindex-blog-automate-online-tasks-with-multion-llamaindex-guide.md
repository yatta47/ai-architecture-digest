---
type: guidance
title: MultiOnとLlamaIndexでメールとWeb操作を自動化するエージェント
title_original: Automate online tasks with MultiOn and LlamaIndex
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- ai-agent
components:
- MultiOn
- LlamaIndex
- OpenAIAgent
- Gmail
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/automate-online-tasks-with-multion-and-llamaindex
published_at: '2024-05-23'
---

## 概要

Webブラウザを自然言語で操作するMultiOnをLlamaIndexのエージェントに組み込み、Gmail検索と合わせてメール対応を自動化するチュートリアル。

## 設計のポイント

- Web操作ツールと情報取得ツールを分けて与え、エージェントに文脈収集と実行を組み合わせさせる。
- 大きな取得結果はオンデマンドローダーで包み、クエリに応じて処理してから返す。

## 使いどころ

- メール確認や返信下書きなどの定型Web作業を自動化したい開発者。
- ブラウザ操作エージェントの試作をする人。
