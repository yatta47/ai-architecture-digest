---
type: case
title: LlamaParseによる住宅ローン書類の抽出・検証・コンプライアンス自動化
title_original: 'Loan processing workflow: automate document extraction'
company: LlamaIndex
industry: financial-services
cloud: []
patterns:
- document-processing
- human-in-the-loop
- ai-agent
components:
- LlamaParse
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/loan-processing-workflow
published_at: '2026-10-07'
---

## 概要

150〜200ページに及ぶ住宅ローンファイルについて、LlamaParseで書類種別ごとに項目を抽出し、書類間の整合性検証やTRID等のコンプライアンスチェックを行うワークフローを示す。信頼度スコアの閾値で人の確認を挟む。

## 設計のポイント

- 書類種別ごとにパースモードを使い分けて抽出する
- 複数書類を突き合わせる検証で手入力の誤りを検出する
- 信頼度スコアの閾値を設けて、低い項目だけ人が確認する

## 使いどころ

- ローンの書類確認と審査前処理を自動化したい金融機関
- 書式が多様な文書の抽出パイプライン
