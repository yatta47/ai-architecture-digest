---
type: case
title: LangSmithで長文リサーチレポートを生成するエージェントを評価するSimilarwebの仕組み
title_original: How Similarweb Evaluates Long-Form Agent Research Reports with LangSmith
company: Similarweb
industry: other
cloud: []
patterns:
- eval
- llmops
- ai-agent
components:
- LangSmith
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-similarweb-evaluates-long-form-agent-research-reports-with-langsmith
published_at: '2026-07-29'
---

## 概要

SimilarwebはWebトラフィック分析を自然言語で問い合わせられるエージェント製品Data Studioの品質担保のため、LangSmith上で決定的チェックとLLM-as-judgeを組み合わせた評価基盤を構築した。単純な質問にはgolden answerとの意味的一致で採点し、正解が一つに定まらない長文の調査レポートにはルーブリック評価を用いることで、スコアからトレースまで一貫して追跡できるようにしている。

## 設計のポイント

- ツール呼び出しの妥当性など機械的に判定できる項目は決定的チェック、意味や品質はLLM-as-judgeで採点し両方をLangSmithのフィードバックとして並べる
- 定型的なチャット質問にはgolden answerとの意味的一致度で評価し、長文レポートのような正解が複数あり得る出力にはルーブリックで採点する
- スコアだけでなく評価理由のコメントとトレースへのリンクを常に紐付け、スコアを検証可能な信号として扱う
- ルーブリックの重み付けは事前にキャリブレーションしないと良い更新を誤って回帰と判定してしまうため慎重に調整する

## 使いどころ

- エージェントやRAGパイプラインの出力更新を安心してリリースしたいチーム
- オープンエンドで主観的な長文出力(調査レポート等)の品質を継続的に監視したい場合
- プロンプトやモデルのA/B更新で、どの品質軸が改善・劣化したかをトレースレベルで確認したいチーム
