---
type: announcement
title: n8nノーコード基盤に統合されたLlamaParse Platformノード
title_original: Bring your Document Workflows to n8n with the LlamaParse Node
industry: cross-industry
cloud: []
patterns:
- ai-agent
- document-processing
components:
- LlamaParse Platform
- n8n
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/bring-your-document-workflows-to-n8n-with-the-llamaparse-node
published_at: '2026-07-18'
---

## 概要

LlamaIndexはn8nと提携し、Parse・Classify・Split・Extract・Retrieveの5つのLlamaCloud機能を単一ノードで扱えるv5/v6の公式検証済みコミュニティノードを公開した。ノードはAIエージェントから呼び出し可能なツールとしても登録でき、分類→抽出→検証といった書類処理パイプラインをノーコードで構築できる。

## 設計のポイント

- 5つのリソースを1つのnode（resource/operationドロップダウン）にまとめ、単一の認証情報で扱えるようにする
- 各リソースをusableAsTool: trueとしてマークし、AI Agentノードから直接呼び出せるツールにする
- 分類結果のconfidenceスコアを低信頼度文書の人手レビューへのゲートとして利用できるようにする

## 使いどころ

- ノーコード/ローコードでドキュメント処理パイプラインを構築したいチーム
- 分類→抽出→LLMによる検証という書類処理フローを自動化したい業務部門
