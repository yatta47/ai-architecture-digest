---
type: guidance
title: 再埋め込み不要の線形アダプタで任意の埋め込みを検索向けに調整
title_original: Fine-tuning a Linear Adapter for Any Embedding Model
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- fine-tuning
- rag
- eval
components:
- LlamaIndex
- EmbeddingAdapterFinetuneEngine
- bge-small-en
- text-embedding-ada-002
- PyTorch
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/fine-tuning-a-linear-adapter-for-any-embedding-model-8dd0a142d383
published_at: '2023-09-06'
---

## 概要

文書の埋め込みは固定し、クエリの埋め込みだけを線形変換するアダプタを学習する手法の解説。任意の埋め込みモデルに適用でき、検索性能の小幅な改善が期待できる。

## 設計のポイント

- 文書側を固定してクエリ側だけ変換し、コーパスの再索引を不要にする。
- LLMで生成した質問と文脈の組を学習・評価データにする。
- 軽量な線形層に絞ることで手元のPCでも学習でき、データ分布の変化に応じて再学習しやすい。

## 使いどころ

- 大規模な索引を作り直さずに検索精度を上げたいチーム向け。
- OpenAIなど重みを調整できない埋め込みAPIを使っている場合。
