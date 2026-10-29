---
type: announcement
title: 'GitHub Copilot in VS Code: クラウドエージェントとセッション継続'
title_original: GitHub Copilot in VS Code Universe releases
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- parallel-execution
components:
- GitHub Copilot
- Visual Studio Code
- Copilot CLI
- GitHub Mobile
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-28-github-copilot-in-vs-code-universe-releases
published_at: '2026-10-28'
---

## 概要

GitHub CopilotはVS Codeで、クラウドエージェントのセッションを携帯、VS Code、github.comなどから引き継げるようにした。Agent Hostによりウィンドウを閉じても処理が続き、モデルやハーネスを並列に比較する機能も加わった。

## 設計のポイント

- セッションをクラウドで実行して複数クライアントから引き継ぎ、端末の電源に依存させない。
- Agent Hostでエージェントをエディタのウィンドウから分離し、バックグラウンドや別マシンで動かす。
- Copilot SDK上の共通ハーネスを標準にし、各クライアントで挙動を揃える。

## 使いどころ

- 席を離れても長時間のコーディングエージェント作業を続けたい開発者。
- 複数モデルの結果を並べて比較したい場面。
