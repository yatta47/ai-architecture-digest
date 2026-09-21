---
type: announcement
title: LangSmith EvalsにSystem OneモデルJevをLLM-as-judgeの代替として追加
title_original: Jev is now available in LangSmith Evals
company: LangChain
industry: cross-industry
cloud: []
patterns:
- eval
- llmops
components:
- LangSmith
- Jev
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/jev-is-now-available-in-langsmith-evals
published_at: '2026-09-21'
---

## 概要

LangSmithはエージェント評価のjudgeとして、テキスト生成をしない「System One」モデルJevを追加した。noul(はい/いいえ確率)・choice(選択)・score(順序尺度)の3種の型付き質問に高速・低コストで答えられ、複数の評価観点を並列に投げても応答時間がほぼ増えないため、コード評価とLLM-as-judgeに次ぐ第3の評価手法として使える。

## 設計のポイント

- 自由記述を生成してから構造化出力へ変換するLLM-as-judgeと異なり、型付きの回答(yes/no確率・選択・スコア)を直接返すモデルを使い、構造化変換に起因する誤りを排除する
- 1リクエスト内で複数の評価質問(PII漏洩・ユーザー意図・不満度など)を並列評価できる設計にし、質問を追加してもレイテンシがほぼ増えないようにする
- オンライン評価では低コスト・低レイテンシのSystem Oneモデルでほぼ全トラフィックを継続的にスコアリングし、開放的な観点が必要な場合のみLLM-as-judgeを併用する

## 使いどころ

- PII漏洩やプロンプトインジェクションなど、検知から対応までの時間を縮めたいセキュリティ/安全性系のオンライン監視
- コストの都合でサンプリング評価しかできていなかったエージェントを、全トラフィックに対して継続的に評価したい場合
- モデルやプロンプトを変更するたびに大量のリグレッションテストを回す必要があり、LLM judgeのコストがボトルネックになっているチーム
