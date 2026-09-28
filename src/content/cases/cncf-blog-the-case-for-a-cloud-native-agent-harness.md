---
type: opinion
title: デスクトップ型ハーネスの限界を超える、分散システムとして設計されたエージェント実行基盤（Mecatl）
title_original: The case for a cloud-native agent harness
company: Stacklok
industry: cross-industry
cloud:
- multi-cloud
patterns:
- ai-agent
- unified-runtime
components:
- Mecatl
- mecatui
- MCP
- Kubernetes
- SPIFFE
outcome:
  type: reliability
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/09/28/the-case-for-a-cloud-native-agent-harness/
published_at: '2026-09-28'
---

## 概要

従来のコーディングエージェント用ハーネスはUI・エージェントループ・サンドボックス・資格情報ストア・ツールホストが1台のマシンに密結合した『デスクトップ型』設計であり、多数セッションの運用やノード障害への対応に不向きだと指摘する。Stacklokはこれをエージェントループとその周辺（クライアント・実行環境・ツール・状態管理）を明確なインターフェースで分離した分散システム『Mecatl』としてオープンソース化した。

## 設計のポイント

- エージェントループ（推論・ツール呼び出し・権限・フック）をコアエンジンとして独立させ、ターミナル・API・アプリケーションクライアントはループを所有せず接続するだけにする。
- セッション状態とイベント履歴をシングルライター調整モデルの永続ストレージに保持し、ワーカーが死んでも直近のターン境界から再開できるようにする（ターン単位の永続性）。
- 無制限シェルを前提とせず、ツール・スキル・アプリ連携を許可リストのカタログとして公開し、権限・監査・実行環境の境界をツールごとに明示する。

## 使いどころ

- 数百セッション規模でエージェントを運用し、ノード障害やデバイス間の引き継ぎに耐えたい組織。
- ターミナル・Web UI・Slack連携など複数クライアントから同じエージェントループにアクセスさせたい場合。
