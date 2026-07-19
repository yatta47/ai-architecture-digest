---
type: case
title: CursorのAI生成コード検証アーキテクチャ：リスクスコアリングと行動証跡でレビューを自動配分
title_original: 'Inside Cursor''s agent factory: how it verifies AI-written code'
company: Cursor
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- eval
- human-in-the-loop
- ci-cd
components:
- Bugbot
- Anthropic
- OpenAI
- Gemini
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/inside-cursors-agent-factory-how-it-verifies-ai-written-code/
published_at: '2026-07-17'
---

## 概要

CursorはAIエージェントが書いたコードを信頼するため、CI・セキュリティレビュー・リスクスコアリング・行動証跡（動画/スクリーンショット）・専門レビューエージェントを組み合わせた検証アーキテクチャを構築している。リスクスコアに応じて低リスクなPRは自動マージ、高リスクなPRは適切な人間レビューアへルーティングし、人間による訂正はレビューエージェントBugbotの学習ルールと評価ケースとして蓄積され、全体としてPRの約3〜4割が人手レビュー無しでマージされているという。

## 設計のポイント

- CI・セキュリティレビュー・デモ証跡から収集した証拠にリスクスコアを付け、閾値以下は自動マージ・それ以外は適切な人間レビューアへルーティングするポリシーとして分離する
- エージェントに開発者相当の実行環境を与え、diffだけでなく動画やスクリーンショットなど『動作した証拠』を成果物として返させる
- 人間によるレビュー訂正をBugbotの学習ルール・回帰評価ケースとして蓄積し、レビューエージェント自体の精度を継続的に測定・改善する
- スキルライブラリは増やし続けるのではなく刈り込み、指示の量より的確なコンテキストを優先する

## 使いどころ

- 大量のAI生成PRを抱え、人手レビューのボトルネックを解消したい開発組織
- コーディングエージェントの出力を安全に自動マージするための承認ポリシーを設計したいプラットフォームチーム
- PRレビューエージェントの精度を継続的に計測・改善する仕組みを作りたいチーム
