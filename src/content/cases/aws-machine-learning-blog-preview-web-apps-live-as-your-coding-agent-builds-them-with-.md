---
type: guidance
title: コーディングエージェントが作るWebアプリをセッション内でライブプレビューする構成
title_original: Preview web apps live as your coding agent builds them with Amazon Bedrock AgentCore runtime
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- human-in-the-loop
components:
- Amazon Bedrock AgentCore
- AgentCore runtime
- Session endpoints
- Vite
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/preview-web-apps-live-as-your-coding-agent-builds-them-with-amazon-bedrock-agentcore-runtime/
published_at: '2026-10-30'
---

## 概要

AgentCore runtimeはエージェントのセッションごとに隔離したmicroVMで動かし、Session endpointsで認証付きURLを発行して許可ポートへHTTP/WebSocketを転送する。これによりエージェントが編集中のViteアプリをブラウザで即時に確認でき、デプロイ待ちなしにレビューと修正依頼を回せる。

## 設計のポイント

- アプリをエージェントが編集する同一セッション内で動かし続け、変更を数秒でブラウザに反映する。
- セッションごとに認証付きエンドポイントを発行し、許可したポートだけにリクエストを転送する。
- HTTPメソッド・パス・クエリ・ボディとWebSocketを透過させ、HMRを含む開発サーバーをそのまま利用する。

## 使いどころ

- プロダクトチームがエージェント生成のプロトタイプを試しながら修正を依頼する場面。
- コーディングエージェントのレビュー速度をデプロイ待ちから解放したい開発組織。
