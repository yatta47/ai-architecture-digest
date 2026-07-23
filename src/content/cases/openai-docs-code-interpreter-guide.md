---
type: guidance
title: Code Interpreterツールでサンドボックス上のPython実行をエージェントに組み込む
title_original: Code Interpreter
industry: cross-industry
cloud: []
patterns:
- ai-agent
- document-processing
components:
- Responses API
- Code Interpreter
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/tools-code-interpreter
published_at: '2025-07-22'
---

## 概要

Code Interpreterはモデルがサンドボックス環境でPythonコードを書いて実行できる組み込みツールで、データ分析やファイル処理、グラフ生成、数学問題の反復的な求解に使える。o3やo4-miniなど推論モデルでは画像のクロップ・回転などの視覚処理能力の強化にも活用される。

## 設計のポイント

- コード実行が失敗した場合、モデルは自律的にコードを書き直して再実行を繰り返せる。
- containerパラメータでメモリ上限などサンドボックスのリソースを制御できる。
- 推論モデルと組み合わせることで画像処理を伴う視覚的タスクの精度を底上げできる。

## 使いどころ

- データ分析や数式処理を対話的に行わせたいチュートリング・分析アシスタント。
- 生成した画像やグラフをその場でユーザーに提示したいアプリケーション。
