---
type: guidance
title: Vellum連携によるLLMプロンプトのテスト・版管理・本番監視
title_original: Vellum + LlamaIndex integration
industry: cross-industry
cloud: []
patterns:
- llmops
- eval
- prompt-optimization
components:
- Vellum
- LlamaIndex
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/vellum-llamaindex-integration-58b476a1e33f
published_at: '2023-06-05'
---

## 概要

LlamaIndexのプロンプトをVellumに登録し、本番前の単体テストと本番後の版管理・監視を行う連携の紹介。用途別の評価指標やユーザーフィードバックの集め方も整理している。

## 設計のポイント

- プロンプトを薄いAPIプロキシ経由で配信し、コード変更なしで版を切り替える。
- 本番投入前に50〜100件のテストケースを用意し、変更時は過去の本番入力で回帰確認する。
- 分類・抽出・コード生成・創作など用途ごとに評価指標を変える。
- 明示的な評価が集まりにくければ、再生成や無編集送信などの暗黙フィードバックを使う。

## 使いどころ

- 本番LLM機能のプロンプト変更で品質劣化を防ぎたいチーム。
- モデルやプロバイダを比較しながらプロンプトを調整する場面。
