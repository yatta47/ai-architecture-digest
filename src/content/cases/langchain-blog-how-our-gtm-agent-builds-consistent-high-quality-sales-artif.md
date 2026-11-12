---
type: case
title: LangChain社内GTMエージェントが営業資料を一貫した品質で生成する
title_original: How our GTM Agent builds consistent, high-quality sales artifacts
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
components:
- Deep Agents
- Managed Deep Agents
- LangChain
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/gtm-agent-high-quality-sales-artifacts
published_at: '2026-11-12'
---

## 概要

LangChain社内のGTMエージェントが、アカウントプランやPoV文書、提案資料などの営業成果物を生成する。品質の多くは営業リーダーの好み、顧客通話の文脈、営業ステージなどのビジネスコンテキストから生まれ、送付された案件は次ステージへ進む割合が47%対16%だった。

## 設計のポイント

- プロンプト調整よりも、営業の型・通話内容・ステージ要件といったコンテキストを与えることに投資する。
- サンドボックス・スキル・メモリ・定期実行のプリミティブ上に構築する。
- 案件の進捗を把握し、顧客通話前に適切な文書を提案する。

## 使いどころ

- 提案資料作成に時間を取られる営業組織。
- 自社の業務ノウハウをエージェントに組み込みたいチーム。
- エージェントの効果を案件成果で測りたい企業。
