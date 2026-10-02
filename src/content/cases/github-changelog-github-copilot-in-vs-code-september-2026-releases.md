---
type: announcement
title: 'VS CodeのCopilot 9月リリース: エージェント駆動開発の強化'
title_original: GitHub Copilot in VS Code, September 2026 releases
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-model-routing
- human-in-the-loop
components:
- GitHub Copilot
- VS Code
- HydraFusion
- Dev Containers
- Codex
- Claude
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-01-github-copilot-in-vs-code-september-2026-releases
published_at: '2026-10-01'
---

## 概要

VS Code v1.136〜v1.140（2026年9月）のCopilotは、実装からPRマージまでのエージェント駆動開発を強化した。スケジュール実行のautomations、レビュー指摘や失敗チェックに対応するagent merge、HydraFusionによるモデル自動選択などが追加された。

## 設計のポイント

- HydraFusionがタスクに応じてモデルとワークフローを自動選択し、モデル選択の負担を減らす。
- automationsで定期タスクを時間・日・週単位または手動で実行し、反復作業をエージェントに任せる。
- agent mergeでレビュー対応、失敗チェック、コンフリクト解消、ワークフロー再実行を自動化する。
- Dev Containerセッションにより、プロジェクト既定のツールと依存関係でエージェントを動かせる。

## 使いどころ

- PRのレビュー対応やCI失敗対応など、マージまでの定型作業を減らしたいチームに効く。
- Copilot、Claude、Codexなど複数エージェントのセッションを一つのウィンドウで管理したい開発者に向く。
