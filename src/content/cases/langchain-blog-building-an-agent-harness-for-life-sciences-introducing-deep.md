---
type: case
title: 臨床・創薬研究者向けオープンソースAIエージェント「Deep Life Sci」
title_original: 'Building an Agent Harness for Life Sciences: Introducing Deep Life Sci'
company: LangChain
industry: healthcare
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- document-processing
- eval
components:
- Deep Agents
- LangSmith
- ClinicalTrials.gov
- PubMed
- PubMed Central
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/agent-harness-life-sciences
published_at: '2026-09-17'
---

## 概要

LangChainは製薬・臨床研究者向けのオープンソースAIエージェント「Deep Life Sci」を、自社のDeep Agentsハーネスをベースに開発した。ClinicalTrials.govの60万件超の臨床試験記録やPubMed・PubMed Centralの数千万件の論文をサブエージェントに分担して調査させ、サンドボックス内でデータ解析も実行できる。LangSmithによるトレーシングと評価を組み込むことで、企業が独自データを統合しながら挙動を監査・改善できる仕組みを提供する。

## 設計のポイント

- 汎用AIアシスタントでは不足するドメイン知識を、公開データソースへの直接統合とサブエージェント分業で補う
- オープンソース化してハーネスをカスタマイズ可能にし、モデルやガードレールを企業側で選べるようにする
- 全実行をLangSmithでエンドツーエンドにトレースし、GxP監査で求められる説明可能性を担保する
- デフォルトの評価セットを用意し、モデル変更やプロンプト修正の前後で性能劣化を検知できるようにする

## 使いどころ

- RNA-seqやプロテオミクスのスクリーニング結果から有意遺伝子を抽出し、文献根拠付きでランク付けしたい創薬研究者
- 既存治療の臨床試験を網羅的に収集し、エンドポイントや対象集団を統一フォーマットで比較したい臨床開発・HEORチーム
- 同意説明文書やプロトコル改訂など大量の臨床文書のレビュー・編集を効率化したい治験関連部門
- 監査ログと説明可能性が必須なGxP規制下でAIを利用したいライフサイエンス企業
