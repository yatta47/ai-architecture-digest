---
type: announcement
title: 長尺動画を構造化メタデータに変換するPegasus 1.5のBedrock提供
title_original: Pegasus 1.5 from TwelveLabs is now available in Amazon Bedrock
company: TwelveLabs
industry: media
cloud:
- aws
patterns:
- video-intelligence
components:
- Amazon Bedrock
- TwelveLabs Pegasus 1.5
- Amazon S3
- Boto3
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/pegasus-1-5-from-twelvelabs-is-now-available-in-amazon-bedrock/
published_at: '2026-10-19'
---

## 概要

TwelveLabsの動画言語モデルPegasus 1.5がAmazon Bedrockで利用可能になった。最大2時間の動画を事前インデックスなしで解析し、ユーザー定義の条件に合う区間をタイムスタンプ付きJSONで返す。

## 設計のポイント

- analysisModeをgeneralとtime_based_metadataで切り替え、自由回答と区間抽出を同一APIで扱う。
- 動画はS3 URIまたは25MBまでのbase64で渡し、インジェスト用パイプラインを不要にしている。
- テキスト記述に参照画像を組み合わせたマルチモーダルプロンプトで、特定の製品やロゴ、人物を検出できる。
- アプリケーション推論プロファイルにタグを付けてコストをアプリ単位で追跡できる。

## 使いどころ

- 放送・スポーツ映像から編集区間や場面をまとめて抽出したい場面。
- 広告で自社ブランドの露出箇所を長尺動画から洗い出したい場面。
- データをAWS境界内に置いたまま動画を解析したい企業。
