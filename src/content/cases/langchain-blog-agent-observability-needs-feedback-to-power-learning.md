---
type: opinion
title: トレースだけでは学習ループは回らない、エージェント可観測性にはフィードバックが要る
title_original: Agent observability needs feedback to power learning
industry: cross-industry
cloud: []
patterns:
- llmops
- human-in-the-loop
- eval
components: []
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/agent-observability-needs-feedback-to-power-learning
published_at: '2026-08-26'
---

## 概要

LangChain創業者のHarrison Chaseは、エージェントの可観測性を単なるデバッグ手段として捉えるのではなく、モデル・ハーネス（プロンプトやツール定義など）・コンテキスト（検索結果やメモリ）という3つのレベルでの学習ループを駆動する基盤として位置付けるべきだと論じている。トレースは「何が起きたか」を記録するだけで、それが良かったかどうかを判断するにはユーザーのフィードバックや自動評価などの信号を紐づける必要があると指摘する。

## 設計のポイント

- エージェントの改善を「モデルの重み更新」「ハーネス（プロンプト・ツール定義・制御フロー）」「コンテキスト（検索・メモリ）」という3つのレベルに分解して捉える
- トレース単体を「学習の原材料」として扱い、そこにフィードバック（成功/失敗/効率/リスク）を紐づけて初めて改善アクションに変換できるとする
- 人手によるレビューと、サンプリング・オンライン評価・失敗パターン検知による自動化を組み合わせ、フィードバック収集をスケールさせる考え方を示す

## 使いどころ

- 本番運用中のエージェントの失敗を継続的に学習ループに変換したいチーム
- 可観測性基盤への投資判断で「トレースだけでは不十分」という視点を持ちたいプロダクト/エンジニアリングリーダー
