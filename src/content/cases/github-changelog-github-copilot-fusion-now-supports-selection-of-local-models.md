---
type: announcement
title: ローカルモデルとクラウドモデルを自動で振り分けるCopilot Fusion
title_original: GitHub Copilot Fusion now supports selection of local models
company: GitHub
industry: cross-industry
cloud:
- azure
patterns:
- multi-model-routing
- inference-optimization
components:
- GitHub Copilot Fusion
- Windows ML
- MAI Code 1.1 Flash
- Qwen3.8 Flash Next
- Copilot CLI
outcome:
  type: cost
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-28-github-copilot-fusion-now-supports-selection-of-local-models
published_at: '2026-10-28'
---

## 概要

Copilot Fusionがオンデバイスのローカルモデルとクラウドモデルの振り分けに対応した実験的プレビューが始まった。WindowsではWindows ML経由で管理ダウンロードでき、OpenAI互換サーバーで自前モデルも利用できる。

## 設計のポイント

- ルーティング判断は引き続きクラウドで行い、推論だけをローカルに寄せる構成である。
- BYOKで追加したモデルは自動ではFusionの対象にならず、明示的な設定が要る。
- ローカルモデルは安全保護がクラウドモデルと異なる可能性がある。

## 使いどころ

- デバイスの計算資源を使って推論コストを下げたい開発者。
- 手動でモデルを切り替えずローカルとクラウドを使い分けたい場面。
