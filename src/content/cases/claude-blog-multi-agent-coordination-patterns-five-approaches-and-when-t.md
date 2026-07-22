---
type: guidance
title: マルチエージェント協調パターン5選と使い分けの指針
title_original: 'Multi-agent coordination patterns: Five approaches and when to use them'
industry: cross-industry
cloud:
- multi-cloud
patterns:
- multi-agent-orchestration
- ai-agent
components: []
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/multi-agent-coordination-patterns
published_at: '2026-04-10'
---

## 概要

生成-検証（generator-verifier）、オーケストレーター-サブエージェント、エージェントチーム、メッセージバス、共有状態という5つのマルチエージェント協調パターンを、それぞれの仕組み・向いている場面・限界とともに解説する。最も単純なパターンから始め、詰まった箇所を見ながら進化させることを推奨している。

## 設計のポイント

- 品質基準が明確な出力には、生成した結果を検証者が受理/差し戻しするgenerator-verifierパターンから始める
- タスクが明確に分解でき境界が定まっているならオーケストレーター-サブエージェント、独立した長時間タスクの並列実行にはエージェントチームを使う
- 見た目が洗練されているという理由でパターンを選ばず、単純な構成から始めて限界にぶつかったら次のパターンへ進化させる

## 使いどころ

- サポート返信のように明確な評価基準で品質を担保したい生成タスク
- サービス群やエージェントエコシステムが成長しイベント駆動の連携が必要になってきたプロダクト
- 複数エージェントが互いの発見を積み上げながら共同作業する調査・分析タスク
