---
type: guidance
title: エージェントの『頭脳』と実行サンドボックスを分離するClaude Managed Agentsの設計
title_original: 'The evolution of agentic surfaces: building with Claude Managed Agents'
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- reasoning-computation-separation
- context-engineering
- multi-agent-orchestration
components:
- Claude Managed Agents
- Claude Agent SDK
- Claude Code
- OpenTelemetry
outcome:
  type: speed
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/building-with-claude-managed-agents
published_at: '2026-06-10'
---

## 概要

AnthropicはトークンをやりとりするだけのシンプルなAPIから、Claude Codeのハーネス、Claude Agent SDK、そして本番運用向けのClaude Managed Agentsへとエージェント基盤を進化させてきた。Managed Agentsは、Claudeを呼び出す推論用ハーネスとコードを実行するサンドボックスを分離し、両者をすべてのモデル呼び出し・ツール呼び出し・結果を記録する追記専用の「セッション」でつなぐことで、ホスティング、セッション管理、実行分離、認証情報保護、可観測性といった本番運用課題をまとめて引き受ける。この設計により、コンテナ起動前から推論を始められ、認証情報をコード実行環境から遠ざけつつ、任意の時点からランを再構築できるようになっている。

## 設計のポイント

- 推論を担うハーネスとコードが実行されるサンドボックスを分離し、両者を追記専用のセッションログで接続することで、コンテナ起動前から推論を開始できるようにした。
- セッションに全モデル呼び出し・ツール呼び出し・結果を記録することで、中断からの再開や任意時点でのラン再構築を可能にしている。
- 認証情報をサンドボックス(コード実行環境)から切り離して配置し、生成されたコードの実行が直接クレデンシャルに触れない構成にした。
- モデルの世代交代(例: Sonnet 4.5からOpus 4.5)に伴う挙動変化に合わせて、ハーネス側の前提(コンテキストリセットなど)を継続的に見直す運用を組み込んでいる。

## 使いどころ

- 数時間規模の長時間タスクをこなすエージェントを、自前でホスティング・スケーリング基盤を構築せずに本番投入したいチーム。
- 生成したコードの実行環境を認証情報から隔離し、想定外の挙動が起きた際の被害範囲を限定したい場合。
- 複数エージェントのオーケストレーションや失敗時の回復処理を、独自のループ実装なしで運用したいチーム。
- プロトタイプから本番稼働までのリードタイムを数か月から数日に短縮したい開発組織。
