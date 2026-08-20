---
type: case
title: Maven AGIがAzure上に構築した『解決型』カスタマーサポートAIエージェント
title_original: 'Resolution not deflection: How Maven uses AI agents to transform the enterprise customer journey'
company: Maven AGI
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- eval
- guardrails
components:
- Microsoft Azure
- Azure Language
- Microsoft Teams
outcome:
  type: productivity
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://www.microsoft.com/en-us/startups/blog/resolution-not-deflection-how-maven-uses-ai-agents-to-transform-the-enterprise-customer-journey/
published_at: '2026-08-20'
---

## 概要

Maven AGIは、問い合わせの転送や抑制ではなくエンドツーエンドの解決を目標に据えたAIエージェントを、チャット・音声・メール・SMS横断でMicrosoft Azure上に構築した。Azureでのデータホスティングと暗号化、Azure LanguageによるPII検出、独自の評価フレームワークでエンタープライズが要求する精度とセキュリティを担保しながら、Clio・Mastermind・ClickUp・Thumbtack・Rhoなど顧客企業で自動解決率や応答速度の大幅な改善を実現している。

## 設計のポイント

- チケット抑制ではなく問い合わせの完全解決をゴールに据え、既存のサポート・営業・マーケティングの各システムに直接統合する
- Azure Languageで機微情報を外部AIモデルに送る前に検出・除去し、AES-256の保管時暗号化と組み合わせて企業のセキュリティ要件を満たす
- 応答がブランドや人間対応と同等かを継続的に測る独自の評価フレームワークを開発初期から組み込み、精度を『あれば良い機能』でなく信頼要件として扱う
- Microsoft Teamsと統合し、既存の業務ツール内でチームがワークフローを管理できるようにする

## 使いどころ

- チャネルが分散し問い合わせ対応に複数システムを跨ぐ必要があるエンタープライズのカスタマーサポート部門
- サポート対応がそのまま解約防止やアップセルの機会になる、顧客ライフサイクル全体を扱いたい組織
- 人員を増やさずに問い合わせ量の増加や満足度目標に応えたいカスタマーサクセスチーム
