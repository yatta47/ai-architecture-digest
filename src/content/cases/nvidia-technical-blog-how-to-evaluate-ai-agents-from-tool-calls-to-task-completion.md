---
type: guidance
title: ツール呼び出しからタスク完遂までAIエージェントを評価する枠組み
title_original: How to Evaluate AI Agents From Tool Calls to Task Completion
industry: cross-industry
cloud: []
patterns:
- eval
- ai-agent
components:
- Nemotron 3.5 Lightning
- PinchBench
- Berkeley Function-Calling Leaderboard
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-to-evaluate-ai-agents-from-tool-calls-to-task-completion/
published_at: '2026-09-21'
---

## 概要

エージェント評価は個々の関数呼び出しの正しさを採点する方式から、実行環境の状態を最後まで追跡してタスク完遂を判定する方式へ移行している。ステップレベルの過程評価とエンドツーエンドの結果評価という2種類のスコアを同じ実行トレース上で組み合わせ、Nemotron 3.5 LightningはPinchBenchで86%の精度と比較対象より30%速いタスク完了を示した。

## 設計のポイント

- ステップレベル評価（各呼び出しが妥当だったか）とエンドツーエンド評価（最終状態が目標と一致したか）を同じトレースの上で分けて計測する
- Benchmark→Trial→Task→Turn→Stepという固定の階層でメトリクスをロールアップしステップを平均してベンチマークスコアとしない
- 成功率は単一の点推定ではなく複数試行の一貫性レンジ（例: 82〜88%）で報告する
- 参照ベースやLLM-as-a-judgeより実行可能な環境状態チェックによる検証を優先する

## 使いどころ

- 本番投入するエージェントモデルを比較検討する意思決定
- 実際のチケットやAPIから作ったドメイン固有評価を環境状態でゲートしたい社内エージェント開発
- ツール呼び出しの精度は高いのにタスク完遂率が低い原因を切り分けたいデバッグ作業
