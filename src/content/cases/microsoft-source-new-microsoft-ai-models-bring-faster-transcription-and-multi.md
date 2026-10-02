---
type: announcement
title: 低遅延ボイスエージェント向けMAI音声認識・音声合成モデルの発表
title_original: New Microsoft AI models bring faster transcription and multilingual voices
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- voice-agent
- realtime-transcription
- multilingual-localization
- inference-optimization
components:
- MAI-Transcribe-2-Streaming
- MAI-Voice-2.1
- MAI-Voice-2.1-Flash
- Microsoft Foundry
- Azure Voice Live
- OpenRouter
- MAI Playground
outcome:
  type: speed
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://microsoft.ai/news/our-first-streaming-transcription-model/
published_at: '2026-10-01'
---

## 概要

Microsoft AIが、ストリーミング音声認識MAI-Transcribe-2-Streamingと、多言語音声合成MAI-Voice-2.1およびその高速版Flashを発表した。認識は約100msで暫定結果を返し、合成Flashは150msの遅延で低価格を実現する。両者の組み合わせで音声エージェントの聞く・考える・話すループの時間を節約する。

## 設計のポイント

- 暫定結果(partials)を先に出して後から修正することで、話し終わる前にエージェントが推論やツール呼び出しを始められる。
- 認識と合成の両端で遅延を削り、その分をエージェントの推論やツール利用に回す。
- 1つの声で複数言語を自然なアクセントで話せるようにし、ブランドの声を統一する。
- 音声クローンには同意ガードレールを組み込み、悪用を防ぐ。

## 使いどころ

- 通話中に要件を処理し始めるカスタマーサービス向け音声エージェント。
- 言語を自動判別して同じ声で返答する多言語アシスタント。
- 学習・ロールプレイなど複数話者の音声コンテンツを作る場面。
