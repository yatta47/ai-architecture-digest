---
type: guidance
title: マルチターン対話エージェントのターン単位評価指標AEM
title_original: Agent Evaluation Metric for multi-turn conversations
industry: cross-industry
cloud:
- aws
patterns:
- eval
- ai-agent
- root-cause-analysis
components: []
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/agent-evaluation-metric-for-multi-turn-conversations/
published_at: '2026-09-10'
---

## 概要

マルチターンのエージェント対話では初期の1つの誤りが後続ターンへ連鎖し、タスク全体の成否だけを見る評価では根本原因を特定できない。この記事はAgent Evaluation Metric（AEM）というターン単位で正確性を分解評価する指標を提案し、誤りの発生ターンと単なる連鎖影響を切り分ける手法を示す。

## 設計のポイント

- 品質を『真実性』『完全性』のような名前付きサブメトリクスに分解し、ターンごとに独立計測してから合成する
- タスク全体のゴール達成率だけでなく、各ターンでのツール呼び出しパラメータや回答内容の正確性を個別に追跡する
- 同じ分解の仕組みを安全性・指示保持など新しい評価軸にもそのまま拡張できる設計にする

## 使いどころ

- エンタープライズアシスタントなど、複数ターンにまたがるタスクを実行するエージェントの品質改善
- 『どのターンが原因で失敗したか』を切り分けたいエージェント開発・デバッグの現場
