---
type: opinion
title: ファイルシステム型エージェントとベクトル検索RAGの使い分け（LlamaIndexニュースレター 2026-01-20）
title_original: LlamaIndex Newsletter 2026-01-20
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- ai-agent
- rag
- context-engineering
- eval
components:
- LlamaParse
- LlamaSheets
- MCP
- Claude Agent SDK
- FunctionAgent
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2026-01-20
published_at: '2026-01-20'
---

## 概要

コーディングエージェントがファイルシステムを中核の抽象に据える流れと、エージェント型ファイル探索対RAGの比較実験を紹介する週次ニュースレター。RAGは約3.8秒速く、ファイル探索エージェントは正答性が2点高いが、100〜1000文書規模ではRAGが優位になるという結果を示す。メモリブロックによるコンテキスト設計やMCPハッカソン事例も含む。

## 設計のポイント

- 小規模で焦点の絞られた文書群ではファイル探索エージェント、大規模でリアルタイム性が必要なら従来のRAGと、規模と要件で検索方式を選ぶ。
- エージェントのコアツールは5〜10個程度に絞り、ファイルシステムアクセスで能力を補う。
- 会話履歴全体ではなく構造化されたメモリブロックに要点を蒸留してコンテキスト比率を管理する。
- PDF/Word/Excelなど非プレーンテキストは事前にパースしてエージェントが扱える形に変換する。

## 使いどころ

- 検索方式（RAGかファイル探索か）を選定するアーキテクト。
- 長期タスクのエージェントでコンテキスト肥大に悩む開発者。
- 経費精算など非構造資料からフォームを自動入力するエージェントを作る場面。
