---
type: guidance
title: LLM-as-Judgeと人間評価者の一致度を測定する評価設計ガイド
title_original: How to measure human-LLM judge alignment
industry: cross-industry
cloud: []
patterns:
- eval
- human-in-the-loop
- llmops
components: []
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/measuring-human-llm-judge-alignment/
published_at: '2026-07-22'
---

## 概要

LLM評価者(LLM judge)を信頼して使う前に、タスク定義・人間同士の一致度・LLMと人間の一致度・誤りの種類という4段階で測定すべきだと説く記事。人間同士の一致度をCohen's kappaやKrippendorff's alphaなどのchance-adjusted指標で測り、同じ指標でLLM-人間一致度と比較したうえで、LLM判定を分類器として精度・再現率・F1・混同行列で評価する手法を解説している。

## 設計のポイント

- 指標を選ぶ前にunit(span/trace/session)・ラベル構造・positive class・reference policy・コスト非対称性をYAML的に明文化する。
- LLM評価前に複数人のアノテーションを集め、人間同士の一致度をCohen's kappa/Fleiss' kappa/Krippendorff's alphaで測定し基準を作る。
- 生の一致率だけでなくchance-adjusted指標を併記し、クラス不均衡による見かけ上の低いkappa(prevalence paradox)を誤解しないようにする。
- 参照ラベル確定後はLLM judgeを分類器として扱い、精度・再現率・F1・混同行列でどんな誤りをするか分析する。

## 使いどころ

- LLM-as-Judgeを本番の自動評価パイプラインへ導入する前に信頼性を検証したいチーム。
- 人手アノテーションの一致率が低く、評価ルーブリック自体を改善する必要がある場合。
- fail/pass判定など特定クラスの検出精度が重要で、クラス不均衡が疑われる評価タスク。
