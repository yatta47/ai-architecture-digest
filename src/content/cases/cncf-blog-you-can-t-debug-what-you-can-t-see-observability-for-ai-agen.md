---
type: guidance
title: AIエージェント可観測性の三本柱:トレース・コスト・監査ログで『見えない失敗』を追う
title_original: 'You Can''t Debug What You Can''t See: Observability for AI Agents'
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llmops
- cost-optimization
- guardrails
components:
- Langfuse
- Prometheus
- Grafana
outcome:
  type: reliability
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/08/04/you-cant-debug-what-you-cant-see-observability-for-ai-agents/
published_at: '2026-08-04'
---

## 概要

本番でAIエージェントを運用してきた経験から、従来のAPMでは捉えられないループ・幻覚・トークン浪費といった障害を可視化する手法をまとめた記事。トレース(セッションの意思決定履歴)、コスト(セッション単位/日次のトークン燃焼)、監査(改ざん不可なログ)の三本柱と、doctor的な単一診断コマンド、異常セッションの自動フラグ付けを提案している。反応的なアラートだけでなく反復回数上限やツール呼び出し予算などの事前ガードレールを重視する点が特徴。

## 設計のポイント

- トレース送信は非同期のバッチエクスポーターで行い、バックエンド障害時はテレメトリのみを失い可用性は落とさない設計にする
- コスト超過対策は事後アラートだけに頼らず、反復回数上限・ツール呼び出し予算・同一呼び出し連続検出などのプリフライト回路遮断器を先に置く
- Prometheusのラベルはツール名・エージェント名など低カーディナリティな値に限定し、セッションIDのような一意識別子はトレースやログ側に任せる
- brew doctor的な単一診断コマンドでモデル接続・ベクトルストア・承認待ち・トレースバックエンドなど依存関係の健全性を一括確認できるようにする

## 使いどころ

- 本番でAIエージェントを多数稼働させ、コスト急増やループを人手監視より早く検知したいチーム
- 1日に数百セッション規模でエージェントが動き、全件手動レビューが不可能なため異常セッションの自動フラグ付けが必要な現場
- 監査ログから認証情報やPIIを除去しつつ、インシデント調査に耐える証跡基盤を整備したい組織
- メトリクス(アラート用)とトレース(デバッグ用)の役割を分離し、可観測性基盤を設計し直したいプラットフォームチーム
