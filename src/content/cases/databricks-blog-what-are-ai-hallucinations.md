---
type: guidance
title: AIハルシネーションの原因と企業における対策
title_original: What are AI hallucinations?
industry: cross-industry
cloud: []
patterns:
- rag
- eval
- guardrails
components: []
outcome:
  type: risk-compliance
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/ai-hallucinations
published_at: '2026-08-13'
---

## 概要

生成AIのハルシネーション(もっともらしいが事実に反する出力)がなぜ起きるかを、次トークン予測という仕組み・不確実性を認めない学習報酬・学習データの限界・temperature等の生成設定から解説する。新しい推論モデルほどハルシネーション率が上がる場合がある点や、Google Bard・Air Canadaのチャットボット・Bing Sydney・弁護士の架空判例引用など実際の被害事例を挙げ、RAGやドメイン特化ファインチューニング、体系的な評価、データガバナンスによるリスク低減を提案する。

## 設計のポイント

- モデルは事実を検索しているのではなく次に来やすい単語を予測しているに過ぎないと理解した上でシステムを設計する
- RAGで検証可能な出典に接地させ、体系的な評価フレームワークで継続的にハルシネーション率を測定する
- 高リスク領域(医療・法務等)では人間レビューを組み込み、AIの回答をそのまま最終判断に使わない

## 使いどころ

- 顧客対応チャットボットや法務・医療などハルシネーションが実害につながる領域にAIを導入する企業
- 新しい推論モデルへの切り替え時にハルシネーション率の変化を評価したいチーム
