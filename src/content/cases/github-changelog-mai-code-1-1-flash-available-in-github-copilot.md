---
type: announcement
title: 画像理解対応・低価格化した新コーディングモデルのCopilot展開
title_original: MAI-Code-1.1-Flash available in GitHub Copilot
company: GitHub
industry: cross-industry
cloud: []
patterns:
- inference-optimization
- multi-model-routing
components:
- MAI-Code-1.1-Flash
- GitHub Copilot
outcome:
  type: cost
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-11-mai-code-1-1-flash-available-in-github-copilot
published_at: '2026-08-11'
---

## 概要

Microsoftの小型コーディングモデルMAI-Code-1.1-FlashがGitHub Copilotに展開された。ネイティブな画像理解対応やコーディング品質・ツール利用の改善に加え、モデル/サービング効率の向上で旧モデル比73%の価格低下を実現し、無料/学生向けは自動選択、有料プランは手動選択も可能になった。

## 設計のポイント

- 画像理解のネイティブ対応など機能向上と同時に、モデル・サービング効率の改善で旧モデル比73%の価格低下を実現した。
- 無料/学生向けには自動モデル選択で提供し、有料プランでは手動選択も可能にするなど利用者層でロールアウト方法を分けた。
- Enterprise/Business管理者がポリシーを明示的に有効化しない限りデフォルトでオフにする設計で、組織側の統制を保った。

## 使いどころ

- 軽量なコーディング作業でコストと性能のバランスを取りたい個人・小規模チーム。
- 複数のIDE・CLI・クラウドエージェントにまたがって同じモデルを使いたい開発者。
- モデルの導入可否を組織ポリシーとして管理したいCopilot Enterprise管理者。
