---
type: guidance
title: Claude Tagの『エージェントアイデンティティ』:自律型・マルチプレイヤーAIのための新アクセスモデル
title_original: 'Agent identity in Claude Tag: a new access model for autonomous, team-wide AI'
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- defense-in-depth
- guardrails
components:
- Claude Tag
- Slack
- GitHub
- Google Drive
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/agent-identity-access-model
published_at: '2026-06-24'
---

## 概要

Claude TagはSlackの共有チャンネルで複数人と同時に働くため、単一ユーザーの権限を借用する『なりすまし』モデルではなく、Claude自身がSlackアプリ・GitHub App・サービスアカウントとして各システムに専用アカウントを持つ『エージェントアイデンティティ』モデルを採用した。管理者はワークスペース単位でベースラインの接続・スキル・指示を定義し、各チャンネルがそれを継承しつつ個別に権限を上書き・縮小できる。プライベートチャンネルごとに独立したidentityとメモリ境界を持たせることで、共有チャンネルが個人の非公開ドキュメントへの抜け道になることを防いでいる。

## 設計のポイント

- ユーザーの権限を代行する『act as the user』方式をやめ、Claudeがシステムごとに専用アカウント(GitHub App、サービスアカウント等)を持つ独立identityモデルに転換した。
- ワークスペースレベルでベースラインの接続・リポジトリアクセス・スキル・標準指示を定義し、各チャンネルがそれを継承しつつ必要に応じて上書きできる階層構造にした。
- パブリックチャンネルはワークスペース共有identity、プライベートチャンネルは個別identityとし、学習した記憶やアクセス範囲をチャンネル境界で分離した。
- DMは各ユーザー個人のclaude.aiアカウント権限で動作させ、共有チャンネルのagent identityとは明確に異なる権限モデルとして使い分けている。

## 使いどころ

- 複数人が同時にステアリングする共有Slackチャンネルで、AIエージェントに『誰か一人の権限』ではなく独自の権限を持たせたい管理者。
- リポジトリ・データウェアハウス・ドキュメントなど複数システムを横断してAIエージェントに作業させたいエンジニアリング/データチーム。
- エージェントが自律的に稼働する時間が長くなる中、個々のユーザーアカウントを監査する代わりに単一identityの失効で全アクセスを一括管理したい組織。
- 法務・エンジニアリングなど部署ごとにアクセス境界を厳密に分離しつつ、監査証跡を見ながら段階的に権限を拡張していきたい企業。
