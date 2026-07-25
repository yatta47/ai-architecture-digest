---
type: announcement
title: 自然言語指示で文書処理エージェントを自動生成・本番デプロイするビルダー
title_original: 'LlamaAgents Builder: idea to deployed agent in minutes'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- ai-agent
- document-processing
- spec-driven-development
components:
- LlamaParse
- LlamaExtract
- LlamaSplit
- LlamaAgents Builder
- GitHub
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaagents-builder-idea-to-deployed-agent-in-minutes
published_at: '2026-07-19'
---

## 概要

LlamaIndexが自然言語の指示から文書抽出向けのエージェントワークフローを自動生成し、GitHubへのコードプッシュとLlamaParseのマネージド基盤への一括デプロイまでを行う「LlamaAgents Builder」のベータ版を発表した。生成されるのはオープンソースのWorkflowsフレームワークに基づく実コードで、ユーザーが中身を検査・カスタマイズし、自前インフラへ移すこともできる。

## 設計のポイント

- 自然言語の説明からPythonコードとして実際のWorkflowを生成し、ブラックボックス化させず中身を検査・拡張できるようにする
- 低コードツールの手軽さとフルコードの柔軟性を両立するため、生成後のコードをGitHubにプッシュしてユーザーが所有できる設計にする
- 抽出対象の文書種別ごとにLlamaExtractエージェントを自動生成し、分類・ルーティング・抽出のワークフローステップに接続する
- デプロイ時にGitHubへのコード反映からAPIエンドポイント発行、レビュー用WebUIまでを一括自動化する

## 使いどころ

- 請求書・領収書・財務諸表など書式が揺れる文書からの構造化データ抽出を素早く試作したいチーム
- 低コードツールのスキーマ制約に縛られずカスタマイズしたいが、自前でオーケストレーションロジックを書きたくない開発者
- プロトタイプから本番稼働まで最短距離で進めつつ、将来的な自社インフラ移行の余地も残しておきたい組織
