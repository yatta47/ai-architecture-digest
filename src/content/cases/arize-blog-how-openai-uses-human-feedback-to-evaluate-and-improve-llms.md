---
type: announcement
title: 音声エージェントの全パイプラインを追跡できるLangSmithのトレーシング
title_original: Trace voice agents in LangSmith
company: LangChain
industry: cross-industry
cloud: []
patterns:
- voice-agent
- eval
- llmops
components:
- LangSmith
- Pipecat
- LiveKit
- OpenAI Realtime
- Gemini Live
- Google ADK
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/how-openai-turns-user-feedback-into-product-improvements/
published_at: '2026-07-21'
---

## 概要

LangChainは、Pipecat・LiveKit・OpenAI Realtime・Gemini Live(Google ADK)向けのPythonトレーシング統合をLangSmithに追加した。「サンドイッチ型」(STT→テキストエージェント→TTS)と音声-音声直結型の両アーキテクチャに対応し、会話音声・各推論ステップのレイテンシ・割り込み検出・ツール呼び出しを単一のトレースツリーで可視化する。

## 設計のポイント

- サンドイッチ型ではSTT/LLM/TTSそれぞれのレイテンシ内訳を分解して表示し、ターン遅延のボトルネックを特定できるようにする。
- 音声-音声型では双方向WebSocket上でやり取りされるイベント(音声・ツール呼び出し・割り込み検出等)をそのまま記録し、実際の挙動を再構成できるようにする。
- テキストエージェントと音声エージェントを同じトレース基盤・レビューワークフローに統合し、別々のツールを使い分けなくて済むようにする。

## 使いどころ

- 音声エージェントを本番運用しており、ターン遅延や割り込みの原因を特定したいチーム。
- 音声・テキスト両方のエージェントを横断してデバッグ・評価・改善サイクルを回したい組織。
