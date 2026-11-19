---
type: case
title: 文化的な判断をクエリ化した動画探索QuickSearch
title_original: How Social Department built culture-aware video discovery
company: Social Department
industry: media
cloud:
- aws
patterns:
- video-intelligence
- rag
components:
- Amazon Bedrock
- QuickSearch
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-social-department-built-culture-aware-video-discovery/
published_at: '2026-11-18'
---

## 概要

Social Departmentは、エンタメ向けマーケティングで「引用されやすい台詞」「ミーム向きの瞬間」といった編集上の判断を、実行可能な検索パイプラインとして実装した。Bedrock上のモデルで、Shareable Scenes、Quotable Quotes、Memeable Moments、Trend Alignを1操作で返す。

## 設計のポイント

- 編集上の定義を検索パイプラインとして実装し、人手での視聴を代替する。
- ライブラリ外のトレンドを継続的に取り込み、判断に使う。
- モデルをBedrock上で動かし、データをAWSの境界内に留める。

## 使いどころ

- 大量の映像資産から宣伝用の場面を探すマーケティングチーム。
- 意味検索では答えにくい判断型のクエリを扱うとき。
