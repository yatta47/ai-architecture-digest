---
type: opinion
title: ハーネス蒸留でエージェントのハーネスは何が変わるか
title_original: Are agent harnesses dying? What harness distillation changes
industry: cross-industry
cloud: []
patterns:
- ai-agent
- fine-tuning
- context-engineering
- eval
components:
- Harness-Zero
- Qwen3.5-9B
- Arize AX
- Arize Phoenix
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/agent-harness-distillation/
published_at: '2026-09-29'
---

## 概要

研究Harness-Zeroが、進化させたハーネスの挙動を小型モデルに蒸留し、ハーネス無しで元のモデルとハーネスの組み合わせを上回った例を紹介する。汎用的な足場はモデルに吸収されるが、自社のツール・データ・利用者・環境に固有の部分は残るため、ハーネスを定期的に作り直す運用が必要だと論じる。

## 設計のポイント

- 失敗分析から自動でハーネスを進化させ、それを使って強いモデルが修正した学習データを作る。
- 蒸留したモデルは最小のループで動かせるが、化学のように知識や検証ツールが要る領域ではハーネスが優位に残る。
- ハーネスは使い捨てを前提に、トレースと評価で再構築を自動化する。

## 使いどころ

- 小型モデルで社内エージェントを運用したい開発チーム。
- モデル更新のたびにハーネスの見直しに追われている担当者。
- 汎用の足場と固有の部分を切り分けて設計したい人。
