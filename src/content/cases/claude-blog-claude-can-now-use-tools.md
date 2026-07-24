---
type: announcement
title: Claudeのツール利用機能が一般提供開始
title_original: Claude can now use tools
company: Anthropic
industry: cross-industry
cloud:
- aws
- gcp
patterns:
- ai-agent
- multi-agent-orchestration
components:
- Claude 3 model family
- Anthropic Messages API
- Amazon Bedrock
- Google Cloud Vertex AI
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/tool-use-ga
published_at: '2024-05-30'
---

## 概要

Claude 3モデルファミリー全体でツール利用(Tool Use)がAnthropic Messages API、Amazon Bedrock、Google Cloud Vertex AIで一般提供開始。外部ツールやAPIを呼び出して構造化データの抽出やAPI呼び出しへの変換、DB検索など、より正確でダイナミックな応答を可能にする。

## 設計のポイント

- 開発者が定義したツールセットからClaudeが適切なツールを自律的に選択・実行する仕組みを提供する
- ストリーミング対応や強制ツール選択(forced tool use)など、開発者が制御性と応答性を調整できるオプションを用意する
- 粒度の細かいタスクごとに複数のClaudeサブエージェントを協調させるオーケストレーションを可能にする

## 使いどころ

- 請求書などの非構造化テキストから構造化データを抽出する業務自動化
- カスタマーサポートでDB検索やAPI呼び出しを介して即答するチャットボット
