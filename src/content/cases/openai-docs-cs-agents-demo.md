---
type: guidance
title: OpenAI Agents SDKによるカスタマーサービス・マルチエージェントデモ
title_original: Customer Service Agents Demo
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- guardrails
components:
- OpenAI Agents SDK
- ChatKit
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://github.com/openai/openai-cs-agents-demo
published_at: '2025-07-21'
---

## 概要

OpenAI Agents SDK上に構築されたカスタマーサービスエージェントのデモリポジトリ。Triage Agentが問い合わせをFlight Information・Booking & Cancellation・Seat & Special Services・FAQ・Refunds and Compensationなど専門エージェントにルーティングするマルチエージェント構成を示し、関連性ガードレールとジェイルブレイクガードレールで会話の逸脱・脱獄を防ぐ。

## 設計のポイント

- Triage Agentを単一のエントリポイントとし、意図に応じて専門エージェントへhandoffするパターンを採用する
- 会話が航空関連トピックから逸脱した場合や指示抽出を試みた場合にガードレールを発火させ安全に応答を制限する
- 便の遅延・欠航などのイレギュラー運用時は複数エージェント(Flight Information→Booking)を連鎖させて自動リブッキングまで完結させる

## 使いどころ

- 複数の専門領域にまたがる問い合わせをルーティングするカスタマーサポートAIの設計
- ガードレールによる話題逸脱・プロンプトインジェクション対策を学びたい開発者
- 実運用前にマルチエージェントオーケストレーションのリファレンス実装を試したいチーム
