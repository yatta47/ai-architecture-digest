---
type: announcement
title: セッション単位の評価とAgent-as-a-Judgeを追加したArize AXアップデート
title_original: 'New in Arize AX: first-class sessions, Agent-as-a-Judge, and vision evals'
industry: cross-industry
cloud:
- multi-cloud
patterns:
- eval
- llmops
components:
- Arize AX
- Alyx
- Claude Fable 5.1
- Amazon Bedrock
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/new-in-arize-ax-september-2026-updates/
published_at: '2026-09-22'
---

## 概要

Arize AXの2026年8〜9月分アップデートでは、セッション（会話全体）が個々のスパンではなく評価・注釈・キューイングの第一級単位になった。トレースを検査し発生している失敗に基準を適応させるAgent-as-a-Judgeが全プランで利用可能になり、画像を直接スコアリングするvision evalsも追加された。

## 設計のポイント

- スパン単位ではなくセッション単位で注釈・レビューキュー・評価プレビューを扱えるようにした
- Agent-as-a-Judgeはトレースを検査して関連スパンを見つけ本番で実際に起きている失敗に評価基準を適応させる
- 画像列を参照するLLM-as-a-judgeテンプレートにより画像そのものをスコアリングできるようにした
- トレースからのデータセット生成でサンプリングによる欠落行をなくし全件を書き込むようにした

## 使いどころ

- 個々の発話単位ではなく会話全体の品質を評価・レビューしたいエージェント運用チーム
- 本番トラフィックで実際に起きている失敗パターンに追随した評価基準を継続運用したい場合
- 画像や音声を扱うマルチモーダルエージェントの出力を定量評価したいチーム
