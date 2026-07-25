---
type: announcement
title: LlamaParseとAgent Workflowsを統合したドキュメントエージェント基盤LlamaAgents
title_original: 'LlamaAgents: Build, Serve, and Deploy Document Agents'
company: LlamaIndex
industry: financial-services
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- document-processing
- human-in-the-loop
components:
- LlamaAgents
- LlamaParse
- LlamaIndex Agent Workflows
- llamactl
- LlamaClassify
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaagents-build-serve-and-deploy-document-agents
published_at: '2026-07-19'
---

## 概要

LlamaParseの文書処理とAgent Workflowsのオーケストレーションを統合したLlamaAgentsのオープンプレビューを発表し、CLIツールllamactlによるテンプレート初期化・ローカルサーブ・クラウドデプロイの流れを解説している。SEC提出書類を種別分類してから該当スキーマで抽出し、UIでレビュー・承認するSEC Insights Agentを具体例として紹介している。

## 設計のポイント

- LlamaParseの文書処理とAgent Workflowsのイベント駆動オーケストレーションを組み合わせ、自由形式のLLM判断から厳密に制御されたフローまで柔軟に設計できる
- SEC Insights Agentの例では、LlamaClassifyでフォーム種別(10-K/10-Q/8-K等)を分類してから該当スキーマの抽出エージェントへ振り分ける
- 抽出結果をUIでレビュー・承認するhuman-in-the-loopをテンプレートに組み込み、本番投入前の確認を担保する
- llamactlによりローカルサーバー起動からクラウドへのワンコマンドデプロイまでを一貫して扱える

## 使いどころ

- SEC提出書類など複数種別の文書を分類してから専用スキーマで抽出したい金融・コンプライアンス部門
- プロトタイプから本番運用まで素早く持っていきたいドキュメントエージェント開発者
