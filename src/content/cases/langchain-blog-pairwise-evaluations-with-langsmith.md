---
type: announcement
title: LangSmithに搭載されたペアワイズ評価機能
title_original: Pairwise Evaluations with LangSmith
company: LangChain
industry: cross-industry
cloud: []
patterns:
- eval
- llmops
components:
- LangSmith
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/pairwise-evaluations-with-langsmith
published_at: '2026-06-30'
---

## 概要

LangSmithに、2つのLLM出力を同時に比較して優劣を判定する「ペアワイズ評価」機能が追加されたことを発表する記事。単体基準でスコアリングする従来の評価では複数モデルが同点になり差別化できない場合があるが、ペアワイズでLLM-as-judgeまたは人手により直接比較させることで明確な優劣が見えるようになったと説明している。ツイート要約生成タスクを例に、カスタムのペアワイズ評価器をLangSmith SDKで定義し実験結果をUI上で可視化するデモを紹介している。

## 設計のポイント

- 個々の出力を独立採点するのではなく2つの候補を同時に評価器へ渡し直接比較させることで僅差のモデルも差別化する
- RLHFやChatbot Arenaと同様の考え方をLLM-as-judgeによる自動ペアワイズ評価に置き換えて自社の評価パイプラインに組み込む
- カスタム評価基準(プロンプト)をSDK上のevaluate_comparative関数に渡すことで既存の実験結果同士を後から比較できるようにする

## 使いどころ

- 単一基準のスコアリングでは複数モデルの差が付きにくいテキスト生成・チャットタスクを評価したいチーム
- RLHF的な人間の選好判断をLLM-as-judgeで自動化してモデル選定に活用したい開発者
- 既に実行済みの複数実験の出力を後から比較検証したいLLMアプリ開発者
