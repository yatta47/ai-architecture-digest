---
type: case
title: Claudeによる自己サービス型データ分析基盤
title_original: How Anthropic enables self-service data analytics with Claude
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- text-to-sql
- ai-agent
- context-engineering
components:
- Claude Code
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude
published_at: '2026-06-03'
---

## 概要

Anthropicは社内のビジネス分析クエリの95%をClaudeで自動化し、集計レベルで約95%の精度を達成した。鍵となるのは、コンセプト-エンティティの曖昧性・データの陳腐化・検索失敗という3つの失敗要因にそれぞれ対応する「データ基盤・保守検証・スキル」からなるエージェント型分析スタックであり、これにより従来ルーチンだった分析業務をClaudeに委ね、データサイエンスチームは因果モデリングや予測などより戦略的な仕事に集中できるようになった。

## 設計のポイント

- 少数の厳格に統治されたカノニカルなデータセットに集約し、類似の重複データセットは積極的に廃止することでコンセプト-エンティティの曖昧性を解消する
- データ基盤・鮮度検証プロセス・スキルという3層構造で、曖昧性・陳腐化・検索失敗という異なる失敗モードにそれぞれ対応する
- コーディングエージェントと異なり分析エージェントには唯一の正解しかないため、コード生成の自由度よりもデータモデルの曖昧性解消を最優先課題と位置づける

## 使いどころ

- SQLを書けない非技術系のビジネスユーザーからのアドホックな分析依頼を自動化したいデータチーム
- ダッシュボードやメトリクス定義の乱立に悩む急成長中の組織におけるデータガバナンス強化
- データサイエンティストをルーチンな集計業務から解放し、因果推論や予測モデリングに再配置したい場合
