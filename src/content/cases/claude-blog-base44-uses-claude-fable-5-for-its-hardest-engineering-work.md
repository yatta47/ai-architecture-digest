---
type: case
title: Base44がシステムプロンプト全面刷新をClaude Fable 5に委ねた事例
title_original: 'Working at the frontier: Why Base44 trusts Claude Fable 5 with their most challenging engineering work'
company: Base44
industry: cross-industry
cloud: []
patterns:
- ai-agent
- spec-driven-development
- context-engineering
components:
- Claude Fable 5
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/working-at-the-frontier-why-base44-trusts-claude-fable-5-with-their-most-challenging-engineering-work
published_at: '2026-07-15'
---

## 概要

vibeコーディングプラットフォームBase44は、これまでシニアエンジニアしか任せられなかったシステムプロンプトの全面書き換えやネイティブモバイル基盤の刷新をClaude Fable 5に任せた。数時間の自律実行で必要な変更の90〜95%を完成させ、当日中にA/Bテストで検証・出荷できた。

## 設計のポイント

- モデルが詰まった際に「同じ問題が既に別の場所で解決されているはず」と自ら推論しコードベースを探索して修正する挙動を活用する。
- 既存のA/Bテスト基盤で生成された変更を即座に測定・検証し、その日のうちに出荷判断できるようにする。
- モデル自身にeval自体の欠陥(キャッシュヒット計測の抜け漏れなど)を発見・指摘させ、盲点を潰す。

## 使いどころ

- シニアエンジニアのボトルネックになっている複雑な基盤変更を委譲したいプロダクト/エンジニアリングチーム。
- プロダクトマネージャーやデザイナーが自ら大きめの実装をエージェントに任せたい組織。
