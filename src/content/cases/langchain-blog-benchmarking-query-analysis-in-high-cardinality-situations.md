---
type: guidance
title: 高カーディナリティな列挙値をLLMのクエリ解析でどう扱うか
title_original: Benchmarking Query Analysis in High Cardinality Situations
company: LangChain
industry: cross-industry
cloud: []
patterns:
- context-engineering
- rag
- eval
components:
- GPT-4
- GPT-3.5
- LangSmith
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/high-cardinality
published_at: '2026-06-30'
---

## 概要

検索クエリの構造化解析において、著者名のような候補値が多い(高カーディナリティ)カテゴリカルフィールドをLLMにどう正しく埋めさせるかを検証したベンチマーク記事。全候補値をプロンプトに詰め込む「コンテキストスタッフィング」はコストと精度の両面で非効率であり、埋め込み類似度やNグラム類似度でLLM呼び出し前に候補を絞り込む前置フィルタリングの方が高精度かつ低コスト・低レイテンシだったと報告している。単発LLM呼び出しに制約した上で複数のアプローチを定量比較している。

## 設計のポイント

- 候補値が多い列挙フィールドは全件をプロンプトに詰め込まず埋め込み類似度やNグラム類似度で事前に候補を絞り込んでからLLMに渡す
- コンテキストスタッフィングはコンテキスト長・速度・コストの面で高カーディナリティには不向きであることを定量的に確認する
- LLM呼び出し後に候補リストと突き合わせて修正するpost-LLM selectionのような後段補正も選択肢に入れる
- レイテンシとコストを制約するため単一LLM呼び出しに絞って各アプローチを比較評価する

## 使いどころ

- 検索・フィルタ機能でユーザー入力から曖昧な固有名詞(著者名・商品名など)を正規化したいチーム
- 候補値が数万〜数百万件規模になるエンタープライズ検索でクエリ解析を設計するエンジニア
- LLM呼び出しのコストとレイテンシを抑えつつ構造化抽出の精度を上げたいプロダクト担当者
