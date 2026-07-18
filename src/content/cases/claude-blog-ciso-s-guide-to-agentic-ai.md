---
type: guidance
title: エージェント型AIの社内リスクを4つの質問で評価するCISO向けフレームワーク
title_original: 'Zero risk isn''t the job: a CISO''s guide to agentic AI'
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- guardrails
- defense-in-depth
components:
- Claude
- Claude Tag
- Claude Cowork
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/ciso-guide-to-agentic-ai
published_at: '2026-07-17'
---

## 概要

Anthropicの副CISOが、社内でエージェント型AIを安全に導入・拡大するために使っているリスク評価フレームワークを解説する記事。「非信頼コンテンツを読むか」「どんな操作を誰の代理で行うか」「誤動作時の被害範囲」「観測可能性」の4つの質問でリスクを可視化し、最小権限の原則に基づいて段階的にアクセスを拡大する運用を紹介している。

## 設計のポイント

- エージェントのリスクを『非信頼コンテンツの摂取有無』『実行可能な操作と代理者』『誤動作時の被害範囲』『観測可能性』の4つの質問で評価する
- 最小権限の原則（least agency）に基づき、タスク遂行に必要な最小限の権限のみを付与する
- エージェントの身元を『単一目的で人間に紐付かないシステムサービスアカウント』と『人間の認証情報』のどちらに寄せるか明確にし、責任の所在が曖昧になる中間領域を避ける
- 小規模グループへの限定公開から始めテレメトリを観察しながら段階的に権限を拡大する『admin-paced rollout』を採用する

## 使いどころ

- 業務システムに接続するエージェント型AIの導入可否をセキュリティ部門が審査するとき
- プロンプトインジェクションやデータ漏洩などエージェント固有のリスクを、既存のインサイダーリスク管理の枠組みで捉え直したい組織
- 複数の部署でエージェントの野良導入（シャドーAI）が進み、ガバナンスを後追いで整備する必要がある企業
