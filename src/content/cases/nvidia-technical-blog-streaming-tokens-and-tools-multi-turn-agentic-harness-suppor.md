---
type: case
title: NVIDIA Dynamoのエージェントハーネス対応強化でTTFTを5分の1に短縮
title_original: 'Streaming Tokens and Tools: Multi-Turn Agentic Harness Support in NVIDIA Dynamo'
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- ai-agent
- inference-optimization
- llmops
- context-engineering
components:
- NVIDIA Dynamo
- NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4
- Claude Code
- Codex
- OpenClaw
- Anthropic Messages API
- NVIDIA B200
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/streaming-tokens-and-tools-multi-turn-agentic-harness-support-in-nvidia-dynamo/
published_at: '2026-06-11'
---

## 概要

NVIDIA Dynamoは、Claude CodeやCodexなど実際のエージェントハーネスを自社推論サーバーで動かす中で見つかった課題に対応し、セッション固有のAnthropic課金ヘッダーを除去する--strip-anthropic-preambleや、ターン単位でreasoningの保持/破棄を制御するパーサー、ツール呼び出しを型付きイベントとして即時ストリーミングする機能を追加した。52Kトークンのプロンプトを使ったB200上の検証では、不安定なヘッダーによりTTFTが168msから912msへ悪化していたのが、ヘッダー除去により169msまで回復し、約5倍のTTFT短縮を達成した。

## 設計のポイント

- セッション固有の可変ヘッダーをトークン化前に除去し、安定したプロンプト先頭をトークン0から揃えることでKVキャッシュ再利用を回復する
- reasoning replayポリシーをモデル/ターンごとに切り替え、ツール呼び出しに付随する推論スパンは保持し、通常の応答ターンでは切り詰めてコンテキストサイズと忠実性のバランスを取る
- 完了したツール呼び出しをターン終了を待たず型付きディスパッチイベントとしてストリーミングし、即時実行とハーネス互換性を両立する
- reasoningパーサーとtool-callパーサーの所有権を推論エンジン側に明示的に持たせ、ハーネスが消費する前に正しくセグメント化されたAPI結果を生成する

## 使いどころ

- Claude CodeやCodexのようなコーディングエージェントハーネスを自前の推論基盤で稼働させたいプラットフォームチーム
- 大きな再利用可能なシステムプロンプトを持つエージェントワークロードでTTFTを改善したい推論基盤運用者
- モデル固有のreasoning/tool-callパーサーの互換性・ストリーミング挙動を標準ハーネスに合わせたい開発者
