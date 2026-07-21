---
type: guidance
title: LLMエージェントの本番監視と評価をどう設計するか
title_original: You don't know what your agent will do until it's in production
industry: cross-industry
cloud: []
patterns:
- llmops
- eval
- human-in-the-loop
- ai-agent
components: []
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/production-monitoring
published_at: '2026-06-30'
---

## 概要

LLMエージェントは入力空間が無限で非決定的に振る舞うため、従来のAPM的な監視だけでは不十分だと指摘する記事。本番トラフィックではプロンプトと応答のペア、マルチターンの文脈、ツール呼び出しを含む実行トラジェクトリ全体を記録する必要があるとする。さらに人手レビューを効率化するため、条件に応じてトレースを振り分け評価基準を定義するアノテーションキューの活用を提案している。

## 設計のポイント

- 完全なプロンプト・レスポンスのペアだけでなく中間のツール呼び出しやマルチターンの文脈も含めてトレースを記録する
- レビュー対象を全件ではなくネガティブフィードバックや高コスト実行など条件でルーティングしてアノテーションキューに流す
- レビュアー向けに評価基準(rubric)を明文化し関連性・正確性・トーン・安全性などの観点を統一する
- レビュー結果を修正データとして評価セットにフィードバックし継続的改善のループを作る

## 使いどころ

- 本番投入後のLLMエージェントの挙動を継続的に観測したいチーム
- 1日あたり数百〜数千件規模のやり取りを人手レビューだけでは追いきれないプロダクトチーム
- 評価データを蓄積してプロンプトやモデル選定を継続的に改善したいLLMOps担当者
