---
type: case
title: Wiz・Palo Alto・AccentureらがClaude Opusで実現する攻撃的検証と脆弱性修復の高速化
title_original: How our partners are putting Opus to work for cybersecurity
industry: cross-industry
cloud: []
patterns:
- ai-agent
- guardrails
components:
- Claude Opus
- Wiz Security Graph
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-our-partners-are-putting-opus-to-work-for-cybersecurity
published_at: '2026-05-21'
---

## 概要

Wiz、Palo Alto Networks、Accenture、CrowdStrike、TrendAI、Deloitte、PwCなどのパートナーがClaude Opusを使い、攻撃的セキュリティテストの高速化・脆弱性の発見から修復までのギャップ短縮・ガバナンスされたAI導入を実現している事例集。Wizは週15万以上の本番資産への継続的ペネトレーションテストで誤検知ゼロの重大指摘を多数検出し、Accentureは自社インフラのセキュリティテストカバレッジを10%から80%以上に、スキャン所要時間を3〜5日から1時間未満に短縮した。

## 設計のポイント

- 攻撃者視点でアプリケーションロジックを解析し、実運用のレスポンスに適応しながら攻撃パスを連鎖させるAIエージェントを本番環境に継続的に走らせ、従来のスキャナーが見逃すロジック起因の欠陥を拾う
- 発見した脆弱性にエクスプロイト可能性の証跡とビジネスコンテキストを付与し、検出から修復までの意思決定レイテンシを短縮する
- 資産・ID・脅威・コントロールを単一の運用モデルに統合し、検知・優先順位付け・修復を継続的なループとしてAIに推論させる
- パイロット止まりになりがちなAI導入を、ガバナンスと監査証跡を整備した上で数週間で本番移行できるようにする

## 使いどころ

- 従来型スキャナーではカバーしきれないロジック起因の脆弱性を、本番規模で継続的に検出したいセキュリティチーム
- 脆弱性の発見から修復までのリードタイムを短縮し、パッチが存在しない場合の緩和策設計まで含めて自動化したい組織
