---
type: announcement
title: 金融アナリスト向けCoworkプラグイン群とFactSet/MSCI連携
title_original: Cowork and plugins for finance
industry: financial-services
cloud: []
patterns:
- ai-agent
components:
- Claude Cowork
- FactSet
- MSCI
- Excel
- PowerPoint
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/cowork-plugins-finance
published_at: '2026-02-24'
---

## 概要

投資銀行・エクイティリサーチ・プライベートエクイティ・資産運用など金融の職種別に特化した5つのプラグインと、FactSet・MSCIの新規MCPコネクタを発表。ExcelとPowerPointの間でコンテキストを保持したまま、リサーチからモデル更新、資料作成までを1つのセッションで完結できるようにする。

## 設計のポイント

- ExcelとPowerPointを跨いでコンテキストを保持し、入力データの変更をモデルと資料の両方へ自動反映させる
- 金融機関固有のデータ資産（FactSetやMSCI）は汎用プラグインでは代替できないため、専用MCPコネクタとして直接組み込む

## 使いどころ

- 決算書の解析からモデル更新、サマリースライド作成までをツール切り替えなしで行いたいエクイティアナリスト
- 大量の取引資料をレビューし財務データを標準化して抽出したいプライベートエクイティのディールチーム
