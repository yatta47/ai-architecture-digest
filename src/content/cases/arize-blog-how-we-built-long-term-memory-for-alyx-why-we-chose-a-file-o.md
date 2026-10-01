---
type: case
title: 'Alyxの長期メモリ設計: 知識グラフでなく8,000文字の単一ファイル'
title_original: 'How we built long-term memory for Alyx: why we chose a file over a knowledge graph'
company: Arize
industry: cross-industry
cloud: []
patterns:
- context-engineering
- memory-consolidation
- eval
- ai-agent
components:
- Alyx
- Arize AX
- Arize Phoenix
- Graphiti
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/alyx-agent-long-term-memory-architecture/
published_at: '2026-10-01'
---

## 概要

ArizeはAIエンジニアリングエージェントAlyxの長期メモリを、ベクトル検索・エピソード/意味ストア・時系列知識グラフの構成から、ユーザーとスペースごとに8,000文字上限の構造化ファイル1つへ簡素化した。毎リクエストでファイル全体を読み込み、バックグラウンドジョブで要約と差分更新・圧縮を行う。最終evalではメモリ依存の18問中16問に正答し、メモリが悪影響を与えないかの問いは全問通過した。

## 設計のポイント

- 検索や知識グラフを使わず、常時ロードする小さな構造化ファイルをメモリとして読み取り経路から検索を排除する。
- 完了したターンをバックグラウンドで要約して的を絞った編集を提案し、サイズ上限内に圧縮する。
- 更新が却下された場合に最新情報が保存されない弱点があることを前提に設計する。
- メモリが必要な問いと、メモリが悪化させうる問いの両方向からevalする。

## 使いどころ

- 範囲が限定されたエージェントで、セッションを跨いだ好みや規約を保持したい場面。
- 検索・グラフ型メモリの書き込みコストとチューニング負荷を避けたい場面。
- メモリ導入が品質を下げないか検証したい場面。
