---
type: announcement
title: GitHub CopilotでGAモデルをデフォルト自動有効化するガバナンスポリシー
title_original: Default model enablement for Copilot Business and Enterprise
company: GitHub
industry: cross-industry
cloud: []
patterns:
- llmops
- policy-as-code
components:
- GitHub Copilot
- DeepSeek
- Kimi K2.7
- Fable 5
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-07-29-default-model-enablement-for-copilot-business-and-enterprise
published_at: '2026-07-29'
---

## 概要

GitHub CopilotのBusinessおよびEnterpriseプランに、一般提供(GA)されたモデルをデフォルトで有効化するグローバルポリシーが導入される。管理者が新モデルごとに個別に有効化する手間を省きつつ、より厳格なガバナンスが必要な組織向けには単一のオプトアウト制御を用意する。DeepSeekやKimi K2.7などのオープンウェイトモデルや、データ保持契約対象外のFable 5はデフォルト有効化の対象から除外される。

## 設計のポイント

- 「未設定」状態のモデルを「デフォルト継承」という動的状態として扱い、組織ポリシーの変更が既存の未設定モデルへ即座に反映される設計にする。
- 管理者が明示的に有効/無効を設定したモデルは、デフォルトポリシーの変更によって上書きされないようにする。
- データ保持契約の対象外モデルやオープンウェイトモデルなど、ガバナンス上のリスクがあるモデル群はデフォルト有効化の対象から明示的に除外する。
- ポリシー適用までに28日間の周知期間を設け、既存ユーザーの挙動を変えずに設定を見直す猶予を与える。

## 使いどころ

- 新しいAIモデルが次々とGAになる中、逐一手動で有効化する運用負荷を減らしたいCopilot管理者。
- モデル利用に厳格なガバナンス・承認フローを課したいセキュリティ/コンプライアンス部門。
- 数百〜数千ユーザー規模でCopilotを展開する企業のIT管理者。
