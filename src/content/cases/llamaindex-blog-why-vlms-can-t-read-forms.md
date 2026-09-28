---
type: case
title: チェックボックスの誤読を防ぐ、フォーム専用の構造化パーサー（LlamaParse）
title_original: Why VLMs can't read forms
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
components:
- LlamaParse
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/why-vlms-can-t-read-forms
published_at: '2026-09-28'
---

## 概要

汎用VLMにフォームのスクリーンショットを渡すだけの抽出はコスト・信頼性・精度に課題があり、特にチェックボックスの状態を誤ると下流のエージェントの判断が丸ごと変わってしまう。LlamaParseはフォームをフィールドとセクションの木構造JSONとして表現し、専用のチェックボックス状態分類器でVLMの初期予測を個別に補正する。

## 設計のポイント

- フォームをid/label/field/valueを持つFormFieldと、items配下にネストするFormSectionの木構造（Pydanticスキーマ）として表現し、同名フィールドが複数セクションにまたがっても親子関係を保持する。
- チェックボックス単体ごとに状態を判定する専用の小規模分類器を組み込み、ページ全体を一度に読むVLMの誤判定（falseと誤読されたチェック済みボックスなど）を補正する。
- 空欄のフィールドも省略せずisEmptyとして出力に残し、下流処理がフィールドの存在自体を見失わないようにする。

## 使いどころ

- W-2やForm 1040のような税務・行政フォームなど、チェックボックス1つの誤読が下流のエージェントの動作を左右する高精度が必要な文書処理。
- フォーム種別ごとに出力の一貫性を保ちつつ、年度改訂などのレイアウト差分も吸収したい定型帳票の自動処理。
