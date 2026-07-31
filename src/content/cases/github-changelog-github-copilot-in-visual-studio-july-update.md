---
type: announcement
title: Visual StudioのGitHub CopilotがCopilot SDKベースの新エージェントを搭載
title_original: GitHub Copilot in Visual Studio — July update
industry: cross-industry
cloud: []
patterns:
- ai-agent
components:
- GitHub Copilot
- GitHub Copilot SDK
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-07-30-github-copilot-in-visual-studio-july-update
published_at: '2026-07-30'
---

## 概要

Visual Studio 2026のGitHub Copilotに、CLI版と同じCopilot SDKを基盤とする新エージェント（プレビュー）が追加された。あわせて.NET/Azureチーム製の組み込みスキル、選択コードのレビュー機能、組織単位のカスタム指示が導入された。

## 設計のポイント

- IDE版エージェントとCLI版エージェントを同一のCopilot SDK上に統一し挙動の一貫性を保つ
- 組織カスタム指示を個々の開発者ではなく組織レベルで一元設定できるようにする
- 専門チーム（.NET/Azure）が作った組み込みスキルをデフォルトオフにして必要な人だけ有効化させる

## 使いどころ

- .NETやAzure関連の定型タスクをエージェントに任せたい開発チーム
- 組織全体でCopilotの応答方針を統一したい大規模開発組織
- コードレビューの前段階で特定ブロックだけ素早く第二の意見を得たい開発者
