---
type: guidance
title: マルチエージェントシステムの使いどころ判断フレームワーク
title_original: 'Building multi-agent systems: When and how to use them'
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- context-engineering
- parallel-execution
components:
- Claude
- Claude Agent SDK
- Claude Managed Agents
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them
published_at: '2026-01-23'
---

## 概要

本記事はAnthropicが、いつマルチエージェントシステムを採用すべきかを整理したガイダンスである。多くの業務では単一エージェントで十分な性能が出る一方、コンテキスト汚染の回避・並列実行・専門特化が有効な3つの状況でのみマルチエージェント化の投資対効果が正当化されると論じている。実測ではマルチエージェント構成は同等タスクに対しシングルエージェントの3〜10倍のトークンを消費するとしている。

## 設計のポイント

- まず単一エージェントで十分かを検証し、複雑なオーケストレーションは最後の手段として検討する
- サブタスクが1000トークン超の情報を生成しつつ本筋には不要な場合、専用サブエージェントに隔離してコンテキスト汚染を防ぐ
- 探索空間が広い調査・検索タスクには並列実行するサブエージェント群を割り当てて精度を高める
- オーケストレーター配下のサブエージェントという階層型パターンから始め、複雑な協調パターンは段階的に導入する

## 使いどころ

- 注文履歴照会など大量情報を伴う問い合わせ対応で、主エージェントの推論品質を保ちたい場合
- 同時に複数の観点を調査するリサーチ・検索タスクで網羅性と精度を高めたい場合
- コーディネーションコストよりも明確な効果が見込める場合にのみマルチエージェント投資を判断したいアーキテクト
