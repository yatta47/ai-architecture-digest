---
type: case
title: Uberが本番規模でAIエージェントを評価する仕組み
title_original: How Uber evaluates AI agents at production scale
company: Uber
industry: logistics
cloud: []
patterns:
- eval
- ai-agent
- llmops
components:
- Arize
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/how-uber-evaluates-ai-agents-at-production-scale/
published_at: '2026-08-14'
---

## 概要

Uberの音声配車エージェントが、子どもの「ピザが食べたい」という発言を誤って配車先変更の指示と解釈してしまった事例を起点に、Uberのエージェントプラットフォームチームが1年以上かけて構築した評価の仕組みを紹介する。トレーシングをデプロイ時のデフォルトにして本番挙動を可視化し、既存の設定情報とトレースから自動でエージェント固有の評価器を生成してSlackにアラートする仕組みで、評価を後付けの作業ではなく開発の既定経路に組み込んだ。

## 設計のポイント

- 個別入出力ログではなく、ツール呼び出しや計画更新を含む完全なトラジェクトリのトレーシングを、デプロイ時に自動で有効化する
- エージェント構成・本番トレース・意図する挙動の文脈情報から評価器を自動生成し、チームがゼロから評価スイートを設計するコールドスタート問題を回避する
- 評価結果をLLM-as-a-judgeの技術詳細を意識させずに、具体的な製品課題として伝わる形(例: ツール出力と矛盾する回答が30%)でSlackにアラートする
- オフライン評価をすり抜けた失敗はセッション長など間接指標の異常から検知し、トレースを辿って原因を特定する運用にする

## 使いどころ

- 技術成熟度の異なる複数チームが同じプラットフォーム上でエージェントを開発する大規模組織
- 評価が後回しにされがちな「まず動くものを作る」フェーズのプロダクトチーム
- エージェントの失敗が実際の収入や配送に直結する高スループット・実運用サービス
