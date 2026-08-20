---
type: case
title: Fanatics Betting and Gamingが構築したスポーツベッティング向けマルチエージェントサポート
title_original: How Fanatics Betting and Gaming built a multi-agent customer support system
company: Fanatics Betting and Gaming
industry: other
cloud:
- aws
patterns:
- multi-agent-orchestration
- rag
- guardrails
- human-in-the-loop
components:
- Amazon Bedrock
- Amazon EKS
- Amazon Bedrock Guardrails
- Amazon Nova
- Anthropic Claude
- Salesforce Einstein
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-fanatics-betting-and-gaming-built-a-multi-agent-customer-support-system/
published_at: '2026-08-19'
---

## 概要

スポーツベッティングのFanatics Betting and Gaming（FBG）は、州ごとに異なる規制やライブイベント時の急増する問い合わせに対応するため、AWS上にオーケストレーターパターンのマルチエージェントカスタマーサポートシステムを構築した。Amazon Bedrock上のClaudeが動くSupervisor Agentが、RAG・アカウント/取引照会用MCPツール・有人転送ツールを使い分け、Amazon Nova搭載のResponsible Gaming分類エージェントが問題賭博の兆候を検知して高リスク時は即座に人間へエスカレーションする。

## 設計のポイント

- 単一の巨大チャットボットではなく責任範囲の明確な専門エージェントに分割し、既存のAmazon EKS基盤の上でそれぞれを独立にデプロイ・スケール・改善できるようにする
- Amazon Bedrockのモデル非依存性を活かし、タスクごとに最適なモデルを選び新しいモデルが出た際も入れ替えやすくする
- Supervisor Agentがオーケストレーターとして意図判定しRAG/アカウント照会/取引照会/有人転送の各ツールを呼び分けることで、新しいツールやビジネスユニットの追加時も中核システムを書き換えずに拡張できる
- Amazon Bedrock Guardrailsによるプロンプトインジェクション対策と、コンプライアンス承認済みの分類フレームワークで動く責任あるゲーミング分類エージェントを、モデルの推論経路とは別の防御レイヤーとして組み込む

## 使いどころ

- 州・地域ごとに規制が異なる業種で、問い合わせ内容に応じて正確な規制情報を返す必要があるサポート窓口
- ライブイベントなどで問い合わせが急増し、既存のヒューマンオンリーサポートでは対応コストが線形に膨らんでしまう場合
- コンプライアンス上、特定の会話パターンを検知したら即座に人間へエスカレーションする必要がある業種（問題賭博・与信など）
