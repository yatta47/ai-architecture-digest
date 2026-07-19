---
type: case
title: CursorがClaude Fable 5を独自ベンチマークで評価した事例
title_original: 'Working at the frontier: How Cursor knew Claude Fable 5 was ready for the hardest 1% of problems'
company: Cursor
industry: cross-industry
cloud: []
patterns:
- eval
- ai-agent
components:
- Claude Fable 5
- CursorBench
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/working-at-the-frontier-cursor
published_at: '2026-07-17'
---

## 概要

AIコーディングエージェントのCursorは、独自ベンチマークCursorBenchで実際の開発者の曖昧なプロンプトを模した評価を行い、Claude Fable 5が72.9%という新記録を達成したことを紹介。トレースを実際に監査して高スコアの妥当性を検証し、モデルが「グローバルな推論」で複雑なタスクの全体像を把握できることを確認した。

## 設計のポイント

- 公開ベンチマークと実際の開発者評価が乖離してきたため、曖昧な実プロンプトを再現する独自評価(CursorBench)を構築する。
- スコアが異常に高い場合はトレースを実際に読み、正当な高性能かベンチマークの穴かを人手で検証する。
- effort設定を用途に応じて使い分け、低effortでも従来モデルの最高effort相当の性能が出せるかを確認する。

## 使いどころ

- フロンティアモデルを実運用タスクに投入する前に定量評価したい開発ツール企業。
- 曖昧で長時間かかるエージェントタスクにどのモデルを割り当てるか判断したいエンジニアリングチーム。
