---
type: case
title: Claude CodeとClaude Agent SDKで会社そのものを構築した3つのYCスタートアップ
title_original: How three YC startups built their companies with Claude Code
company: HumanLayer / Ambral / Vulcan Technologies
industry: cross-industry
cloud: []
patterns:
- human-in-the-loop
- multi-agent-orchestration
- context-engineering
- ai-agent
components:
- Claude Code
- Claude Agent SDK
- Opus
- Sonnet
- Slack
outcome:
  type: speed
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/building-companies-with-claude-code
published_at: '2025-11-17'
---

## 概要

Y Combinator出身の3社（HumanLayer、Ambral、Vulcan Technologies）が、Claude CodeとClaude Agent SDKを軸に自社プロダクトと開発体制そのものを構築した事例。リスクのある操作への人間承認組み込み、サブエージェントによる業務自動化、並列実行基盤の整備など、それぞれ異なる切り口でAIネイティブな開発・運用パターンを確立し、非技術系創業者やソロエンジニアでも数週間かかる開発を数時間に圧縮できることを示した。

## 設計のポイント

- データベース操作など不可逆でリスクの高い処理には、SlackやEmail経由の人間承認ステップを組み込み、エージェントの自律実行と安全性を両立させた（human-in-the-loop）。
- Claude Agent SDKを使い、Opusを『思考・計画』、Sonnetを『実装』に使い分けるサブエージェント構成で、精度とコストのバランスを取った。
- Gitのworktreeとリモートクラウドワーカーを活用し、複数のClaude Codeセッションを並列実行できる社内基盤（CodeLayer）を構築した。
- 自社の実践知を『12-Factor Agents』として文書化・公開し、コンテキストエンジニアリングのベストプラクティスを業界と共有することで採用を加速した。

## 使いどころ

- 非技術系の創業者やソロエンジニアが少人数でプロダクトを立ち上げ、複雑な規制対応（政府調達など）まで一気に進めたい場合。
- AIエージェントに機微な操作を任せる際、承認フローを組み込んで安全に自律実行させたいチーム。
- アカウントマネジメントなど属人化しやすい業務をAIエージェントで代替・拡張したいB2B SaaS企業。
- 組織全体でAI駆動開発を展開する際に、コラボレーションやツール運用を再設計する必要があるエンジニアリング組織。
