---
type: guidance
title: 規制産業向けAI駆動コードモダナイゼーションの事前準備ガイド
title_original: How to prepare for AI-driven code modernization projects
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- parallel-execution
- human-in-the-loop
components:
- Claude Code
- Code modernization plugin
outcome:
  type: speed
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-to-prepare-for-ai-driven-code-modernization-projects
published_at: '2026-09-23'
---

## 概要

Anthropicの forward deployed engineer が、重要システムや規制企業でエージェント駆動のコード移行を進める前に必要な組織的準備を6ステップで整理したガイド。エージェントで変更の生成が速くなると、ボトルネックは変更の作成から、変更管理・レビュー・承認への組織対応に移る。

## 設計のポイント

- 移行の種類（Uplift / Transform / Reimagine）を先に決め、ゴールとなるターゲットと振る舞い仕様を明文化して「正しさ」の争いを後に持ち越さない。
- 変更が満たすべき条件を「証明書（certificate）」として定義し、変更ごとに証拠を付けて審査を機械的に通せるようにする。
- 認定済みの変更が生成速度に見合う速さで本番へ届くよう、昇格ポリシー・CI/CD・レビュー容量・承認を事前に整備する。
- ターゲット・証明書・昇格ポリシーを軸に、Claude Codeの動的ワークフローで多数の並列サブエージェントに分割し、小さなパーティションで実証してから拡大する。

## 使いどころ

- 銀行など変更管理が厳格な組織で、レガシー（COBOL→Javaなど）の移行を数か月規模で進めたいとき。
- 移行の目的をリスク低減で説明し、経営層や依存チームの合意形成を進めたいとき。
- エージェント生成の大量の差分に対し、レビューと承認の体制を設計したい移行PMやアーキテクト。
