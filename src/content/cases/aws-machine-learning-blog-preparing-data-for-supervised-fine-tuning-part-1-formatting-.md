---
type: guidance
title: SFT向けデータ準備ガイド：品質・多様性・一貫性のチェック法
title_original: 'Preparing data for supervised fine-tuning Part 1: Formatting and quality'
industry: cross-industry
cloud:
- aws
patterns:
- fine-tuning
- llmops
components:
- Amazon Bedrock
- Amazon Nova
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/preparing-data-for-supervised-fine-tuning-part-1-formatting-and-quality/
published_at: '2026-08-26'
---

## 概要

AWS Machine Learning Blogが、教師ありファインチューニング(SFT)向けデータ準備の要点を解説する2部構成記事の前編。SFTは新しい知識を注入するのではなく既存知識の使い方（応答の型）を教える手法だとした上で、正確性・多様性・一貫性・重複排除という4つの品質チェック観点を提示し、少量でも高品質なデータの方が大量の低品質データより効果を出すことを示している。

## 設計のポイント

- CPT→SFT→RFTの順で役割を分離する: 知識注入はCPT、応答挙動の型付けはSFT、報酬信号による最適化はRFTが担う
- 学習データは正確性・多様性(意味的カバレッジと情報の深さ)・類似タスク内の一貫性・重複排除の4観点で投入前に監査する
- プロンプトを埋め込みベクトルでクラスタリングし、疎または欠落したクラスタから本番トラフィックとのギャップ（例: 返金対応データの不足）を発見する
- 同一タスク種別内では出力形式（文体・スキーマ・固定文言）を統一し、矛盾した教師信号を排除する

## 使いどころ

- 基盤モデルの素の性能が出力スキーマ順守・ドメイン分類・トーン維持などの本番要件を満たさずSFTを検討しているMLエンジニア
- 人手アノテーション済みの学習データセットを本番投入前に品質監査したいデータ準備チーム
- LIMA/AlpaGasusのような少量精鋭データ戦略でアノテーション・学習コストを抑えたいプロジェクト
