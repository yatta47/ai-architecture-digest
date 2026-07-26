---
type: announcement
title: LlamaParseに新モデル・傾き自動補正・信頼度スコアを追加
title_original: 'LlamaParse Update May 2025: New Models, Skew Detection and More'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
components:
- LlamaParse
- GPT-4.1
- Gemini 2.5 Pro
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaparse-update-may-2025-new-models-skew-detection-and-more
published_at: '2026-07-19'
---

## 概要

ドキュメントパースサービスLlamaParseに、GPT-4.1・Gemini 2.5 Proモデルの追加、スキャン文書の回転・傾き自動検出補正、ページ単位の信頼度スコア、許容エラー率指定、失敗ページの扱い方（生テキスト/空白/エラーメッセージ）を選べる機能を追加したアップデート内容をまとめている。

## 設計のポイント

- ページ単位に信頼度スコアを付与し、閾値以下を自動フラグすることで後続の人手レビュー対象を絞り込めるようにする
- 失敗ページの扱いをraw_text/blank_page/error_messageから選択可能にし、後続パイプラインの用途に応じてフェイルセーフの挙動を変える
- 許容エラー率（page_error_tolerance）を指定できるようにし、多少のページ失敗ではジョブ全体を失敗させない運用を可能にする

## 使いどころ

- スキャンした帳票や傾いた文書を大量にバッチ処理する必要がある場合
- パース精度をページ単位でモニタリングし、低信頼ページのみ人手確認したい運用チーム
