---
type: announcement
title: Claudeがウェブ検索に対応、引用付きの最新情報を回答に反映
title_original: Claude can now search the web
industry: cross-industry
cloud: []
patterns:
- rag
components:
- Claude 3.7 Sonnet
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/web-search
published_at: '2025-03-20'
---

## 概要

Claudeが会話中にウェブ検索を実行し、最新情報を引用付きで回答に組み込めるようになった。営業・金融分析・研究・購買比較など、最新データを要する用途での回答精度と鮮度の向上を狙う。

## 設計のポイント

- 検索結果に直接引用（citation）を付与し、ユーザーがソースをすぐ確認・ファクトチェックできるようにする
- ユーザーがプロフィール設定でウェブ検索のオン/オフを切り替えられるようにする
- 検索の要否をモデル自身に判断させ、必要な場合のみウェブ検索を発火させ会話形式で結果を統合する

## 使いどころ

- 営業担当が商談前に業界動向や見込み客の課題を調査する場面
- 金融アナリストが最新の市場データや決算情報を踏まえて投資判断や財務モデルを更新する場面
- 研究者が最新文献を横断的に調べて研究提案や文献レビューを補強する場面
- 消費者が複数情報源の価格・レビューを比較しながら購買判断をする場面
