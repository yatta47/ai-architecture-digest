---
type: case
title: 'PUBG Ally: KRAFTONがNVIDIA ACEで作った共同プレイキャラクター'
title_original: 'Q&A: How KRAFTON Built PUBG Ally, a Co-Playable Character Powered by NVIDIA ACE'
company: KRAFTON
industry: media
cloud:
- on-prem
patterns:
- voice-agent
- ai-agent
components:
- NVIDIA ACE
- Mistral-NeMo-Minitron-2B
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-krafton-built-pubg-ally-a-co-playable-character-powered-by-nvidia-ace/
published_at: '2026-07-09'
---

## 概要

KRAFTONはPUBG: BATTLEGROUNDS向けに、NPCとは異なる『共同プレイキャラクター』PUBG AllyをNVIDIA ACEで構築した。オンデバイスのASR・2BパラメータSLM・TTSで音声とゲーム状態を処理し、反射的行動はビヘイビアツリー、言語推論はSLMに分離することでクラウドLLMでは実現できない実戦的な低遅延を達成した。

## 設計のポイント

- クラウドLLMのネットワーク往復遅延を避けるため、Mistral-NeMo-Minitron-2Bを量子化しオンデバイスで実行しVRAM8GBでも動作するようにした
- 戦闘中の即応が必要な行動はビヘイビアツリーに、自然な会話や状況理解はSLMに役割分担し、言語推論の待ち時間が操作性を損なわないようにする
- 英語・韓国語・中国語のマルチリンガル対応と長短期記憶を組み合わせ、セッションをまたいだパーソナライズを実現する

## 使いどころ

- リアルタイム性が最優先されるバトルロイヤル等のゲームでAI仲間キャラクターを実装したい開発者
- クラウド依存を避けVRAM制約のあるコンシューマGPU上でオンデバイス音声AIを提供したいスタジオ
