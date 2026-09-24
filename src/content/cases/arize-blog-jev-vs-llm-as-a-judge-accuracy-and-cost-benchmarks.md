---
type: guidance
title: LLM-as-a-JudgeとJevの精度・コスト比較と判定閾値チューニング
title_original: 'Jev vs. LLM-as-a-Judge: Accuracy and cost benchmarks'
company: Arize
industry: cross-industry
cloud: []
patterns:
- eval
- llmops
- cost-optimization
components:
- Jev
- Claude Opus 5
- GPT-5.6 Terra
- RAGTruth
- SummEval
- Arize AX
- Arize Phoenix
outcome:
  type: cost
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/jev-as-a-judge/
published_at: '2026-09-23'
---

## 概要

Arizeが、確率を返す型付きモデルJevをClaude Opus 5、GPT-5.6 Terraと比較し、幻覚検出とサマリー品質評価で計23,325件を検証した。閾値調整後のJevは幻覚検出でOpus 5と同じ87%の精度を約300分の1のコスト、23倍の速度で達成した。既定の0.5閾値では劣って見え、閾値の調整が重要という結論。

## 設計のポイント

- 確率出力を判定に変える閾値を人手ラベル付きの検証セットで調整し、別のテストデータで確認する。
- ROC AUCで判定モデルの順位付け能力と閾値の位置を切り分けて評価する。
- 許容できる誤検知と見逃しに応じて閾値を選ぶ（0.5から0.8〜0.9で精度が向上）。
- 低コスト・低レイテンシの判定器なら、サンプル評価でなくリクエスト経路の全応答に適用できる。

## 使いどころ

- RAGの幻覚検出を全応答に対し低遅延で回したいLLMOpsチーム。
- LLM judgeの費用が大きく、代替の評価器を検討している組織。
- 評価器の既定閾値のまま採否を決めてしまうのを避けたい評価設計者。
