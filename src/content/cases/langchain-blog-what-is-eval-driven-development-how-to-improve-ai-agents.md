---
type: guidance
title: 評価駆動開発（EDD）でAIエージェントを継続的に改善する手法
title_original: What Is Eval-Driven Development? How to Improve AI Agents
company: LangChain
industry: cross-industry
cloud: []
patterns:
- eval
- llmops
- ai-agent
components:
- LangSmith
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/what-is-eval-driven-development
published_at: '2026-11-09'
---

## 概要

LangChainは、TDDに倣い、先に『良い状態』の仕様と評価を書いてからエージェントを変更する評価駆動開発を紹介している。実験を比較して改善を判断し、評価をCIと本番で回して失敗事例をデータセットに戻す。

## 設計のポイント

- 振る舞いごとに、いつ・何をする・何をしないかの短い仕様を書き、狙いを1つに絞ってヒルクライムする
- 変更ごとに実験を比較し、1件の改善が他の事例を壊していないか確認する
- 本番で見つかった失敗を評価データセットの新しい例として追加する
- LLM-as-a-judgeを使い、非決定的な出力もスコア化する

## 使いどころ

- プロンプトを手で試す開発から抜け出したいエージェント開発チーム
- 変更の良し悪しを判断できず困っている場面
- 評価をCIや本番監視に組み込みたいLLMOps担当
