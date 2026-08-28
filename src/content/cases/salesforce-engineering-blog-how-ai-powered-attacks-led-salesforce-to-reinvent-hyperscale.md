---
type: case
title: Salesforce、AI推論とTemporalオーケストレーションで秒単位のDDoS防御基盤DREAMを構築
title_original: How AI-powered attacks led Salesforce to reinvent hyperscale DDoS defense
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- defense-in-depth
- event-driven
- ai-agent
components:
- Temporal
outcome:
  type: speed
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/how-ai-powered-attacks-led-salesforce-to-reinvent-hyperscale-ddos-defense/
published_at: '2026-08-28'
---

## 概要

SalesforceはAIで自動生成・進化する機械速度の攻撃に対抗するため、450万ドメイン・300万顧客組織を守るDDoS対策基盤DREAMを3か月強で全面刷新した。テレメトリ・AI推論・ポリシー配布・通知を跨ぐ長時間実行ワークフローを、状態管理やリトライを自前実装せずTemporalの分散オーケストレータに委ね、コーディングをAIアシスト（約10万行を移行、90%以上がAI支援）で加速することで最初のMVPを3週間で完成させた。結果、初動緩和までの時間を5倍高速化した。

## 設計のポイント

- 状態管理・リトライ・分散ロックなどの分散システムのプリミティブは自前実装せず、Temporalのような分散オーケストレータに委譲し、差別化要素（防御ロジック）に開発リソースを集中する
- AI駆動の推論を、決定的なワークフローオーケストレーション層と分離し、外部副作用（推論・通知・ポリシー配布）としてアクティビティ化する
- AIコーディングアシスタントを大規模移行（レガシー10万行）に活用しつつ、コーディング規約・人間レビュー・95%超のテストカバレッジで品質を担保する
- 大きなテレメトリペイロードをオーケストレーション層に直接流さず、転送サイズの上限を踏まえてデータとワークフロー制御を分離する

## 使いどころ

- マルチテナント基盤で一つの攻撃が他の顧客にも波及するリスクを抱えるクラウド事業者のセキュリティ基盤刷新
- レガシーの緩和プラットフォームのライセンス期限が迫る中、短期間で本番信頼性のある置き換えを行う必要がある場合
- AIコーディングアシスタントを使って大規模なレガシーコード移行を加速したいエンジニアリング組織
