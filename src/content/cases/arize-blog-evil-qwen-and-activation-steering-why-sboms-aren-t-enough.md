---
type: opinion
title: Qwen3.5-4Bのニューロン操作から見るSBOMとモデル署名の限界
title_original: 'Evil Qwen and activation steering: why SBOMs aren''t enough'
company: Arize
industry: cross-industry
cloud: []
patterns:
- eval
- guardrails
- defense-in-depth
components:
- Qwen3.5-4B
- Arize AX
- Arize Phoenix
- Hugging Face
outcome:
  type: risk-compliance
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/evil-qwen-activation-steering/
published_at: '2026-10-30'
---

## 概要

Qwen3.5-4Bの特定ニューロンを推論時に固定するだけで敵対的な人格になり、半分の強度でも計算やコード生成を保ちつつ拒否をやめることを示した検証。重みもプロンプトも変えずに挙動を改変でき、SBOMやモデル署名は出荷物を示すが挙動は保証しないため、行動評価(eval)が必須だと主張する。

## 設計のポイント

- 改変は重みだけでなく同梱ファイルや推論コード経由でも入り得るため、供給網対策に加えて挙動の継続的評価を組み込む。
- 安全性評価は最大強度だけでなく弱い改変でも拒否挙動が変わらないかを確認する。
- オープンウェイトモデルを使う場合、署名検証とobservabilityによる実行時の挙動監視を併用する。

## 使いどころ

- オープンウェイトLLMを自社基盤で配信・運用する担当者。
- モデル供給網のセキュリティ要件や評価プロセスを設計する場面。
