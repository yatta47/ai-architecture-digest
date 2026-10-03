---
type: case
title: 'プロンプトキャッシュのベンチマーク: 再利用率が高くてもコストが下がるとは限らない'
title_original: 'Prompt caching benchmark: high cache reuse doesn''t always mean lower cost'
company: Arize
industry: retail
cloud: []
patterns:
- llmops
- eval
- cost-optimization
components:
- Arize Phoenix
- Harbor
- DeepSeek
- GLM
- GPT
- Claude
outcome:
  type: cost
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/prompt-caching-benchmark/
published_at: '2026-10-02'
---

## 概要

DeepSeek、GLM、GPT、Claudeを、同一の多ターン買い物アシスタントエージェントでHarborとPhoenixのトレースを使って比較した。DeepSeekはキャッシュ読み出し率93.6%で推定コスト最小、Claudeは89.8%を再利用しても出力トークンが支出を左右し最高コストだった。会話が長いほどキャッシュ再利用は増える。

## 設計のポイント

- キャッシュ読み出し率だけでなく、出力トークンを含む総コストで評価する。
- タスク指示や評価基準を固定し、モデルとプロバイダだけを変えて比較する。
- Harborの実行とPhoenixのトレースを連携させ、実験を再現可能にする。

## 使いどころ

- エージェントのモデル選定やコスト試算をするチーム。
- 長い会話履歴を持つ対話型エージェントのコスト最適化を検討する場面。
