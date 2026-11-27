---
type: guidance
title: Llama 2をtext-to-SQL向けにファインチューニングする手順
title_original: Easily Finetune Llama 2 for Your Text-to-SQL Applications
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- text-to-sql
- fine-tuning
components:
- Llama 2
- OpenLLaMa
- PEFT
- Modal
- LlamaIndex
- sql-create-context
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/easily-finetune-llama-2-for-your-text-to-sql-applications-ecd53640e10d
published_at: '2023-08-17'
---

## 概要

小型のオープンモデルはSQL生成が苦手なため、公開データセットで追加学習し、LlamaIndexから任意のSQL DBに問い合わせる手順を示す。

## 設計のポイント

- 質問とテーブル定義を入力、正解SQLを出力とする形式でデータを整える。
- PEFTで一部のパラメータだけを学習し、計算コストを抑える。
- 学習の計算基盤はModalに任せ、調整済みモデルは下流のアプリにそのまま差し込む。

## 使いどころ

- 外部APIに頼らず自然言語でのDB分析を実現したいチーム向け。
- 小型モデルを特定タスクに適応させる手順を学びたい開発者向け。
