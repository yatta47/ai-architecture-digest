---
type: case
title: カスタムMLモデルとLLMを組み合わせた顧客バグ分類・トリアージ自動化システム「BugWiser」
title_original: How AI Reduced Customer Bug Triage From Nearly a Year to Less Than a Week
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- root-cause-analysis
- multi-model-routing
- human-in-the-loop
- llmops
components:
- Anthropic Opus
outcome:
  type: speed
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/how-ai-reduced-customer-bug-triage-from-nearly-a-year-to-less-than-a-week/
published_at: '2026-07-21'
---

## 概要

SalesforceのSales Cloudチームは、顧客報告バグの分類とトリアージを自動化する社内AIシステム「BugWiser」を構築した。過去の技術者の判断データで学習させたカスタム機械学習モデルで決定論的なバグ分類と信頼度スコアを生成し、AnthropicのOpusなどのLLMで調査背景を要約・文脈化することで、300人日規模だった手動トリアージ作業を1週間未満に短縮した。技術者がモデルの予測に不同意の場合は正しい分類を入力し、それが継続的にモデルの再学習に使われることで、専門知識をシステムに蓄積し続ける仕組みとなっている。

## 設計のポイント

- 決定論的で説明可能な分類にはカスタム機械学習モデル、非構造情報の要約・文脈生成には汎用LLMというように、タスクごとに最適なAIモデルを使い分ける
- 各予測に信頼度スコアと根拠の説明を付与し、技術者が結果を検証してから行動できるようにすることで信頼性を担保する
- 技術者がモデルの予測に反対する場合は正しい分類を入力させ、それを継続的な再学習に反映することでモデルを組織の専門知識と同期させ続ける
- 汎用的なAI推論に頼るのではなく、過去数年分の技術者の実際の判断データでモデルを学習させ、既存の組織的知見をシステムに継承させる

## 使いどころ

- 大量の顧客報告バグを抱え、技術者ごとに分類基準がばらつきがちなエンジニアリング組織の標準化とトリアージ高速化
- リリースごとにどの製品領域で問題が集中しているかなど、経営層向けの品質インサイトを迅速に得たい場合
- 既存の暗黙知・過去の意思決定データが豊富に蓄積されており、それをAIに継承させて一貫適用したい業務プロセス
- AIの予測に対する現場の信頼を得る必要がある場面で、信頼度スコア・根拠提示・人間によるフィードバックループを組み合わせた設計
