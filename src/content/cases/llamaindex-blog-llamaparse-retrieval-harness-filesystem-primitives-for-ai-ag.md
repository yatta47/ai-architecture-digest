---
type: announcement
title: エージェント向けファイルシステム操作を備えたLlamaParse Retrieval Harness
title_original: Announcing Retrieval Harness for LlamaParse Index
industry: cross-industry
cloud: []
patterns:
- rag
- ai-agent
- document-processing
components:
- LlamaParse Index
outcome:
  type: reliability
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/announcing-retrieval-harness
published_at: '2026-07-18'
---

## 概要

従来のRAGはチャンク境界をまたぐ質問に弱く、かといってエージェントがファイルを総当たりで読むとトークン予算を浪費する。LlamaParse IndexはRetrieval Harnessとして「List Files」「File Grep」「File Read」などファイルシステム的なツール群と、ページのスクリーンショットを紐づけた視覚レイアウト保持、段階ごとのパイプライン監視を追加した。

## 設計のポイント

- ハイブリッド検索（ベクトル＋キーワード＋リランキング）を第一段の絞り込みとし、正規表現グレップや直接読み取りで補完する
- テキスト化だけでは失われる表・図面のレイアウトを、ページスクリーンショットとして源泉に紐づけて保持する
- 差分同期により変更されたファイルのみを再処理し、コストとレイテンシをフォルダサイズではなく実際の変更量に比例させる

## 使いどころ

- チャンク分割では答えが見つからない複雑な質問に答える必要があるエンタープライズ検索エージェント
- 同期パイプラインの障害箇所を素早く特定したい本番運用チーム
