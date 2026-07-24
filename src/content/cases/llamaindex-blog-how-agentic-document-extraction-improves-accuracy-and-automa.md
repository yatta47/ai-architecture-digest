---
type: guidance
title: エージェント型ドキュメント抽出が精度と自動化をどう向上させるか
title_original: How Agentic Document Extraction Improves Accuracy and Automation
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- ai-agent
components:
- LlamaParse
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/agentic-document-extraction
published_at: '2026-07-18'
---

## 概要

テンプレートベースのOCRは文書レイアウトが変わるたびに壊れる。LlamaIndexはplan-act-verifyループで文書構造を先に理解してから抽出し、抽出後に妥当性を自己検証するエージェント型ドキュメント抽出により、請求書や複雑な医療フォームでもテンプレート保守なしに高精度を保つ手法を解説する。

## 設計のポイント

- 抽出前に文書種別とレイアウト構造(ヘッダー/データ領域の位置)を特定し、全文を左から右へ流し読みするのではなく該当領域だけを狙って抽出するplan-act-verifyループを採る
- 抽出後に日付や数値が妥当な範囲かを自己検証し、OCRエンジン自身は自信満々でも意味的におかしい値をフラグ付けする
- テキストの位置情報をバウンディングボックスで紐付ける視覚的グラウンディングにより、同一フォーマットの数値でも「合計」と「小計」をレイアウト上の位置で区別する
- 表構造は列境界の座標をハードコードせず、ヘッダーとセルの対応を都度セマンティック・空間的に推論することでテンプレート変更に追従する

## 使いどころ

- ベンダーごとに異なる請求書フォーマットをテンプレート保守なしに処理したい経理・オペレーション部門
- 手書き注記や複数セクションが混在する医療フォームなど高難度文書を扱うヘルスケア領域
