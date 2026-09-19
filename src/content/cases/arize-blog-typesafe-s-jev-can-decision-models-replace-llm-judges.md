---
type: opinion
title: LLM判定の代替となるか：構造化決定に特化したモデル『Jev』を検証
title_original: 'TypeSafe''s Jev: Can decision models replace LLM judges?'
industry: cross-industry
cloud: []
patterns:
- eval
- cost-optimization
components:
- TypeSafe Jev
- GPT-5.6 Terra
- Opus 5
- Gemini Flash-Lite
outcome:
  type: cost
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/typesafe-jev-llm-judge/
published_at: '2026-09-18'
---

## 概要

TypeSafe社は、自由文を生成せず分類・スコアリング・ルーティングのみを行う新種のモデル『Jev』を発表した。LLM-as-a-judgeと比べて最大200倍高速・400倍安価とされ、Arizeはこれが評価（eval）や確信度ベースのルーティングなどアプリケーションアーキテクチャに与える影響を検証している。独立ベンチマークでもコストと精度のトレードオフで有望な結果が出ている一方、キャリブレーションの信頼性など未検証の論点も残る。

## 設計のポイント

- 自由文生成を伴わない『System One』型のモデルにより、トークンストリーム生成をスキップして確率付きの型付き回答を返す
- Reinforcement Learning for Calibrated Decisions（RLCD）で、申告確率と実際の正解率が対応するようキャリブレーションして学習する
- ラベル付き学習データが不要な点はLLM-as-a-judgeの利点を保ちながら、コストとレイテンシだけを大幅に下げる位置づけで使う

## 使いどころ

- エージェントトレースのトリアージなど大量の合否判定・ルーティングを低コストで行いたい場合
- LLM-as-a-judgeのコストとレイテンシがボトルネックになっている評価パイプライン
- ラベル付き学習データを用意できないが、ロジスティック回帰やファインチューニング済みエンコーダ並みの速度が欲しい場合
