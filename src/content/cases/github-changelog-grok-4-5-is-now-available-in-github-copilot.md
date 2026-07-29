---
type: announcement
title: xAIのGrok 4.5をGitHub Copilotのモデル選択肢に追加
title_original: Grok 4.5 is now available in GitHub Copilot
company: GitHub
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
- ai-agent
components:
- GitHub Copilot
- Grok 4.5
- Visual Studio Code
- GitHub Copilot CLI
- GitHub Copilot cloud agent
- GitHub Copilot app
outcome:
  type: speed
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-07-28-grok-4-5-is-now-available-in-github-copilot
published_at: '2026-07-28'
---

## 概要

xAIの最新推論モデルGrok 4.5がGitHub Copilotで順次利用可能になった。最大50万トークンのコンテキストウィンドウ、テキスト・画像入力、3段階の推論強度に対応し、ターミナルベースのコーディングタスクや並列ツール呼び出しで高い性能を示している。Copilot Pro/Business/Enterprise等の各SKUで、VS CodeやCopilot CLIなど複数クライアントのモデルピッカーから選択でき、Enterprise/Business管理者はポリシーで有効化を制御する。

## 設計のポイント

- モデルピッカー方式で複数のLLMをユーザーがタスクに応じて切り替えられるようにする。
- 推論強度(low/medium/high)を選択可能にし、タスクの複雑さとレイテンシ・コストのトレードオフを調整できるようにする。
- Enterprise/Business管理者がポリシーで新モデルの有効化を制御し、既定オフでガバナンスを効かせる。

## 使いどころ

- 探索的なコーディングタスクやブロッカー解消など、並列ツール実行が有効な場面。
- 大規模なコードベースを扱う際に50万トークンの広いコンテキストが必要な場面。
- 画像入力を伴うマルチモーダルなコーディング支援が必要な場面。
