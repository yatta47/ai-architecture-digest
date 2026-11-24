---
type: announcement
title: 'LlamaIndex: 請求書照合エージェントと多言語マルチモーダルRAG'
title_original: LlamaIndex Newsletter 2025-05-06
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- ai-agent
- document-processing
- rag
- event-driven
components:
- LlamaIndex.TS
- LlamaParse
- LlamaDeploy
- Solace
- Qwen 3
- Ollama
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-05-06
published_at: '2025-05-06'
---

## 概要

請求書と契約の整合性を自動確認するエージェント、Deep Researcherテンプレート、LlamaDeployのSolace対応、CondoScanの事例を紹介。エージェントとWorkflowsの決定論的処理を混ぜる設計方針にも触れる。

## 設計のポイント

- 自律的なエージェントと決定論的なWorkflowsを組み合わせる
- サブ質問を生成して回答し最終レポートに統合する
- 非同期メッセージブローカーでマルチサービス構成のエージェントをデプロイする

## 使いどころ

- 契約書と請求書の突合を自動化したい場面
- 不動産などで大量文書のレビュー時間を短縮したい場面
