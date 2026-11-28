---
type: guidance
title: DiffusionDBの例示をRAGで引き画像生成プロンプトを書き換えるエージェントツール
title_original: LlamaIndex and Transformers Agents
industry: cross-industry
cloud: []
patterns:
- rag
- ai-agent
- prompt-optimization
components:
- LlamaIndex
- Transformers Agents
- Hugging Face Spaces
- DiffusionDB
- OpenAI
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-and-transformers-agents-67042ee1d8d6
published_at: '2023-06-08'
---

## 概要

1万件の画像生成プロンプトを索引化し、類似例を参照してユーザーの指示を書き換えるツールをTransformers Agents向けに作った事例解説。書き換え後のプロンプトを画像生成ツールに渡すことで出力の見栄えを高める。

## 設計のポイント

- 良い出力例のコーパスを検索して少数例として与え、入力プロンプトを自動改善する。
- エージェントが1回に1ツールしか選ばない制約があるため、書き換えと画像生成を1つのツールに合成する。
- 索引は事前に構築して永続化し、ツールの初期化時にダウンロードする。

## 使いどころ

- 画像生成の入力品質を利用者の腕に依存させたくないサービス開発者。
- エージェントの既存ツールに前処理を足したい場面。
