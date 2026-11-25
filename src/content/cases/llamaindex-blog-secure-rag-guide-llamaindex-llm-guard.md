---
type: guidance
title: LLM GuardでRAGの取得文書に潜むプロンプトインジェクションを防ぐ
title_original: Secure RAG with LlamaIndex and LLM Guard by Protect AI
company: Protect AI
industry: cross-industry
cloud: []
patterns:
- rag
- guardrails
- defense-in-depth
components:
- LLM Guard
- LlamaIndex
- OpenAI GPT-3.5
outcome:
  type: risk-compliance
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/secure-rag-with-llamaindex-and-llm-guard-by-protect-ai
published_at: '2024-03-20'
---

## 概要

履歴書に白文字で埋め込まれた注入攻撃を例に、LLM GuardでRAGの入力と出力をスキャンして防ぐ方法を示す。

## 設計のポイント

- 取得文書は信頼せず、検索後のノード後処理でインジェクションや秘密情報をスキャンする。
- 可能なら取り込み前にも走査し、外部APIのリアルタイムデータは取得時にも確認する。
- 出力側も同様にスキャンして漏洩や不適切内容を検出する。

## 使いどころ

- 外部から投稿される文書をRAGで扱う採用・審査系システムの開発者。
- LLMアプリのセキュリティ対策を設計する担当。
