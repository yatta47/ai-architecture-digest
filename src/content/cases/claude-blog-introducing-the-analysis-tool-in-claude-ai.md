---
type: announcement
title: Claude.aiのコード実行によるデータ分析ツール
title_original: Introducing the analysis tool in Claude.ai
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- code-execution
- ai-agent
components:
- Claude 3.5 Sonnet
- analysis tool (JavaScriptサンドボックス)
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/analysis-tool
published_at: '2024-10-24'
---

## 概要

Claude.aiに組み込みのコード実行サンドボックスとしてanalysis toolを追加し、ClaudeがJavaScriptを書いて実行しながら段階的にデータのクレンジング・探索・分析を行えるようにした。抽象的な推論だけでなく、実行結果に基づく数学的に正確で再現可能な回答を返せる。

## 設計のポイント

- Claude.ai内蔵のサンドボックスでコードを書いて即実行し、結果を見ながら反復改善できるループを持つ
- CSVなどのアップロードデータに対して段階的に処理させることで検証可能な結果を担保する

## 使いどころ

- マーケティングや営業部門がアップロードした実データから傾向・パフォーマンス分析を行う場面
- エンジニアがログデータからリソース使用状況を分析する場面
