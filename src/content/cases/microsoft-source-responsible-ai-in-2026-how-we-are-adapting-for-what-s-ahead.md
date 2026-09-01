---
type: announcement
title: エージェント型AI時代に向けたMicrosoftの責任あるAIガバナンス刷新
title_original: 'Responsible AI in 2026: How we are adapting for what''s ahead'
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- guardrails
- eval
- policy-as-code
components:
- AI Red Teaming Agent
- RAMPART
- ASSERT
- Agent Control Specification
- Microsoft 365 Copilot
- Microsoft Foundry
- GitHub Copilot
outcome:
  type: risk-compliance
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://blogs.microsoft.com/on-the-issues/2026/09/01/responsible-ai-in-2026-how-we-are-adapting-for-whats-ahead/
published_at: '2026-09-01'
---

## 概要

Microsoftは2026年版Responsible AI Transparency Reportを公開し、モデル単体でなくエージェント・ツール・データ・人との相互作用まで含めたリスク管理へガバナンスを拡張したと説明する。AI Red Teaming AgentやRAMPART、ASSERT、Agent Control Specificationといった実務ツールで、事前評価だけでなく稼働中のエージェントの挙動監視・介入を可能にしている。

## 設計のポイント

- モデル・プラットフォームサービス・アプリケーションの各層に応じて適用要件を切り替える階層型ポリシー構造にする
- エージェントID・ツール権限・行動監視をエージェント間の相互作用単位でガバナンス対象にする
- レッドチーム結果をRAMPARTで再現可能なテストに変換し継続的な評価ループにする
- デプロイ前評価だけでなく稼働中の挙動を監視・制御するランタイムコントロールを併用する

## 使いどころ

- 多数のエージェントやツールを本番運用する組織のAIガバナンス設計
- ISO 42001等の認証取得に向けて責任あるAIプロセスを標準化したい企業
- プロンプトインジェクションやエージェント脅威モデリングの社内教育を整備したいセキュリティ部門
