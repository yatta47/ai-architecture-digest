---
type: announcement
title: Claudeのプロンプトキャッシュでコスト最大90%・レイテンシ最大85%を削減
title_original: Prompt caching with Claude
company: Anthropic
industry: cross-industry
cloud:
- aws
- gcp
patterns:
- llmops
- context-engineering
components:
- Claude API
- Claude 3.5 Sonnet
- Claude 3 Opus
- Claude 3 Haiku
- Amazon Bedrock
- Google Cloud Vertex AI
outcome:
  type: cost
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/prompt-caching
published_at: '2025-08-14'
---

## 概要

頻繁に使う長いコンテキストをAPI呼び出し間でキャッシュできるプロンプトキャッシュ機能がAnthropic APIで公開された。同じ背景知識や出力例を繰り返し送る用途で、コストを最大90%、レイテンシを最大85%削減できる。

## 設計のポイント

- 会話エージェント・コーディングアシスタント・大規模文書処理など、同一コンテキストを繰り返し参照する用途を狙って設計する
- コードベースの要約やサンプル出力など『大量の背景情報を一度だけ送り、以後は差分のみ』というアクセスパターンに最適化する

## 使いどころ

- 長い指示や大量のアップロード文書を伴う長時間の対話エージェントを運用するチーム
- コードベースQ&Aやオートコンプリートなど、同じコンテキストを繰り返し参照するコーディング支援ツール
