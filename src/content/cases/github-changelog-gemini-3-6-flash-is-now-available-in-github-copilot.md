---
type: announcement
title: GitHub CopilotにGoogleのGemini 3.6 Flashが追加
title_original: Gemini 3.6 Flash is now available in GitHub Copilot
company: GitHub
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
components:
- GitHub Copilot
- Gemini 3.6 Flash
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-07-21-gemini-3-6-flash-is-now-available-in-github-copilot
published_at: '2026-07-21'
---

## 概要

GitHub Copilotのモデル選択肢に、Web/アプリ開発や長時間のエージェントタスク向けに調整されたGoogleのGemini 3.6 Flashが追加された。推論の強度を調整可能で並列ツール呼び出しにも対応し、前世代のGemini 3.5 Flashよりタスク完了率とトークン効率が向上している。

## 設計のポイント

- VS Code・Visual Studio・Copilot CLI・JetBrainsなど複数クライアントのモデルピッカーから同一モデルを選択できるようにする。
- Enterprise/Businessプランでは管理者がポリシーで有効化するまで組織内で使用不可にし、モデル導入をガバナンス配下に置く。

## 使いどころ

- コーディングと長時間稼働のエージェントタスクでモデルごとのコスト・性能トレードオフを選びたい開発チーム。
