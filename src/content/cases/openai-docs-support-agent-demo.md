---
type: guidance
title: AIが下書きし人間が確定するHuman-in-the-Loop型カスタマーサポートエージェント
title_original: Customer Support Agent with Human in the Loop Demo
company: OpenAI
industry: cross-industry
cloud: []
patterns:
- human-in-the-loop
- rag
- document-processing
components:
- Responses API
- File Search
- Vector Store
outcome:
  type: productivity
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://github.com/openai/openai-support-agent-demo
published_at: '2025-07-18'
---

## 概要

OpenAI Support Agent Demoは、ファイル検索(RAG)で作った回答案をカスタマーサポート担当者向け画面に「提案」として表示し、担当者が編集・承認してから顧客に送る構成のHuman-in-the-Loop(HITL)デモ。注文キャンセルなど機微なアクションは提案のみに留め、非機微な操作だけ自動実行する。

## 設計のポイント

- ナレッジベースへのファイル検索から得た回答をそのまま送信せず、必ず人間の担当者が確認・編集できる「提案」として提示する。
- アクションを機微度で区分し、注文キャンセルなど影響の大きい操作は提案どまり、影響の小さい操作(注文履歴取得など)のみ自動実行を許可する。
- 回答の根拠となったナレッジベース記事へのリンクを表示し、担当者が回答の妥当性をその場で検証できるようにする。

## 使いどころ

- AIによる自動応答を全面採用する前に、まず提案+人間承認のフローで安全に導入したいサポート部門。
- 機微なアクションと非機微なアクションを分けて自動化範囲を段階的に広げたい場合。
