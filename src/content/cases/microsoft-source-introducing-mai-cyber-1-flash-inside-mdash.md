---
type: announcement
title: セキュリティ専用モデルMAI-Cyber-1-Flashと多エージェント脆弱性対応基盤MDASH
title_original: Introducing MAI-Cyber-1-Flash inside MDASH
company: Microsoft
industry: other
cloud:
- azure
patterns:
- multi-agent-orchestration
- multi-model-routing
- reinforcement-learning
- guardrails
components:
- MAI-Cyber-1-Flash
- MDASH
- GPT-5.4
- MAI-Thinking-1
- Project Perception
outcome:
  type: cost
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://microsoft.ai/news/introducing-mai-cyber-1-flash-inside-mdash/
published_at: '2026-07-27'
---

## 概要

Microsoftはコード脆弱性検出に特化した小型モデルMAI-Cyber-1-Flashを発表し、100以上のエージェントで構成される脆弱性発見・検証・修復ハーネスMDASH上で運用する。タスクの9割を軽量モデルで処理し、真に難しい1割のみ大型モデル（GPT-5.4）に回すルーティングにより、CyberGymベンチマークで96%を達成しつつコストを50%削減した。

## 設計のポイント

- 大半のタスクは安価な専用モデルで処理し、真に困難なタスクのみ高コストな大型モデルへルーティングするマルチモデル構成でコストと精度を両立する
- 脅威調査→修復→結果学習のループを継続的な強化学習ループとして捉え、実運用のフィードバックでモデルを継続改善する
- ロールベース制御・テナント分離・サンドボックス実行・インターネット非接続などエンタープライズ向けガバナンスを基盤に組み込む

## 使いどころ

- 膨大な量の脆弱性スキャン・トリアージをコストを抑えながらAIで自動化したいセキュリティ運用チーム
- 1つの大型モデルに全タスクを流すのではなく難易度に応じてモデルを使い分けたいAI基盤チーム
