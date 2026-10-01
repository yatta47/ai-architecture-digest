---
type: announcement
title: VS CodeとCopilotアプリで使えるマルチモデル協調HydraFusion
title_original: HydraFusion in VS Code and the GitHub Copilot app
company: GitHub
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
- multi-agent-orchestration
- ai-agent
components:
- GitHub Copilot
- HydraFusion
- Visual Studio Code
- GitHub Copilot CLI
outcome:
  type: quality
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-30-hydrafusion-in-vs-code-and-the-github-copilot-app
published_at: '2026-09-30'
---

## 概要

研究プレビューのHydraFusionが、Copilot CLIに加えてVS CodeとGitHub Copilotアプリでも利用可能になった。単一モデルではなく複数モデルを協調させ、タスクに応じてSingle、Cascade、Critiqueのいずれかのワークフローを選ぶ。進捗の透明性や更新頻度も改善された。

## 設計のポイント

- 推論・コード生成・デバッグ・ツール利用の能力シグナルから、品質基準を満たす最も効率的な実行パターンを選ぶ。
- Cascadeでは効率的なモデルが下書きし、品質ゲートで合格か上位モデルへのエスカレーションかを判定する。
- Critiqueでは別モデルファミリーの読み取り専用批評者がレビューし、下書きモデルが一度だけ修正する。
- Autoはリクエスト単位のモデル選択、HydraFusionはワークフロー選択とターン内の複数モデル協調という違いがある。

## 使いどころ

- コストと品質のバランスを取りつつコーディング支援を使いたい開発者。
- 複数モデルを組み合わせるオーケストレーション設計の参考にしたいチーム。
