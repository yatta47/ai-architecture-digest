---
type: case
title: 危機相談員を裏側で支えるRAG+ReActのカウンセラー支援コパイロット
title_original: Counselor Copilot
industry: healthcare
cloud: []
patterns:
- ai-agent
- rag
- human-in-the-loop
- document-processing
components:
- LlamaParse
- LlamaIndex ReAct Agent
- GPT-4
- AstraDB
- Salesforce
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/bridging-the-gap-in-crisis-counseling-introducing-counselor-copilot-db42e26ab4f3
published_at: '2024-02-24'
---

## 概要

ハッカソンで作られた、The Trevor Projectの相談員向けリアルタイム支援の試作。ReActエージェントが会話を監視し、返信案の提示、上長へのエスカレーション提案、地域資源の検索、ケース記録の入力を行う。

## 設計のポイント

- AIは相談者へ直接返信せず、返信案を相談員が編集して送る。
- 相談員のプロンプト入力を不要にし、会話を監視するエージェントがツールを選ぶ。
- 返信案は組織のガイドライン文書をRAGで引いて生成する。
- 緊急性を会話から判定し、人へのエスカレーションを提案する。

## 使いどころ

- 機微な対話を扱う相談窓口やサポート部門。
- 担当者の事務作業を会話中に肩代わりしたい場面。
