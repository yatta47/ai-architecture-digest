---
type: announcement
title: コミュニティ主導でAI画像生成の代表性データを構築する仕組み
title_original: A new approach to AI data puts communities in charge
company: Microsoft
industry: cross-industry
cloud: []
patterns:
- human-in-the-loop
- eval
components:
- Community Library Creator
- Hugging Face
outcome:
  type: quality
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://news.microsoft.com/signal/articles/a-new-approach-to-ai-data-puts-communities-in-charge/
published_at: '2026-07-22'
---

## 概要

Microsoft Researchは、障害当事者などの当事者コミュニティが自ら画像とその意味づけを注釈し、AI生成画像の評価基準を定義できるツール「Community Library Creator」を開発した。コミュニティはテーマ選定・画像収集・注釈・生成画像への評価という一連のプロセスを主導し、そのレーティングがAIモデルの学習・改善へのフィードバックループとして活用される。データの所有権や第三者への共有・削除の可否もコミュニティ側が保持する契約設計になっている。

## 設計のポイント

- コミュニティ自身がテーマ選定から画像収集・注釈・生成結果の評価までを一貫して主導する構造化プロセスを採用している
- 1ライブラリあたり約400枚の実世界画像に絞り込み、量より質を重視したデータセット設計にしている
- 生成画像に対するコミュニティのレーティングを継続的なフィードバックループとしてモデル改善に還元している
- データの所有権と共有範囲・削除の決定権をコミュニティ側に残す契約・運用プロセスを設けている

## 使いどころ

- ウェブ上のデータに偏りやステレオタイプが多い障害・少数属性コミュニティのAI画像生成品質を改善したい場合
- アドボカシー団体がAIベンダーと協働し、自分たちの代表性に関するデータと評価基準を主導したい場面
- モデル開発者が公開データの偏りを補う追加の学習・評価データセットを、当事者の同意付きで調達したい場面
