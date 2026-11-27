---
type: announcement
title: Zapier NLAで5000超のアプリを操作できるデータエージェント
title_original: Data Agents + Zapier NLA
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- ai-agent
components:
- LlamaIndex
- Zapier NLA
- OpenAIAgent
- Slack
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/data-agents-zapier-nla-67146395ce1
published_at: '2023-07-25'
---

## 概要

LlamaIndexのデータエージェントからZapier NLA経由で5,000以上の外部アプリと3万超の操作を、数行のコードで使えるようになった。

## 設計のポイント

- 個別連携を実装せず、集約サービスを1つのツール仕様として接続する。
- 読み取りだけでなく送信などの操作も同じエージェントに実行させる。

## 使いどころ

- メール要約とSlack通知のような業務自動化を手早く試したい開発者向け。
- 多数のSaaSをまたぐ個人アシスタントの試作。
