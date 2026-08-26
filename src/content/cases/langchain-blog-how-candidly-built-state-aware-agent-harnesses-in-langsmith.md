---
type: case
title: 金融相談AIエージェントの会話状態をリアルタイム推定し応答を制御するハーネス
title_original: How Candidly Built State-Aware Agent Harnesses with LangSmith
company: Candidly
industry: financial-services
cloud: []
patterns:
- ai-agent
- llmops
- eval
- context-engineering
components:
- LangSmith
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-candidly-built-state-aware-agent-harnesses-with-langsmith
published_at: '2026-08-26'
---

## 概要

Candidlyは、借金返済や貯蓄など高難度の金融相談に応じるAIエージェント「Cait」について、会話終了後の解決/離脱を判定するハイブリッドラベリングパイプラインをLangSmith上に構築し、92.3%の人手一致率を達成した。さらにQ/Aの語彙一致度やユーザー発言の文字数・大文字比率などトレースから軽量に計算できる特徴量を用い、IO-HMMで会話をユーザー側の状態とエージェント側の応答特徴に分離してモデル化することで、会話終了前にリアルタイムで状態を推定し応答を調整できるようにした。

## 設計のポイント

- 明確なケースはルールベースで判定し、曖昧なケースのみLLM-as-judgeに振り分けるハイブリッドラベリングで、人手ラベルとの一致率92.3%を達成した
- Q/Aの語彙重なりや応答の意味的連続性、ユーザー発言の長さ・大文字比率など、ミリ秒オーダーで計算できる軽量な決定的特徴量のみをリアルタイム推定に使用した
- IO-HMMを用いてユーザー側の挙動を『観測(状態推定の材料)』、エージェント側の応答特徴を『制御可能な遷移入力』として明確に分離し、状態とその遷移関数をEMで同時に学習した
- RNNやトレース変換器のような高性能だが解釈困難なモデルではなく、held-outフィットとBICで4状態のIO-HMMを選び、解釈可能性とリアルタイム介入のしやすさを優先した

## 使いどころ

- 会話終了後の事後評価だけでなく、会話の途中で介入して結果を改善したい高難度・高ステークスな相談系AIエージェントの構築チーム
- LangSmithなどのトレース/観測データを、単なる可視化にとどめず会話中の応答制御ポリシーへと転用したいチーム
- ブラックボックスな深層モデルより、状態や遷移の解釈可能性を重視して意思決定ロジックを説明したい規制産業のAIプロダクト
