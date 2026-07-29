---
type: case
title: エージェントスキルの効率化をトレーシングと評価で検証・修復した事例
title_original: How to improve agent skills with tracing and evals
company: Arize
industry: cross-industry
cloud: []
patterns:
- eval
- prompt-optimization
- ai-agent
- context-engineering
components:
- Arize AX
- OpenInference
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/how-to-evaluate-and-optimize-agent-skills-with-tracing-and-evals/
published_at: '2026-07-28'
---

## 概要

ADHDセルフスクリーニングエージェントに「スキル」を追加したところレイテンシ56%減・トークン27%減・コスト44%減を達成したが、トレーシングと完全性評価を組み合わせることで回答の網羅性が悪化する回帰が起きていたことを発見した。長時間稼働エージェントに実験結果とスキルファイルを渡して複数回イテレーションさせ、効率改善を維持したまま完全性をベースライン超えまで回復させた。

## 設計のポイント

- スキルのON/OFFをフラグ化し、モデル・プロンプト・タスクを固定した対照実験でトレースにskill.enabled属性を付与し比較可能にする。
- コストやレイテンシの改善だけでなく、固定データセットに対する完全性(completeness)評価器を併用しないと品質劣化を見逃す。
- 手動でのトランスクリプト比較は『見た目が綺麗』に引きずられやすく、定量評価に置き換える。
- 長時間稼働エージェントに評価スコアを見ながらスキルを反復修正させることで、効率と品質のトレードオフを解消する。

## 使いどころ

- プロンプトやSKILL.mdなどのエージェントスキルを導入・改修するチームが、効率化の裏で品質が落ちていないか検証したい場面。
- モデルやプロンプトの変更を継続的にトレースし、コスト・レイテンシ・品質を同時に追跡したいLLMOps担当者。
- 評価スコアを基準に自動でプロンプトやスキルを反復改善したい長時間稼働エージェントの運用者。
