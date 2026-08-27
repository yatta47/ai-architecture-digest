---
type: case
title: トレース集計をSQL化してコスト17分の1に抑えたArize PhoenixのMCPサーバー設計
title_original: Arize Phoenix has a built-in MCP server that lets your agents query traces with SQL
company: Arize
industry: cross-industry
cloud: []
patterns:
- llmops
- text-to-sql
- eval
components:
- Arize Phoenix
- MCP (Model Context Protocol)
outcome:
  type: cost
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/phoenix-mcp-sql-code-mode/
published_at: '2026-08-27'
---

## 概要

Arize Phoenixに組み込みMCPサーバーとread-onlyのSQLツール(describeSqlSchema/executeSql)を追加し、コーディングエージェントがトレースを1件ずつページングして取得する代わりにDB側で集計できるようにした。エージェントはコードモードでサンドボックス内のプログラムからツールを呼び出し、結果だけをモデルコンテキストに返すことで、8問のベンチマークで従来のretrieval専用ツール比で平均17倍のコスト削減を達成した。

## 設計のポイント

- 集計・フィルタ・JOINが必要な質問はDB側に処理を寄せ、retrieval専用ツールによる全件ページングを避ける
- モデルが書いたSQLをそのまま実行せず、毎回検証・再構築・境界チェックしてから実行する
- コードモードでツール呼び出しをサンドボックスに閉じ込め、中間結果ではなく最終結果のみをモデルコンテキストに渡す

## 使いどころ

- 大量スパン/トレースに対する件数・平均・パーセンタイルなどの集計質問に答えたいAI可観測性チーム
- コーディングエージェントが自らトレースを調べてデバッグする開発ワークフロー
