---
type: case
title: インバウンド営業を置き換えるClaude購入支援エージェント
title_original: How Anthropic's sales team rebuilt inbound with Claude Managed Agents
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
- prompt-optimization
components:
- Claude Managed Agents
- Claude
- Claude Code
- Claude.ai
outcome:
  type: revenue
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-anthropics-sales-team-rebuilt-inbound-with-claude-managed-agents
published_at: '2026-09-30'
---

## 概要

Anthropicの営業チームは、問い合わせフォームへの返信に数日かかっていたインバウンド対応を、Claude Managed Agents上の購入支援エージェントに置き換えた。エージェントは料金・セキュリティ・データに関する質問に答えてプランと席数を提案し、購入・担当者への引き継ぎ・即答のいずれかで会話を終える。1日数千件の会話を処理し、引き継がれたリードは旧フォーム経由の2倍以上の割合で商談化し、約5日早くクローズしている。

## 設計のポイント

- プロンプト・少数のツール・ナレッジベースに注力し、エージェントループやセッション管理、ホスティングはマネージド基盤に任せる。
- 詳細なルールの列挙ではなく目的を与える簡潔なプロンプトにし、必要な知識と文脈を渡す。
- エージェントのバージョン管理とステージング環境で、営業担当など非エンジニアもプロンプトを直接編集・検証できるようにする。
- 担当者へのエスカレーション時に理由を記録させてフィードバックとして活用し、人手が必要な会話の割合を約半減させた。

## 使いどころ

- 月数万件規模のインバウンド問い合わせに担当者が追いつかないB2B営業組織。
- 料金・プラン・コンプライアンスなど文書化済みの質問に24時間多言語で即答したいセルフサービス型販売。
- 大型・複雑な案件だけを会話履歴付きで営業担当に引き継ぎたいチーム。
