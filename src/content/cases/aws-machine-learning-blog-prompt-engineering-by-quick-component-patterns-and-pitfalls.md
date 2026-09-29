---
type: guidance
title: Quickの機能別プロンプトパターンと落とし穴
title_original: 'Prompt engineering by Quick component: Patterns and pitfalls'
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- context-engineering
- ai-agent
components:
- Amazon Quick Research
- Amazon Quick Flows
- Amazon Quick Sight
- Quick Index
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/prompt-engineering-by-quick-component-patterns-and-pitfalls/
published_at: '2026-09-29'
---

## 概要

Amazon Quickの Research・Flows・Sight などコンポーネントごとに、プロンプトの書き方と避けるべき失敗を解説する第2回。各機能が入力をどう解釈するかに合わせて、目的・トリガー・指標などを具体的に指定するのが要点。

## 設計のポイント

- Researchでは目的・読み手・焦点を明記し、サブ質問やデータソースを絞って調査計画を確認する。
- Flowsではスケジュール・データソース・出力・宛先を明示し、複雑な処理は番号付きステップで記述する。
- 初回構築後は全面書き直しでなく、対話による追加指示で反復改善する。
- Sightでは業務課題・指標・軸・期間・可視化形式を揃えて問い合わせる。

## 使いどころ

- 市場調査や競合分析をResearchに任せたいアナリスト。
- 週次レポートや承認フローをノーコードで自動化したい業務部門。
- BIの対話的探索を導入し、出力のばらつきを抑えたいデータチーム。
