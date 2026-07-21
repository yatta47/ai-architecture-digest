---
type: case
title: Azure全体の健全性をAIでリアルタイムにモデル化する信頼性システム「Brain」
title_original: 'Meet Brain: The AI system behind Azure reliability'
company: Microsoft Azure
industry: cross-industry
cloud:
- azure
patterns:
- root-cause-analysis
- ai-agent
- decision-execution
- event-driven
components:
- Azure Resource Graph
outcome:
  type: reliability
source_id: azure-blog
source_name: Azure Blog
source_url: https://azure.microsoft.com/en-us/blog/meet-brain-the-ai-system-behind-azure-reliability/
published_at: '2026-07-02'
---

## 概要

Microsoft Azureは、Azure Resource Graph上に構築したAIOps基盤「Brain」を公開した。SLI・サービス個別の監視・サードパーティ指標などの信号を統合し、サービス/リージョン/顧客リソースごとに健全性・重大度・影響範囲・原因を継続的に算出することで、障害宣言や顧客通知、危険なデプロイのブロック、インシデントのルーティングなどの信頼性アクションを自動化している。Brainはトポロジー・サービスカタログ・実行時状態・意図・履歴・顧客視点という要素を保持する『Azureのデジタルツイン』として機能し、今後のエージェント型AI運用の基盤にもなるという。

## 設計のポイント

- Azure Resource Graphの上にAIOpsレイヤーを重ね、トポロジー・サービスカタログ・実行時状態・意図（進行中のデプロイ/変更）・過去のインシデント履歴・顧客視点を統合した『デジタルツイン』としてプラットフォームの健全性を継続的にモデル化する。
- 健全性判定の出力を『health state・severity・impact・reason』という共通語彙に標準化し、下流の障害宣言・通知・デプロイゲート・インシデントルーティングなど複数の自動化システムが同じ意味論で連携できるようにする。
- SLI・サービス固有の監視・サードパーティ指標という3系統の異なる信号源を並行して取り込み、単一の経路では得られない網羅的なカバレッジを確保する。
- 推論結果をダッシュボード提示に留めず、危険なロールアウトを止めるデプロイゲートや障害範囲に基づく自動アウテージ宣言など、実際のアクション実行にまで接続する。

## 使いどころ

- 数百のサービスと80以上のリージョンを抱えるハイパースケールクラウドで、人手によるダッシュボード監視が信号量に追いつかなくなった運用チームの意思決定を支援する。
- 顧客が自ら不具合に気づく前にプラットフォーム側が検知し、影響を受けるサブスクリプション/リージョン単位で通知したい場合。
- デプロイの安全性をリアルタイムに評価し、有害なロールアウトを自動的に一時停止させたいプラットフォームチーム。
