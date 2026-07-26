---
type: case
title: コンドミニアム購入審査を数週間から数分に短縮するAIエージェント
title_original: 'Case Study: How CondoScan is Simplifying Condo Purchases with LlamaIndex and LlamaParse'
company: CondoScan
industry: other
cloud: []
patterns:
- rag
- document-processing
- ai-agent
components:
- LlamaIndex
- LlamaParse
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/case-study-how-condoscan-is-simplifying-condo-purchases-with-llamaindex-and-llamaparse
published_at: '2026-07-19'
---

## 概要

カルガリー拠点のスタートアップCondoScanは、コンドミニアム購入時に必要な10〜40件・数百ページの財務書類を自動評価するプロダクトを、LlamaIndexとLlamaParseを使い6か月で本番投入した。専門家による約2週間の手動レビューを数分に短縮し、特別査定などの財務リスクを事前に検知する。

## 設計のポイント

- LlamaParseで議事録・準備金調査・予算書などをベクトルDB投入用に自動でパース・構造化する
- エージェントワークフローで文書内容とアルバータ州のコンドミニアム法など外部規制を突き合わせ、財務損失リスクとガバナンスを評価する
- 静的なプロンプトチェーンではなくエージェントに動的にツール選択・推論させることで、他フレームワークより高い精度を実現した
- 評価結果をレポート化するだけでなく、コンドミニアムの状態について自然言語で質問できるチャット機能を統合した

## 使いどころ

- 住宅購入前に大量の財務書類を短時間で審査したい個人ユーザー
- コンドミニアムのHOAガバナンスや財務健全性を体系的にベンチマークしたいプロダクト開発チーム
- 非構造化文書からのリスク抽出を自動化したい不動産・金融サービス系スタートアップ
