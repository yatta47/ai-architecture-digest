---
type: case
title: Salesforce、12,000ダッシュボードのMLシグナルを『Next Best Action』層でMCP経由のエージェント推奨に変換
title_original: 'From Prediction to Action: How to Turn AI Outputs into Decisions'
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- decision-execution
- ai-agent
- context-engineering
components:
- XGBoost
- Model Context Protocol (MCP)
- Next Best Action
outcome:
  type: productivity
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/from-prediction-to-action-how-to-turn-ai-outputs-into-decisions/
published_at: '2026-08-24'
---

## 概要

Salesforceの営業担当は約12,000のダッシュボードと20以上のアプリからの予測・スコアに埋もれ、モデルは正確でも『何をすべきか』が分からない状態だった。同社はモデル出力を『答え』ではなく『シグナル』と位置付け直し、シグナル・ビジネスロジック(閾値や優先順位)・暗黙知(熟練者の経験知)の3つを融合する『Next Best Action』層を新設して、行動・対象・根拠・期待効果を含む推奨を生成する構成に転換した。さらにMCPを契約として使い、エージェントが実行時に必要なツール(Next Best ActionレコードやKPI履歴など)を判断して呼び出せるようにしている。

## 設計のポイント

- モデル出力を『答え』ではなく『シグナル(assessment)』として扱い、行動を決める層(action)をあえて分離して設計する
- シグナル・ビジネスルール・暗黙知という3種類の異なる性質の情報を1つの推奨(行動・対象・根拠・期待効果)に統合するレイヤーを新設した
- スケールしやすい『シグナル』とスケールしにくい『暗黙知』を区別し、ボトルネックがモデル精度ではなく知識の欠落にある場合は新しいモデルを作らない
- MCPをエージェントと推奨レイヤーの間の契約として使い、全経路をハードコードせずエージェントが実行時に必要なツールを選択できるようにする

## 使いどころ

- 大量のダッシュボード・アラート・スコアが乱立し、ユーザーが『次に何をすべきか』を判断できずにいる社内システム
- 予測モデルの精度は十分なのに利用率や行動率が上がらない場合の、システム設計側の原因切り分け
- 複数のAIエージェントに、統一された推奨・意思決定ロジックを安全に呼び出させたいプラットフォームチーム
