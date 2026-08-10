---
type: announcement
title: Claude Code、分類器ベースの『Auto mode』を安全性データとともにデフォルト化
title_original: Auto mode is now the default in Claude Code for Pro, Max, and Team plans
company: Anthropic
industry: cross-industry
cloud:
- multi-cloud
patterns:
- guardrails
- human-in-the-loop
- ai-agent
components:
- Claude Code
- Claude Opus 5
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/auto-mode-default-in-claude-code
published_at: '2026-08-07'
---

## 概要

Claude CodeはPro/Max/Teamプラン向けに8月14日から「Auto mode」をデフォルトにする。Auto modeは全ツール呼び出しを分類器に通し、破壊的・不可逆・環境外に影響する操作をブロックする仕組みで、許可プロンプトへの人手承認より高い安全性を確認したうえでの切り替えとなる。1,053人の有償テスターによる対照実験では、危険なコマンドを人間は13.6%しか検知できなかったのに対しAuto modeは89%を検知した。

## 設計のポイント

- 許可プロンプトの都度承認ではなく、ツール呼び出しごとに分類器を通し、不可逆・破壊的・環境外向けの操作のみをブロックする設計にすることで長時間の自律実行を阻害しない
- 分類器が3回連続、またはセッション中に20回ブロックした場合は手動承認モードにフォールバックし、進捗が止まらないようにする
- python:*のような任意コード実行を許可する既存の許可ルールは分類器を丸ごとバイパスしてしまうため、Auto mode中は一時的に無効化する
- セッションが長くなるほど人間の承認精度は低下する（初期17%→50プロンプト以降5%）のに対し、分類器の検知率はセッション長に関わらず一定を保つ

## 使いどころ

- 数時間にわたる自律的なコーディングタスクを一晩中実行させたいチーム（夜間の調査・改善エージェントなど）
- 許可プロンプトへの『とりあえず承認』が形骸化し、危険な操作の見落としリスクが高まっているチーム
- 本番インフラに直接触れる作業では手動承認に切り替えるなど、リスクに応じてモードを使い分けたい運用
