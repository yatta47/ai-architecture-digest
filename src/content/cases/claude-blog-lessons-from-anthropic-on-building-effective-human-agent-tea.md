---
type: guidance
title: Slackに常駐する『マルチプレイヤーエージェント』で実現する人間×AIチーム運用の設計指針
title_original: Building effective human-agent teams
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- context-engineering
- human-in-the-loop
components:
- Claude Tag
- Slack
- BigQuery
- Playwright MCP
- Claude.ai
- Claude Cowork
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/building-effective-human-agent-teams
published_at: '2026-06-24'
---

## 概要

AnthropicはClaude Tagのようなツールにより、単一ユーザーとエージェントの1対1対話から、複数人と複数エージェントが同じワークスペースで協働する『マルチプレイヤーエージェント』へ働き方が移行していると説明する。エージェントが永続メモリ・独自クレデンシャル・組織情報への広範なアクセスを持ち、チームの一員として機能するための技術基盤と、社内で実践している運用ルールを2つの教訓として紹介している。

## 設計のポイント

- エージェントに永続的メモリ、人に紐付かない独自クレデンシャル、組織情報への継続的な広範アクセスを持たせ、チームの正式なメンバーとして機能させる
- 情報共有はドキュメント/チャンネル単位の個別判断ではなく、ワークスペース全体に適用される少数の明確なセキュリティ境界で管理し、意思決定疲れと機密境界の混乱を防ぐ
- 人間・エージェントそれぞれに役割（データ分析担当、デザイン基準の維持担当、リサーチ統合担当など）と必要なツールアクセス（BigQuery、Playwright MCPなど）を明示的に割り当てる
- 役割を持つエージェントが必要に応じて別のエージェントを起動し、適切なメモリ・権限を持つエージェントにタスクを委譲できるようにして、個人利用AIの乱立と作業重複・文脈の分断を防ぐ

## 使いどころ

- 複数人のチームが同じSlackワークスペース上でエージェントと共に戦略立案から実行までを共同で進めたい場合
- データ分析・QA・リサーチ統合など役割の異なる複数エージェントをプロジェクト単位で並行運用したい組織
- メトリクス集計やレポーティングなど、個々人が別々のAIに同じ作業をさせて数値がずれる状態を解消し、チーム全体で単一の結果を参照させたい場合
- 会議メモや仕様書など社内ドキュメントの公開範囲を整理し、エージェントと人間の双方に一貫した文脈を与えたい場合
