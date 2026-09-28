---
type: opinion
title: 確率を返すジャッジモデルは1回の呼び出しでLLM評価のブレを検知できるか（Jev検証）
title_original: What Jev's probabilities reveal that repeated LLM judgments miss
company: Arize
industry: cross-industry
cloud: []
patterns:
- eval
- llmops
components:
- Arize Phoenix
- Jev
- GPT-5 nano
- Gemini 3.8 Flash
- Claude Haiku 4.5
- GPT-5.6 Sol
- Claude Opus 5
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/jev-llm-judge-consistency/
published_at: '2026-09-28'
---

## 概要

LLMジャッジは同じ入力でも実行のたびに回答がぶれることがあり、著者はこれまで高温度で10回以上実行してブレを検知することを推奨してきたが、本番運用には高コストだと指摘する。ラベルごとに確率を返す評価モデル『Jev』が、1回の呼び出しでこのブレのシグナルを代替できるかをArize Phoenixの10種類の評価器・517件のラベル付きベンチマークで検証し、Jevの低確信度な回答は誤りである確率が有意に高く、5つのLLMジャッジより回答のブレが少ないことを示した。

## 設計のポイント

- LLMジャッジを『固定ラベル集合に強制する分類器』とみなし、通常の分類器と同じ精度指標（Accuracy・F1）で評価する枠組みを採用する。
- 既存のLLM向けプロンプトをそのまま流し込む『ドロップイン』と、state/instructions/criteriaに構造化して渡す『ネイティブ』の2方式でJevを比較し、長文入力ではネイティブ方式が精度を押し上げることを確認する。
- 10回の実行のうち1回でも他と異なる回答が出た場合を『回答のブレ』と定義し、ジャッジ選定の指標としてコスト・レイテンシに並べて扱う。

## 使いどころ

- 評価パイプラインのコストとレイテンシを抑えつつ、LLMジャッジの回答が不安定な難しい事例を検出したいLLMOpsチーム。
- 新しい評価基準（eval）を開発する際に、確信度の低い判定を人手レビューへ振り分ける仕組みを作りたい場合。
