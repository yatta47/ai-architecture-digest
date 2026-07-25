---
type: case
title: 給与明細と証券口座明細を突合するローン審査パイプライン
title_original: Building a Financial Document Pipeline with LlamaParse
company: LlamaIndex
industry: financial-services
cloud: []
patterns:
- document-processing
- ai-agent
components:
- LlamaParse
- LlamaCloud SDK
- FastAPI
- Pydantic
- SQLite
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/building-a-financial-document-pipeline-with-llamaparse
published_at: '2026-07-18'
---

## 概要

LlamaIndexがNYCで開催したワークショップでは、給与明細や証券口座明細などレイアウトが揺れる金融書類からPDF→Markdown変換、Pydanticスキーマでの構造化抽出、複数書類を横断した審査サマリ生成までを一気通貫で構築した。人手による相互チェックの一部をLLM推論に置き換え、不一致フラグ付きの審査サマリを自動生成する。

## 設計のポイント

- Parse→Extract→クロスドキュメント分析という3段階でLlamaParseを異なる目的に使い分ける
- 複数書類の抽出結果をテキストにまとめて再アップロードし、システムプロンプトで業務知識（審査基準）を注入したクロスドキュメント推論を行う
- 非同期Python＋SQLiteのシンプルな構成にしつつ、ジョブキューやDBを差し替え可能なアーキテクチャにしておく

## 使いどころ

- 収入証明・資産証明など複数書類の整合性チェックが必要なローン審査業務
- 人間によるレビューを最終ステップに残したhuman-in-the-loop型の書類自動化
