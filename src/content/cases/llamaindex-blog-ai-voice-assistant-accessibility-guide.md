---
type: case
title: ウェイクワードで起動するRAG対応の音声アシスタントC3
title_original: 'AI Voice Assistant: Enhancing Accessibility in AI with LlamaIndex and GPT-3.5'
industry: cross-industry
cloud: []
patterns:
- voice-agent
- rag
components:
- LlamaIndex
- create-llama
- GPT-3.5
- React
- Flask
- Vercel
- Render
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/ai-voice-assistant-enhancing-accessibility-in-ai-with-llamaindex-and-gpt3-5-f5509d296f4a
published_at: '2024-01-14'
---

## 概要

タイピングが難しい利用者にも使えるよう、音声で一般質問や文書への質問ができるアシスタントを構築した個人プロジェクト。ブラウザの音声認識・音声合成をReact側で使い、Flaskバックエンドを通じてLLMとRAGに問い合わせる。

## 設計のポイント

- 音声認識と合成はブラウザAPIに任せ、サーバーはテキストの問い合わせ処理に専念させる。
- ウェイクワード検出と本認識を別の認識インスタンスに分ける。
- 会話履歴をテキストでも表示し、応答を後から確認できるようにする。

## 使いどころ

- アクセシビリティ向けの音声UIを試作する開発者。
- 文書Q&Aに低コストで音声入出力を追加したい場面。
