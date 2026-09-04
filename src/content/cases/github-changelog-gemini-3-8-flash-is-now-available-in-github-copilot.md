---
type: announcement
title: GitHub CopilotへのGemini 3.8 Flash追加
title_original: Gemini 3.8 Flash is now available in GitHub Copilot
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
components:
- GitHub Copilot
- Gemini 3.8 Flash
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-03-gemini-3-8-flash-is-now-available-in-github-copilot
published_at: '2026-09-03'
---

## 概要

GoogleのGemini 3.8 FlashがGitHub Copilotの各種インターフェース(VS Code、Copilot CLI、クラウドエージェント等)で利用可能になり、複雑なターミナルベースのコーディングタスクで高い検証・失敗回復性能を示したことを紹介する。導入は段階的で、2026年12月31日まで導入時価格の従量課金となる。

## 設計のポイント

- 新モデルはデフォルトで自動有効化されるが、管理者はモデルポリシーでグローバルデフォルトやモデル単位の有効/無効を制御できる
- 段階的ロールアウトのため利用可能になるタイミングは組織・ユーザーによって異なる

## 使いどころ

- 複数のIDE/CLIにまたがってCopilotのモデル選択を統一管理したいCopilot Enterprise/Business管理者
- 複雑なターミナルベースのコーディングタスクで新しいモデルの性能を試したい開発者
