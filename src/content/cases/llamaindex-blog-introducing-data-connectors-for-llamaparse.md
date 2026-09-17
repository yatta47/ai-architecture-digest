---
type: announcement
title: LlamaParseにSharePoint/Google Driveのデータコネクタを追加
title_original: Introducing Data Connectors for LlamaParse
industry: cross-industry
cloud: []
patterns:
- document-processing
- data-federation
components:
- LlamaParse
- SharePoint
- Google Drive
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-data-connectors-for-llamaparse
published_at: '2026-09-17'
---

## 概要

LlamaParseにSharePointとGoogle Driveのデータコネクタが追加され、ドキュメントを手動アップロードせずに既存フォルダを接続してParse・Extract・Indexに利用できるようになった。同期フォルダの新規・更新ファイルは日次で自動同期され、インデックス更新時も変更のあったファイルのみが再処理される。エージェントやワークフローは同じ同期フォルダから構造化データと引用元ドキュメントの両方を参照できる。

## 設計のポイント

- 手動アップロードをやめ、既存の共有フォルダをソースとして接続する同期型の取り込みにする
- 同期と処理（Parse/Extract/Index）のステップを分離し、変更ファイルのみ差分再処理することでコストと時間を抑える
- 構造化データの抽出元とエージェントが引用する原文ソースを同じ同期フォルダに揃え、一貫性を保つ

## 使いどころ

- SharePointやGoogle Driveで日常的にドキュメントを管理しているチームがRAGやエージェントに継続的にデータを反映したい場合
- 四半期レポートなど定期更新されるドキュメント群から財務分析エージェントが最新情報を参照する場面
