---
type: case
title: LlamaAgents Builderで自然言語からPEディールソーシングエージェントを構築・デプロイする
title_original: Create a Deal Sourcing Agent With LlamaAgents Builder
industry: financial-services
cloud: []
patterns:
- ai-agent
- document-processing
components:
- LlamaAgents Builder
- LlamaParse
- LlamaExtract
- LlamaClassify
- GitHub
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/creating-a-deal-sourcing-agent-with-llamaagents-builder
published_at: '2026-07-19'
---

## 概要

自然言語プロンプトからLlamaParse/LlamaExtract/LlamaClassifyを組み合わせたエージェントワークフローを生成するLlamaAgents Builderを使い、投資案件のティーザーや財務サマリーを『buyout/growth/minority』の3戦略に分類し、収益やEBITDAなどの主要指標を抽出するPEディールソーシングエージェントを構築・GitHub連携でデプロイする手順を示す。

## 設計のポイント

- プロンプトは専門用語を避けて明確・具体的・簡潔に書くことが高品質な生成コードにつながるとし、良いプロンプト設計の3原則を示した
- サンプルファイルは20〜30ページ程度に抑え、過度に特化・汎化した例を避けることで過学習/過汎化のリスクを避ける
- 生成されたワークフローをノーコードで可視化し、GitHubへコード同期してから再デプロイする反復修正のループを用意した

## 使いどころ

- 投資案件のスクリーニングを人手のトリアージから自動分類・指標抽出に置き換えたいPEファーム
- 非エンジニアでも文書処理エージェントを自然言語だけで組み立てたい業務チーム
