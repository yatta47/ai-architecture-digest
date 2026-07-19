---
type: guidance
title: ファインチューニング無しでエージェント精度を上げるハーネスプロファイル設計
title_original: Create a LangChain Deep Agents Harness Profile for NVIDIA Nemotron 3 Ultra to Improve Performance
company: NVIDIA
industry: cross-industry
cloud:
- multi-cloud
patterns:
- ai-agent
- eval
- prompt-optimization
- context-engineering
components:
- NVIDIA Nemotron 3 Ultra
- LangChain Deep Agents
- LangSmith
- LangSmith Engine
- build.nvidia.com
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/create-a-langchain-deep-agents-harness-profile-for-nvidia-nemotron-3-ultra-to-improve-performance/
published_at: '2026-07-09'
---

## 概要

オープンモデルであるNVIDIA Nemotron 3 Ultraを、ファインチューニングではなくLangChain Deep Agentsのハーネスプロファイル（プロンプト変更・ツール記述変更・ミドルウェア追加）でプロプライエタリなフロンティアモデル並みの精度に近づける手法を解説する。評価ベンチマークで失敗を検出し、原因分析からハーネス修正、再評価までを繰り返すループで、read_fileのページネーション見落としのような具体的な失敗をミドルウェアで是正する例を示す。LangSmith Engineやralphループのような自動提案エージェントを使えば、このハーネス改善プロセス自体を機械化できるとしている。

## 設計のポイント

- モデルの重みを変えるファインチューニングの代わりに、プロンプト・ツール説明・ミドルウェアなどハーネス側の変更で挙動を調整する
- ベースライン評価→失敗分析→ハーネス変更案→再評価という反復ループを回し、修正が退行を生んでいないか都度ベンチマーク全体で確認する
- read_fileの続きページ見落としのような具体的な失敗パターンに対し、ツール結果に注釈を追記するミドルウェア(ReadFileContinuationNoticeMiddleware)で対処する
- LangSmith Engineやralphループのような自動提案エージェントにハーネス修正の提案・検証を担わせ、過学習しない汎化した修正だけを採用する

## 使いどころ

- 高コストなフロンティアモデルの代わりに、オープンモデルを特定のエージェントハーネス向けに調整したいチーム
- モデル自体は変えずプロンプトやミドルウェアの調整だけでエージェントの弱点（ツール利用ミスなど）を是正したい場合
- 評価ベンチマークを備えたエージェントハーネスで、モデル切り替えのたびに継続的な改善サイクルを回したいチーム
