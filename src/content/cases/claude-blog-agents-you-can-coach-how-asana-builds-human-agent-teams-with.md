---
type: case
title: AsanaのWork Graph上で役割・権限・共有メモリを持つAIチームメイト運用
title_original: 'Agents you can coach: how Asana builds human-agent teams with Claude'
company: Asana
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- human-in-the-loop
- guardrails
components:
- Claude
- Asana Work Graph
- AI teammates
- Google Drive
- Slack
- HubSpot
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/agents-you-can-coach-how-asana-builds-human-agent-teams-with-claude
published_at: '2026-09-29'
---

## 概要

Asanaは、タスク・プロジェクト・目標を関係づけるWork Graphモデルの中でAIエージェント（AI teammates）を人間と同じように動かし、Claudeモデルで複雑なタスクを処理している。エージェントは役割・スキル・連携・権限をプロファイルで定義され、実効アクセスは起動した人の権限に制限される。共有メモリへの恒久的なフィードバック反映は管理者・編集者のみに限定し、作業はアクティビティフィードで全員に可視化される。

## 設計のポイント

- AI専用の新しいコンテキスト構造を作らず、既存のWork Graph（担当者・依存関係付きのタスク構造）をエージェントのコンテキストとして使う。
- エージェントの実効アクセス権を起動したユーザーの権限で上限づけ、プライベート文脈で得た情報の漏えいリスクを抑える。
- 誰でもタスク単位のフィードバックはできるが、共有メモリへのコミット・取り消し・削除は管理者・編集者のみに限定し、利用と訓練を分離する。
- エージェントをコンテンツライターやインサイトアナリストなどの役割単位で定義し、事前構築スキルと必要な連携を持たせる。

## 使いどころ

- 社内の業務プラットフォーム上でAIエージェントを人間の同僚と同じ扱いで運用したい組織。
- ブランドボイスなど品質基準を持つチームが、エージェントの振る舞いを専門家だけで管理したい場面。
- Slackや会議メモなど非構造な情報をタスク化し、エージェントに引き継がせたいチーム。
