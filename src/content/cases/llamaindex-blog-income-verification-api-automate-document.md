---
type: guidance
title: 収入証明APIの設計:給与API・銀行データ・文書抽出の使い分け
title_original: 'Income Verification API: Automate Document-Based Income Verification'
industry: financial-services
cloud: []
patterns:
- document-processing
- data-federation
components:
- Argyle
- Pinwheel
outcome:
  type: risk-compliance
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/Income-verification-api
published_at: '2026-07-18'
---

## 概要

給与APIはW-2従業員はカバーできてもギグワーカーや自営業者には弱く、銀行データは収入源を証明できない。文書抽出APIと給与APIを組み合わせたハイブリッド構成が、幅広い収入形態を高精度・自動でカバーする収入証明ワークフローの鍵になると論じる。

## 設計のポイント

- 給与API・銀行データ・文書抽出をそれぞれの守備範囲に応じて使い分ける
- 収入タイプごとに異なるデータ収集経路をハイブリッドに統合する設計
- 抽出結果をそのまま与信判断に使わず構造化レコード化して下流システムに渡す

## 使いどころ

- 自営業・ギグワーカーなど非定型な収入証明が必要な与信審査
- 複数の収入証明手段を統合したいレンダー・不動産賃貸業者
