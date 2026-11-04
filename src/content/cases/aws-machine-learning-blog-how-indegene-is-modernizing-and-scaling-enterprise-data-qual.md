---
type: case
title: ライフサイエンス企業のLLMデータ品質ルール生成エージェント
title_original: How Indegene is modernizing and scaling enterprise data quality in life sciences
company: Indegene
industry: healthcare
cloud:
- aws
patterns:
- ai-agent
- human-in-the-loop
- guardrails
components:
- NEXT Unified Data Platform
- AWS
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-indegene-is-modernizing-and-scaling-enterprise-data-quality-in-life-sciences/
published_at: '2026-11-04'
---

## 概要

IndegeneはNEXT統合データ基盤上に、文脈を考慮したデータ品質ルールを生成・検証し、実行可能なSQL/Pythonまで出力するLLMエージェントを構築した。技術ルールと業務ルールの分断を埋め、人によるレビューを組み込んだ集中ガバナンスで運用する。

## 設計のポイント

- 業務用語集やSOPにある業務ルールと、コード上の技術ルールをLLMで橋渡しする。
- 生成したルールを検証してから実行コードに変換する。
- 人が承認するガバナンスを集中管理で組み込む。

## 使いどころ

- 規制の厳しい業界でデータ品質ルールの作成・保守工数を減らしたいとき。
- データ基盤チームと業務部門のルール定義をそろえたいとき。
