---
type: announcement
title: エージェントのツール実行を自社インフラに隔離するセルフホストサンドボックスとプライベートMCP接続
title_original: 'New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels'
industry: cross-industry
cloud:
- multi-cloud
patterns:
- ai-agent
- unified-runtime
- confidential-computing
- llm-gateway
components:
- Claude Managed Agents
- Cloudflare
- Daytona
- Modal
- Vercel
- Messages API
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-managed-agents-updates
published_at: '2026-05-19'
---

## 概要

Claude Managed Agentsに、エージェントのツール実行を顧客が管理するサンドボックスに委譲する「セルフホストサンドボックス」と、社内ネットワークのMCPサーバーに安全に接続する「MCPトンネル」が追加された。オーケストレーションやコンテキスト管理はAnthropic側に残しつつ、コード実行やデータは企業の境界内に留まる構成で、Cloudflare・Daytona・Modal・Vercelなどのマネージドサンドボックスプロバイダも選択できる。Amplitude、Clay、Rogoなど複数企業が採用事例として紹介されている。

## 設計のポイント

- エージェントループ（オーケストレーション・コンテキスト管理・エラー回復）はAnthropic側のインフラに残し、ツール実行のみを顧客が管理する環境に分離するアーキテクチャ。
- サンドボックスはセルフホストまたはCloudflare/Daytona/Modal/Vercelなどのマネージドプロバイダから選択でき、リソースサイジングやランタイムイメージは利用者側で制御する。
- MCPトンネルは軽量ゲートウェイによるアウトバウンド接続のみを使い、インバウンドのファイアウォール開放や公開エンドポイントなしに社内MCPサーバーへアクセスさせる。

## 使いどころ

- 金融や法務など機密データを扱う企業が、コード実行やファイルを自社のセキュリティ境界内に留めたままAnthropicのエージェントループを利用したい場合。
- 社内データベースやチケットシステムなど公開できない内部システムを、外部公開せずにエージェントのツールとして使わせたい場合。
- 長時間ビルドや画像生成などコンピュート要求の大きいワークロードで、自前のCPU/メモリ/ランタイムを調整したい場合。
