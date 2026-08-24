---
type: case
title: LLMと埋め込みでメタデータのスキーマ整合・欠損値補正を自動化するハーモナイゼーション基盤
title_original: AI-powered metadata correction and harmonization
industry: healthcare
cloud:
- aws
patterns:
- human-in-the-loop
- metadata-harmonization
components:
- Amazon Bedrock
- Amazon S3
- Amazon DynamoDB
- Amazon Cognito
- Amazon ECS
- Amazon Titan
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/ai-powered-metadata-correction-and-harmonization/
published_at: '2026-08-24'
---

## 概要

AWSは、異なるソース由来のメタデータのスキーマ不整合やフィールド値の誤りをLLMと埋め込みモデルで自動検出・補正するハーモナイゼーション基盤を紹介する。Amazon Bedrock上のLLMによるスキーマ意味的マッチングと、Amazon Titan埋め込みによる類似度ベースの値補正を段階的に組み合わせ、ヒューマンインザループの承認を残しつつスケールする。スキーマ整合とフィールド値検証を並列に実行し、修正候補を提示してから最終判断は利用者に委ねる。

## 設計のポイント

- コストと精度のバランスを取るため、まず古典的NLP・埋め込み類似度で解決し、曖昧なケースだけLLMに回すレイヤードアーキテクチャを採用する
- スキーマ整合とフィールド値検証を並列ストリームとして実行し、検証エラーを「必須項目・列挙値・パターン」の3種に分類して修正提案の文脈を明確にする
- 自動修正を適用せず常に人間の最終承認を残すヒューマンインザループ設計で、研究者のドメイン知識を保持する
- 埋め込み結果をキャッシュすることでLLM呼び出しを最小化し推論コストを予測可能にする

## 使いどころ

- 複数機関から集まる研究・オープンサイエンスデータのメタデータを統一フォーマットに揃えたい場合
- ルールベースの表記ゆれ対応では対応しきれない同義語・略語を含むメタデータを扱う場合
- 自動化は進めたいが最終承認は人間に残したいガバナンス重視のデータ基盤
