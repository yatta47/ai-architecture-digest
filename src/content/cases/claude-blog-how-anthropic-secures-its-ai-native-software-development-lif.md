---
type: case
title: コードの8割をAIが書く時代のソフトウェア開発ライフサイクル セキュリティ設計
title_original: How Anthropic secures its AI-native software development lifecycle
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- ci-cd
- defense-in-depth
- human-in-the-loop
components:
- Claude Code
- Claude Tag
- Claude Opus
- CLAUDE.md
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle
published_at: '2026-07-21'
---

## 概要

Anthropicでは、マージされるコードの約8割をClaudeが執筆し、半数以上が社内版Claude Tagによってマージされるまでに開発ライフサイクルが変化した。これに対応するため、セキュリティチームはシフトレフト、権限・ID境界によるブラスト半径の縮小、決定論的レビューとエージェントによるレビューの組み合わせ、そして人間を最もレバレッジの高いポイントに介在させる、という4つの戦略を軸にSDLC全体のセキュリティを再設計している。計画段階ではClaude Opusによる自動プロジェクトセキュリティレビュー(PSR)を社内ナレッジインデックスと連携させ、コーディング段階ではCLAUDE.mdにセキュアコーディング指針を組み込み、生成と同時にベストプラクティスを適用している。

## 設計のポイント

- Claude Opus搭載の自動プロジェクトセキュリティレビュー(PSR)を社内ナレッジインデックスに接続し、組織のポリシーや過去の意思決定を踏まえたリスク評価を行う。
- CLAUDE.mdファイルや組織横断のスキルにセキュアコーディング指針を明文化し、コード生成の瞬間からベストプラクティスが適用されるようにする。
- AIがリスクを低いと判定したプロジェクトはチーム自身が承認できるようにし、人間のレビューを最もレバレッジの高い意思決定ポイントに集中させる。
- エージェントが新たなバグクラスを発見するたびに関連するガイドファイルを更新し、再発防止を自動で組み込むクローズドループを構築する。

## 使いどころ

- コードの大半をAIエージェントが生成・マージする組織で、開発速度を落とさずにセキュリティレビューを継続したい場合。
- セキュリティ担当者が限られる中、低リスク案件は自動承認し、人手を高リスク判断に集中させたい場合。
- 過去のレビューや組織知識をエージェントのセキュリティ判断に継続的に反映し、脆弱性の再発を防ぎたい開発チーム。
