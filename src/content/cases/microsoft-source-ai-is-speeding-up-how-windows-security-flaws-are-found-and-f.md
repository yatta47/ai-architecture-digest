---
type: announcement
title: AIを使ったWindowsの脆弱性発見から展開までの高速化方針
title_original: A new standard for vulnerability management in the AI era
company: Microsoft
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
components:
- MDASH
- Microsoft Security Response Center
- Windows
outcome:
  type: risk-compliance
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://blogs.windows.com/windowsexperience/2026/11/05/a-new-standard-for-vulnerability-management-in-the-ai-era/
published_at: '2026-11-05'
---

## 概要

MicrosoftがAIによる脆弱性発見の加速を踏まえ、発見、修正、検証、展開の各段階にAIを適用する方針を示した記事。複数モデルとエージェントによるコードスキャナーMDASHなどを使いつつ、最終判断は技術者が負う。

## 設計のポイント

- マルチモデル・専門エージェントのスキャナーで脆弱性を発見し、誤検知を絞り込む。
- 影響範囲の判定、類似コードの探索、バックポート戦略、テスト作成をAIで支援する。
- 発見から修正まで人間のレビューと責任を残す方針を明示している。

## 使いどころ

- 脆弱性対応の件数増加に開発体制が追いつかない製品組織。
- AI活用と人の責任分界を設計したいセキュリティ部門。
