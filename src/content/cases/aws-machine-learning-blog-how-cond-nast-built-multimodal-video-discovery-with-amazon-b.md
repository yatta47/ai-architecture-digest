---
type: case
title: Condé Nastの14万本動画を横断するマルチモーダル動画検索
title_original: How Condé Nast built multimodal video discovery with Amazon Bedrock
company: Condé Nast
industry: media
cloud:
- aws
patterns:
- video-intelligence
- rag
- event-driven
- parallel-execution
components:
- Amazon Bedrock
- TwelveLabs Marengo
- Amazon OpenSearch Service
- Amazon S3
- Amazon ECS
- AWS Fargate
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-conde-nast-built-multimodal-video-discovery-with-amazon-bedrock/
published_at: '2026-09-29'
---

## 概要

Condé Nastは14万本超の動画から素材を探す作業に1件平均250分かかっていた。TwelveLabs Marengoの埋め込みとOpenSearchのベクトル検索で映像・音声・書き起こしを横断する意図ベース検索を構築し、2分未満に短縮した。

## 設計のポイント

- 映像・音声・書き起こしを同時に埋め込めるモデルを選び、意図ベースの検索を実現する。
- 重い埋め込み生成を行う取り込み系と、低遅延な検索提供系を分離し、それぞれ独立にスケールさせる。
- イベント駆動で取り込み、チャンク単位の並列処理・再試行・追跡性を確保して大規模バックフィルに耐える。
- Bedrock経由でIAM・VPC・CloudTrailのガバナンスを適用し、専用のモデル基盤を運用せずに済ませる。

## 使いどころ

- 大規模な動画・画像アーカイブを持つメディア企業の編集部門。
- キーワード検索では見つからない素材を発掘したいコンテンツ運用チーム。
- 埋め込み生成と検索提供の分離設計を検討している基盤担当者。
