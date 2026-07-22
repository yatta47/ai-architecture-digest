---
type: guidance
title: AIエージェントのためのゼロトラストセキュリティフレームワーク（3段階成熟度モデル）
title_original: Zero Trust for AI agents
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- guardrails
- ai-agent
- defense-in-depth
components: []
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/zero-trust-for-ai-agents
published_at: '2026-05-27'
---

## 概要

自律的なAIエージェントをエンタープライズに展開する際のゼロトラストセキュリティフレームワークを紹介する記事。プロンプトインジェクションやツール汚染、メモリ汚染などエージェント特有の脅威に対し、Foundation/Advanced/Optimizedの3段階成熟度モデルと8フェーズの実装ワークフロー、AI加速攻撃に対応するアジェンティックSOAR運用を提示する。

## 設計のポイント

- 暗号学的に根付いたID・タスク単位でスコープされた権限・メモリ汚染対策など、ゼロトラストの原則をエージェント特有の脅威モデルに合わせて再設計する
- 組織の成熟度とリスク許容度に応じてFoundation→Advanced→Optimizedの3段階でゼロトラスト態勢を段階的に強化する
- ID・アクセススコープ・サンドボックス化・入出力制御・メモリ保護を含む8フェーズの実装ワークフローで導入を進める
- AI加速型攻撃に対抗するため、防御側の運用（Agentic SOAR）も自律攻撃者と同等の速度で回せる体制にする

## 使いどころ

- 自律的なAIエージェントを本番導入する前に、権限スコープやサンドボックス化などのセキュリティ設計を体系的に整理したいセキュリティ・リスク部門
- 医療・金融・政府など規制業界でAIエージェント導入時のコンプライアンス整合を確認したい組織
