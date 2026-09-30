---
type: guidance
title: NeMo RelayによるHermes Agentの実行トレース取得とハーネス改善評価
title_original: Tracing Agent Harness Behavior with NVIDIA NeMo Relay
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llmops
- eval
components:
- NVIDIA NeMo Relay
- Hermes Agent
- Arize Phoenix
- OpenTelemetry
- OpenInference
- NVIDIA Nemotron 3.5 Lightning
- Docker
- Qwen Coder 30B
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/tracing-agent-harness-behavior-with-nvidia-nemo-relay/
published_at: '2026-09-29'
---

## 概要

NVIDIA NeMo Relayはエージェント実行のライフサイクルイベントを記録する共通の可観測性レイヤーで、Hermes Agentにネイティブ統合されている。ATOF（イベントストリーム）、ATIF（ステップ単位の軌跡）、OpenInferenceラベル付きOpenTelemetryスパンを出力し、Arize Phoenixでモデル・ツール呼び出し、エラー、トークン使用量を確認できる。タスク検証結果とトレース証拠を組み合わせ、108回の実行でハーネス変更の効果を比較するHermes ToolPerfの事例も示している。

## 設計のポイント

- 成功判定だけでなく、モデル/ツール呼び出し・リトライ・所要時間・トークン量のトレースを併せて見ることで、非効率な経路を検出する。
- 用途に応じて、監査・デバッグ向けのATOF、ステップ評価向けのATIF、OTEL互換ツール向けのOpenTelemetryスパンという3形式を使い分ける。
- ツール実行はネットワークやAPIキーにアクセスできない隔離Dockerコンテナで行い、出力を固定値で検証できるタスクでセットアップを確認する。
- ハーネス変更はベースラインと修正版を繰り返し実行して比較し、タスク回復率と呼び出し数・レイテンシのトレードオフを評価する。

## 使いどころ

- エージェントハーネスの変更が実際にタスク成果を改善したかを定量評価したい開発者。
- エージェントの挙動をセキュリティやガバナンスの観点から監査・調査したい企業。
- Phoenixなど既存のOTEL互換ツールでエージェントの観測を行いたいチーム。
