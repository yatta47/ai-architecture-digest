---
type: guidance
title: エージェント型ドキュメント処理とは何か:4層アーキテクチャの解説
title_original: What Is Agentic Document Processing?
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- ai-agent
- rag
components:
- LlamaParse
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/agentic-document-processing
published_at: '2026-07-18'
---

## 概要

従来のIDP(インテリジェント文書処理)はテンプレートが崩れるたびに人手のレビューキューに頼っていた。LlamaIndexは「脳(LLMによる推論・計画)」「記憶(RAGによる知識ベース)」「ツール(API/ERP連携)」「出力(構造化データ)」の4要素からなるエージェント型文書処理アーキテクチャを提示し、例外処理を自律的に解決できるようにする設計を解説する。

## 設計のポイント

- 抽出(データを取り出す)と理解(その意味を文脈の中で把握する)を明確に区別し、契約条項のような条件付き制約もリスクフラグとして解釈できるようにする
- テキストは言語モデル、図表は視覚モデル、レイアウトはレイアウト認識モデルというように内容種別ごとに専門モデルを使い分け、オーケストレーション層が結果を統合する
- 人間の介入(HITL)は低信頼度の意思決定ポイントに限定し、大半の例外はLLMの判断で自律的に解決させることで従来IDPの人手依存を減らす

## 使いどころ

- 契約書の条項を自動レビューし社内プレイブックとの矛盾を検出したい法務チーム
- 口座開設など複数書類にまたがるオンボーディング処理を自動化したい金融機関のオペレーション部門
