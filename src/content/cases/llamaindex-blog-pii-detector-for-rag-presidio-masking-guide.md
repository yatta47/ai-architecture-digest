---
type: guidance
title: PresidioでRAGに混入する個人情報を検出・マスキングする
title_original: 'PII Detector: hacking privacy in RAG'
industry: cross-industry
cloud: []
patterns:
- rag
- guardrails
components:
- Microsoft Presidio
- LlamaIndex
outcome:
  type: risk-compliance
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/pii-detector-hacking-privacy-in-rag
published_at: '2024-03-13'
---

## 概要

RAGではモデルとベクトルDBの両方で個人情報対策が必要だと整理し、OSSのPresidioで検出・匿名化する方法を紹介する。

## 設計のポイント

- ベクトルDBへ平文の個人情報を保存せず、取り込み前に匿名化する。
- NER・正規表現・チェックサムを組み合わせ、独自の認識器も追加する。
- 検出は万能ではないため暗号化・アクセス制御・地域規制対応を併用する。

## 使いどころ

- 個人情報を含む非構造化文書をRAGに入れる開発者。
- GDPRやHIPAA対応を求められるチーム。
