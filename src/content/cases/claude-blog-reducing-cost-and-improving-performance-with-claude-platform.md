---
type: guidance
title: Claude Platformのプロンプトキャッシュと指示チューニングによるコスト削減
title_original: Reducing cost and improving performance with Claude Platform
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- prompt-optimization
- context-engineering
- cost-optimization
components:
- Claude Platform
- Claude Console
- claude-api skill
- Claude Code
outcome:
  type: cost
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/reducing-cost-and-improving-performance-with-claude-platform
published_at: '2026-09-08'
---

## 概要

Anthropicは、プロンプトキャッシュのヒット率最大化・フロンティアモデル向けの過剰な指示（アンチパターン）の除去・タスクに応じたeffort調整という3点で、性能を落とさずにClaude Platformのコストを削減できると解説している。claude-apiスキルにprompt-auditコマンドを追加し、CLAUDE.mdやツール定義に残る古い指示パターンを自動検出できるようにした。

## 設計のポイント

- キャッシュ可能な静的部分（system prompt・ツール定義）を先頭に固定し可変な会話部分を末尾に追記する構造にする
- タイムスタンプやIDなど揮発的な値をプレフィックスから排除しキャッシュ断絶を防ぐ
- めったに使わないツール定義はdefer_loadingでキャッシュ対象外にし必要時のみ差し込む
- compactionなどどのみちキャッシュが切れるタイミングにモデルやeffortの切り替えをまとめる

## 使いどころ

- 長い会話やサブエージェント呼び出しでプロンプトキャッシュのヒット率が低下し費用が膨らんでいるチーム
- 旧世代モデル向けの冗長な指示や検証儀式が残ったままフロンティアモデルに移行したアプリケーション
- レイテンシ低減のためセッション開始時にキャッシュを温めておきたいリアルタイム用途
