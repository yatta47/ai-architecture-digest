---
type: guidance
title: ツールコーリングとは何か、AIエージェントに実行力を与える仕組み
title_original: What is tool calling?
company: Databricks
industry: cross-industry
cloud: []
patterns:
- ai-agent
- rag
components:
- Databricks Agent Bricks
- Unity Catalog
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/what-is-tool-calling
published_at: '2026-08-06'
---

## 概要

この記事はツールコーリング(モデルが外部API・DB・コード実行などを呼び出す仕組み)の6ステップの処理ループ(要否判断→ツール選択→リクエスト生成→レスポンス処理→回答生成→反復)を解説し、静的なチャットボットと実際に行動できるAIエージェントを分ける中核機能として位置づけている。Databricks Agent BricksがMCPとUnity Catalogガバナンスにネイティブ対応することで、ガバナンスされたツールコーリングエージェント基盤を提供するとしている。

## 設計のポイント

- ツールはモデルに直接実行させず、モデルが生成した構造化リクエストをアプリケーション層が実行し結果を返す間接実行の形にする
- 各ツールを名前・説明・パラメータのスキーマで記述し、モデルがユーザー意図とスキーマを突き合わせて選択できるようにする
- 複数ツール呼び出しを要する複雑な依頼では、各ステップで十分な情報が揃ったかを評価し続ける反復ループを組み込む

## 使いどころ

- CRM更新やレポート生成など、会話だけで完結せず外部システムへの実行アクションが必要な業務
- ガバナンスされたエンタープライズデータに対してツールコーリングエージェントを構築したいデータチーム
