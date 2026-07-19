---
type: case
title: Flo Healthの医療コンテンツレビュー自動化基盤
title_original: Scaling medical content review at Flo Health with Amazon Bedrock – Part 2
company: Flo Health
industry: healthcare
cloud:
- aws
patterns:
- llmops
- document-processing
- rag
- eval
- human-in-the-loop
- guardrails
components:
- Amazon Bedrock
- Contentful CMS
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/scaling-medical-content-review-at-flo-health-with-amazon-bedrock-part-2/
published_at: '2026-07-14'
---

## 概要

Flo HealthはAWSとのPoCを本番システムに発展させ、Amazon Bedrock上にレビュー観点ごとの「AI Judge」群とRAGによる生成支援を構築。医療専門家によるレビュー時間を60%削減し、人員を増やさずにコンテンツ生産量を3倍にした。

## 設計のポイント

- 医学的正確性・法令順守・ブランドスタイルなどレビュー観点ごとに専用プロンプトのAI Judgeを分離し、他のJudgeに影響を与えずに個別改善できるようにする。
- 社内ガイドラインと外部の信頼できる医療情報源への二段階検証で、根拠のない生成(ハルシネーション)を防ぐ。
- Judgeの指摘をもとにBedrockで改善案を生成しContentful上でハイライト表示、最終判断は人間の専門家に残す。

## 使いどころ

- 専門家レビューがボトルネックになっているコンテンツパイプラインを持つ組織。
- 正確性が最優先される医療・法務など高リスク領域のコンテンツ生成・レビュー。
