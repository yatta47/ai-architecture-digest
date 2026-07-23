---
type: guidance
title: Sora 2の動画生成プロンプト設計ガイド
title_original: Sora 2 Prompting Guide
company: OpenAI
industry: media
cloud: []
patterns:
- generative-video-editing
- prompt-optimization
components:
- Sora 2
- Sora API
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide/
published_at: '2026-03-12'
---

## 概要

OpenAIのSora 2 APIにおける、キャラクター参照・高解像度出力・最大20秒動画・動画拡張などを踏まえたプロンプト設計ガイド。詳細なプロンプトは一貫性と制御を、簡潔なプロンプトは創造的な多様性を生むというトレードオフを軸に、撮影監督への指示に例えた書き方を解説する。

## 設計のポイント

- 解像度・尺・キャラクター参照はプロンプトの文章では制御できずAPIパラメータとして明示的に指定する
- 詳細な指示ほど一貫性は増すがモデルの創造的余地は減るというトレードオフを踏まえ、目的に応じて詳細度を調整する
- 長い1本のクリップより短いクリップを複数生成して編集でつなぐ方が、指示追従性が高い場合がある

## 使いどころ

- ブランドやキャラクターの一貫性を保ちながら複数動画を生成したい制作チーム
- 実写映画のような特定の撮影スタイル（IMAXエアリアル、35mmハンドヘルドなど）を再現したい場合
