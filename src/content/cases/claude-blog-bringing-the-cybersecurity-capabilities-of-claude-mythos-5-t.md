---
type: announcement
title: Claude Mythos 5の高度なサイバーセキュリティ能力を『直接アクセスさせず成果物だけ渡す』設計で防御側に拡大
title_original: Bringing the Cybersecurity Capabilities of Claude Mythos 5 to More Defenders
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- guardrails
- out-of-band-inference
- human-in-the-loop
- defense-in-depth
components:
- Claude Mythos 5
- Claude Security
- Claude Fable 5
- Claude Opus
- Claude Sonnet
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/bringing-claude-mythos-5-to-more-defenders
published_at: '2026-08-21'
---

## 概要

Anthropicは、最も高度なモデルClaude Mythos 5のサイバー防御能力を、モデルへの直接アクセスを許さず特定の成果物（パッチ候補や脆弱性所見）だけを渡すインターフェース経由でパートナー製品に統合し、より多くの防御チームへ届ける取り組みを発表した。Claude Enterprise向けのClaude SecurityはMythos 5でコードスキャンを実行し、CWE分類・信頼度・重大度付きの所見とパッチ案を返すが、実装は必ず人間のレビュー・承認を経る。オープンソースのセキュリティ維持を支援する3,500万ドル規模のDefender Advantage Fundも新設した。

## 設計のポイント

- モデルへの直接プロンプトアクセスは与えず、目的特化のインターフェース経由で決まったタスクだけをバックグラウンドで実行し、特定の成果物だけをユーザーに返す(直接アクセス vs 出力アクセスの分離)ことでデュアルユースリスクを下げる
- スキャン結果はCWE分類・信頼度・重大度付きの構造化された所見として返し、パッチの実装は必ず人間のレビュー・承認を経てから適用する
- 検証済みの防御者に対しては段階的に安全策を緩和するプログラム(Cyber Verification Program)を設け、一般提供モデルとは別の権限レベルを用意する
- モデル自体を配らずに資金(クレジット)を提供することで、リソースの乏しいOSSメンテナ組織のセキュリティ対応能力を底上げする

## 使いどころ

- 病院・公益事業・金融機関などクリティカルなソフトウェアを守るセキュリティチームが、最先端モデルの脆弱性発見能力を安全に使いたい場合
- サイバーセキュリティ製品ベンダーが、モデルへの直接アクセスを提供せずに高度なAI機能を自社製品に組み込みたい場合
- リソースの乏しいオープンソースプロジェクトのメンテナが、脆弱性のスキャン・パッチ適用を自動化したい場合
