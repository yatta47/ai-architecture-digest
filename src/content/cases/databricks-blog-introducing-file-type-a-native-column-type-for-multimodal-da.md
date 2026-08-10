---
type: announcement
title: Databricks FILE型で非構造データをガバナンス付きネイティブ列として管理
title_original: 'Introducing FILE type: a native column type for multimodal data'
industry: cross-industry
cloud:
- multi-cloud
patterns:
- document-processing
- video-intelligence
- rag
components:
- Databricks Unity Catalog
- Delta Lake
- Parquet
- Databricks SQL
- Python UDF
outcome:
  type: risk-compliance
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/introducing-file-type-native-column-type-multimodal-data
published_at: '2026-08-10'
---

## 概要

Databricksは非構造データ（画像・音声・動画・文書）をテーブルの列として直接扱えるネイティブ型「FILE」のベータ版を発表した。FILE列は軽量な参照のみを保持し、行削除に伴いオブジェクトストレージ上の実体も自動削除されるためGDPR対応が容易になり、Unity Catalogの行・列レベルのアクセス制御をそのまま非構造データにも適用できる。自動運転企業のダッシュカム映像分析を例に、SQL/Python UDFとAI関数で構造化データと同じ行に処理結果を並べてエージェントが根拠付きで回答できる様子を示している。

## 設計のポイント

- FILE列は実体バイナリではなく軽量な参照のみを保持し、クエリが実際に内容を必要とするステップでのみバイトを取得することでパフォーマンスを担保する
- URL文字列でファイルパスを保持する従来手法と異なり、Unity Catalogの行・列レベルのアクセス制御とABACをFILE型に直接統合し、二重の権限管理を排除する
- 行削除とオブジェクトストレージ上のファイル実体のライフサイクルを同期させ、孤立ファイルやGDPR「忘れられる権利」対応の手作業を不要にする
- Parquet/Delta Lakeへのオープン仕様化を進めることで特定ベンダーやモデルプロバイダーへのロックインを避ける

## 使いどころ

- 契約書・ポリシー文書を横断検索できる社内ドキュメントアシスタントを構築したいチーム
- 製品画像の外観検査や動画の異常検知など、大量の非構造データにAI関数を適用したい現場
- 根拠となる実データ（画像・音声・動画）を引用しながら回答するエージェント/RAGシステムを構造化メタデータと同じ場所で管理したい場合
