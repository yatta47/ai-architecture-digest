---
type: guidance
title: OpenAI Speech APIの音声表現力をブラウザで試せるTTSデモ実装
title_original: OpenAI.fm
company: OpenAI
industry: cross-industry
cloud: []
patterns:
- text-to-speech
components:
- Speech API
- Next.js
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://github.com/openai/openai-fm
published_at: '2025-07-18'
---

## 概要

openai.fmはOpenAIのテキスト読み上げ(TTS)モデルを試せるNext.js製インタラクティブデモで、Speech APIを直接呼び出すシンプルな構成により、声色や話し方のプロンプト制御を体験できる。共有機能を使う場合のみPostgresへの接続を追加する任意構成になっている。

## 設計のポイント

- デモの中核機能(音声生成)はSpeech APIの呼び出しのみで完結させ、共有機能などの付加要素だけを外部DB依存にすることで最小構成での起動を可能にする。
- APIキーはサーバー環境変数として持たせ、公開デプロイ時の利用量管理はデプロイ主体の責任と明記する。

## 使いどころ

- TTSモデルのプロンプトによる声質・トーン制御を素早く試作・検証したい場合。
