---
type: announcement
title: Claude Codeの動的ワークフロー：数百のサブエージェントを並列実行するオーケストレーション機能
title_original: Introducing dynamic workflows in Claude Code
company: Anthropic
industry: cross-industry
cloud:
- multi-cloud
patterns:
- multi-agent-orchestration
- parallel-execution
- ai-agent
components:
- Claude Code
- Claude API
- Amazon Bedrock
- Vertex AI
- Microsoft Foundry
outcome:
  type: speed
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
published_at: '2026-05-28'
---

## 概要

Claude Codeが、タスクをサブタスクに分解し数十〜数百のサブエージェントを並列実行してから結果を検証する「動的ワークフロー」機能を発表。エージェント同士が独立した視点から取り組み、互いの結果を検証し合うことで、単独パスでは届かない精度と規模の作業をこなせるとしている。BunのZig→Rust移植（75万行、11日間）が実例として紹介されている。

## 設計のポイント

- オーケストレーションスクリプトを動的に生成し、数十〜数百のサブエージェントを並列実行して大規模タスクを分解する
- 結果を折り込む前に別エージェントが検証し、複数の視点からの意見を収束させることで単独パスでは届かない精度を実現する
- 進捗はセッション外で保存されるため、中断されたジョブも最初からやり直さずに再開できる
- 初回起動時に使用量の見積もりを提示し確認を求めることで、通常セッションより多いトークン消費を制御する

## 使いどころ

- リポジトリ全体のバグハントやセキュリティ監査など、単一エージェントでは処理しきれない大規模タスクに使う
- フレームワーク移行や言語ポートなど、数百〜数千ファイルにまたがる大規模マイグレーションに向く
- 誤りのコストが高い重要な意思決定を、独立した複数の試行とアドバーサリアルなレビューで検証したい場面に使う
