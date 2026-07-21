---
type: announcement
title: LangSmith連携のプロンプト自動最適化ライブラリ「Promptim」
title_original: 'Promptim: an experimental library for prompt optimization'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- prompt-optimization
- eval
- human-in-the-loop
components:
- LangSmith
- Promptim
- DSPy
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/promptim
published_at: '2026-06-15'
---

## 概要

LangChainは、初期プロンプト・データセット・評価関数を与えると最適化ループを回して改善プロンプトを生成するOSSライブラリ「Promptim」を公開した。LangSmithのデータセット管理・プロンプトHub・アノテーションキューと統合し、自動評価に加え人間フィードバックも最適化ループに組み込める。

## 設計のポイント

- train/dev/testに分割したデータセット上でベースラインを測定し、メタプロンプトが改善案を提案する反復ループを回す
- 改善後のプロンプトはdevセットで再評価し、スコアが向上した場合のみ採用する
- 自動評価だけでなくLangSmithのアノテーションキュー経由で人間フィードバックも最適化に組み込めるようにする
- DSPyのようなシステム全体の最適化ではなく、単一プロンプトの書き換えに絞ってスコープを限定する

## 使いどころ

- 手動のプロンプトチューニングに時間を取られているAIエンジニア
- モデルを切り替えるたびにプロンプトを再調整する必要があるチーム
