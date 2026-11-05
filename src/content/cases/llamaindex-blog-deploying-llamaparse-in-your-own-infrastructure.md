---
type: guidance
title: LlamaParseを自社環境にデプロイし、推論の置き場所を選ぶ
title_original: Deploying LlamaParse in your own infrastructure
company: LlamaIndex
industry: cross-industry
cloud:
- aws
- azure
- gcp
- on-prem
patterns:
- document-processing
- confidential-computing
components:
- LlamaParse
- Helm
- Kubernetes
outcome:
  type: risk-compliance
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/deploying-llamaparse-in-your-own-infrastructure
published_at: '2026-11-05'
---

## 概要

LlamaParseを自社のクラウドアカウントまたはデータセンターのKubernetesにHelmで構築する選択肢と、推論の実行場所（LlamaIndex管理、既存のモデル提供元、自前GPU）を選ぶ指針の記事。OCR・レイアウト・文書モデルと大規模言語モデルを別の場所で動かせる。

## 設計のポイント

- プラットフォームと推論を分離し、文書は自社のオブジェクトストレージに置いたまま、モデルの実行場所だけ別に選ぶ。
- OCRやレイアウトのモデルは自前GPUで動かし、推論の重い段階は外部の提供元に任せる併用ができる。
- 基盤の運用負荷を減らしたければLlamaIndex管理の推論から始める。

## 使いどころ

- 機密文書を自社環境から出せない金融・医療などの組織
- 既存のモデル提供契約やGPUを活かして文書処理を構築したいチーム
