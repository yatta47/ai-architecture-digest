---
type: case
title: Claude TagがAnthropic社内のCI/CD障害対応ファーストレスポンダーになる仕組み
title_original: 'Claude on call: How Claude Tag serves as Anthropic''s first responder for CI/CD failures'
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- root-cause-analysis
- ci-cd
components:
- Claude Tag
- Claude Code Remote
- Slack
- Datadog
- Grafana
- PagerDuty
- GitHub
- Kubernetes
- MCP Connectors
outcome:
  type: speed
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/ai-ci-cd-on-call
published_at: '2026-08-18'
---

## 概要

Anthropicは自社のCI/CDインシデント対応にClaude Tagを組み込み、Slackのオンコールチャンネルでの記憶・権限・スケジュール・指示（Markdownスキル）を土台に、検知からトリアージ、SITREP作成までを担う一次対応エージェントを構築した。オーケストレータエージェントが依存先ごとの調査を並列の実行サブエージェントに割り振り、平均14分で根拠付きの初期分析を投稿できるようになった。

## 設計のポイント

- 標準指示やルーティングポリシー、過去の教訓をGitHub管理のMarkdownスキルとして版管理し、複数人で継続的に改善できるようにする
- アラート検知は決定論的なルールで行い、エスカレーション判断はエージェントに委ねる決定論とエージェント判断のハイブリッド設計にする
- オーケストレータが複数の実行サブエージェントに調査を並列分散させ、Grafana・ログ・PagerDuty・GitHubなど複数ソースを横断させる

## 使いどころ

- 24時間365日のオンコール負荷を減らしたいSRE・インフラチーム
- アラート疲れが問題になっている大規模サービスの障害検知プロセスを見直したい組織
- インシデント対応の一次調査・状況報告作成を自動化し人間はレビューと意思決定に集中したい場合
