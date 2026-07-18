---
type: guidance
title: テキスト/PDFから構造化データを抽出するOSS抽出サービスのリファレンス実装（LangChain Extract）
title_original: Open Source Extraction Service
company: LangChain
industry: cross-industry
cloud: []
patterns:
- document-processing
- context-engineering
components:
- LangChain
- LangServe
- langchain-extract
- GPT-3.5-turbo
- Pydantic
- JSON Schema
data_sources:
- PDF
- HTML
- テキスト文書
- 決算発表トランスクリプト
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/open-source-extraction-service
published_at: '2026-07-18'
---

## 概要

LangChainが、テキストやPDFなどの非構造データからスキーマに沿った構造化データを抽出するOSSサービス（langchain-extract）と、その動作を無償で試せるホスト版フロントエンドを公開した。ユーザーは自然言語でスキーマや抽出指示を定義し、few-shot例を加えながら抽出器を作成・共有でき、コアの抽出ロジックはLangServeエンドポイント経由で自前のワークフローに組み込める。記事ではUberの決算発表PDFから財務数値を抽出する例を通じて使い方を解説している。

## 設計のポイント

- 抽出情報をPydantic/JSONスキーマで宣言し、各フィールドにevidence（根拠となる原文の一文）を持たせて予測結果の検証とダウンストリームの信頼性を確保する
- モデルが指示どおりの表記に従わない場合は、大型モデルへ切り替える前にfew-shot例を数件加えて意図を明確化する
- 抽出ロジックをLangServeエンドポイントとして切り出し、既存のLangChainワークフローに差し込める疎結合な構成にする

## 使いどころ

- ソフトウェア開発者が、決算トランスクリプトや契約書などの非構造の文書から、比較・分析できる構造化データを取り出したいとき
- 自前の抽出アプリを素早く立ち上げる出発点を探している場面
