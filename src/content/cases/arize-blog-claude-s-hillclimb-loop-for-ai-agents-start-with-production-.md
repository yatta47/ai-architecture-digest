---
type: guidance
title: 本番トレースから始めるエージェント評価とヒルクライム改善ループ
title_original: 'Claude''s hillclimb loop for AI agents: start with production traces'
company: Arize
industry: cross-industry
cloud: []
patterns:
- eval
- llmops
- ai-agent
- prompt-optimization
components:
- Arize AX
- Claude Code
- Cursor
- Codex
- claude-api skill
- OpenInference
- Arize Phoenix
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/claude-hillclimb-production-traces/
published_at: '2026-10-02'
---

## 概要

Anthropicの/claude-api build-evalとhillclimbの考え方を紹介し、それを本番トレースに対して回す方法をArize AXで示した記事。1回に1変更のみ加え、同一実験を再実行してスコアが上がれば採用するループを、トレース由来のデータセットと人手アノテーションで運用する。arize-instrumentationスキルの改善を実例にしている。

## 設計のポイント

- 評価セットは本番トレースから作り、新たな失敗が出るたびにデータセットへ追加して利用者に追従させる。
- 難しいケースの判定は人が行い、LLMはエラーパターンの絞り込みを補助する。
- グレーダーは決定的に確認できる部分はコード、意味判断が要る部分はLLMジャッジと使い分け、評価対象と別モデルをジャッジに使う。
- 1回に1変更だけ加えてtrain/testを分け、trainだけ上がる場合は過学習として戻す。

## 使いどころ

- 本番エージェントのプロンプト・ツール説明・スキルを継続的に改善したいチーム。
- モデル更新後に陳腐化した評価セットを見直したいとき。
- チームで再現可能な形でエージェント改善の実験を回したいとき。
