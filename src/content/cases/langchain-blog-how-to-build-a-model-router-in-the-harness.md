---
type: guidance
title: コーディングエージェントのハーネス内に置くモデルルーター設計
title_original: How to Build a Model Router in the Harness
company: LangChain
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
- cost-optimization
- eval
- context-engineering
components:
- LangChain
- Open SWE
- LangSmith
- LangSmith Insights
- Artificial Analysis Intelligence Index
- GLM-5.3-Flash
- GPT-5.6 Sol
- GPT-6 Astra
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-to-build-a-model-router-in-the-harness
published_at: '2026-10-01'
---

## 概要

LangChainは自社のOSSコーディングエージェントOpen SWEにモデルルーターを実装し、常に最上位モデルを使う基線に比べスレッド当たり中央値コストを64%削減し、品質に目立った変化はなかったと報告する。ルーティングは汎用ゲートウェイでなくハーネス内に置くべきだと主張し、タスク分析、モデル選定、ミドルウェアでの実装という手順を示す。

## 設計のポイント

- LangSmithのトレースからタスク種別とコスト・呼び出し回数を分析し、複雑度の分布を把握してからルーターを設計する。
- Artificial AnalysisのパレートフロンティアからFast/Balanced/Performanceの3段階のモデルを選び、プロバイダを跨いでオープンモデルも含める。
- ルーティングは最初のユーザーメッセージを分類器LLMで判定するミドルウェアとして実装し、ベースプロンプトと段階別基準で最安の適格モデルを選ばせる。
- タスク固有の文脈を持つハーネス側にルーターを置き、観測性とevalを前提に基準を調整する。

## 使いどころ

- コーディングエージェントのLLMコストが急増しているチームが、品質を保ったままコスト削減を図る場面。
- 複数プロバイダのモデルを使い分けるエージェント基盤で、タスク難易度別の振り分けを導入する場面。
- モデルの入れ替えが頻繁で、一行変更で差し替えられる抽象化を求める場面。
