---
type: guidance
title: プロンプトキャッシュ入門
title_original: Prompt Caching 101
industry: cross-industry
cloud: []
patterns:
- prompt-optimization
- cost-optimization
components:
- OpenAI API prompt caching
outcome:
  type: cost
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/cookbook/examples/prompt_caching101/
published_at: '2024-10-01'
---

## 概要

1024トークンを超えるプロンプトに自動適用されるOpenAIのプロンプトキャッシュ機能を解説。プロンプト冒頭の共通部分(ツール定義やシステムプロンプトなど)がキャッシュされると、長いプロンプトでレイテンシを最大80%削減しコストも下げられる。

## 設計のポイント

- 静的な内容(指示・ツール定義・画像など)をプロンプトの先頭に、可変の内容を末尾に配置してキャッシュヒット率を最大化する
- 組織単位でキャッシュがスコープされるため同一組織内のリクエスト間でキャッシュを共有できる設計を理解して活用する

## 使いどころ

- 同じツール定義やスキーマを繰り返し使うエージェントアプリケーション
- 大規模なコードベースやワークスペースの要約をプロンプトに繰り返し挿入するコーディング支援ツール
- マルチターン会話の静的な文脈を保持し続けるチャットボット
