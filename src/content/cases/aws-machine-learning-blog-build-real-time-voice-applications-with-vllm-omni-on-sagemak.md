---
type: guidance
title: SageMaker AIでのリアルタイム音声合成配信基盤（vLLM-Omni×Qwen3-TTS）
title_original: Build real-time voice applications with vLLM-Omni on SageMaker AI – Part 1
industry: cross-industry
cloud:
- aws
patterns:
- voice-agent
- unified-runtime
- inference-optimization
components:
- Amazon SageMaker AI
- vLLM-Omni
- Qwen3-TTS
- Gradio
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-real-time-voice-applications-with-vllm-omni-on-sagemaker-ai-part-1/
published_at: '2026-09-28'
---

## 概要

AWS vLLM-Omni DLCを使い、Amazon SageMaker AI上でQwen3-TTSモデルを双方向ストリーミング配信する構成を解説する。テキストをストリーム入力し、生成完了前から音声チャンクを再生できるため、音声エージェントなどの低遅延応答が求められる用途に向く。SageMakerのインスタンスプール機能でGPUインスタンスの可用性フォールバックも設計している。

## 設計のポイント

- SageMakerのbidirectional streaming（HTTP/2 WebSocket）でテキスト送信と音声チャンク受信を1つの持続接続に統合する。
- vLLM-Omniのheterogeneous pipeline抽象で自己回帰・拡散など複数ステージのモデルワークフローを1つのランタイムに統合する。
- instance poolsで優先順位付きのフォールバックインスタンスリストを設定し、キャパシティ不足時も単一インスタンスで起動を継続する。

## 使いどころ

- 音声エージェントやカスタマーサポートアシスタントなど、生成完了前に再生を始めたい低遅延音声対話。
- アクセシビリティツールやインタラクティブ学習アプリでのリアルタイムTTS配信。
