---
type: case
title: オープン標準×マルチエージェントで実現する「エージェント型メディア購入」
title_original: Agentic media buying cannot scale without the right foundation
company: Databricks
industry: media
cloud:
- multi-cloud
patterns:
- multi-agent-orchestration
- ai-agent
- event-driven
components:
- Databricks Apps
- Databricks Model Serving
- CrewAI
- MCP
- IAB Tech Lab AAMP
- OpenDirect
- OpenRTB
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/agentic-media-buying-cannot-scale-without-right-foundation-see-how-buyers-and-sellers-get
published_at: '2026-07-30'
---

## 概要

Databricksは、広告の買い手・売り手エージェントがIAB Tech LabのAAMPオープン標準を介して自律的に交渉・取引する「エージェント型メディア購入」のリファレンス実装を構築。CrewAIによる階層型マルチエージェント構成をDatabricks Apps上で動かし、状態管理・モデル提供・データガバナンス・ID/信頼・可観測性を単一プラットフォームに統合する。

## 設計のポイント

- 買い手・売り手・レジストリを別個の主体として設計し、当事者間の通信はオープン標準(AAMP/OpenDirect/OpenRTB)に任せ、状態やIDをどこで保持するかはプラットフォームの責務として分離する
- 各当事者を自己完結したDatabricks Appsとして実装し、状態・ID・実行モデルを自分自身で保持したまま標準プロトコルのみで他者とやり取りする
- 買い手エージェントをCrewAIによる階層型マルチエージェント(3階層)構成にし、上位エージェントが下位の専門エージェントに委譲する
- 状態管理・モデル提供・ガバナンス済みデータ・ID/信頼・可観測性を単一プラットフォームにまとめ、複数ベンダー統合プロジェクトを避ける

## 使いどころ

- RFP・メール・電話でのやり取りが中心の従来型メディア購入プロセスを自動化したい広告主・パブリッシャー
- オープン標準に準拠した相互運用可能なエージェント間取引の実装例を探すチーム
- 複数の専門エージェントが連携して交渉・意思決定を行うマルチエージェントシステムの設計参考
