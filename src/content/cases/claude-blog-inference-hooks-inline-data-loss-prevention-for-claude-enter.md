---
type: announcement
title: Claude Enterpriseの全サーフェスにインラインDLP検査を挟むinference hooks
title_original: 'Inference hooks: inline data loss prevention for Claude Enterprise'
industry: cross-industry
cloud: []
patterns:
- guardrails
- llm-gateway
- defense-in-depth
components:
- Claude Enterprise
- Claude Code
- Claude Cowork
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-enterprise-inference-hooks
published_at: '2026-08-05'
---

## 概要

Claude Enterpriseの新機能「inference hooks」は、チャット・Claude Code・Cowork・MCP経由のツール呼び出しなど全ての推論リクエストを、企業が管理するDLPサーバーに署名付きWebSocketで転送し、モデルが応答を生成する前に許可/拒否の判定を受けてから処理を進める仕組みである。これまでClaude Codeのクライアント側フックに限られていたインライン検査を、Enterpriseの全サーフェスに単一の設定で拡張する。

## 設計のポイント

- 推論の実行前にDLPサーバーの判定を待ち合わせる同期的な検査ポイントを設け、承認されない内容がモデルに渡る前にブロックする
- 既存のDLPベンダーや自前のセキュリティサーバーにそのまま接続できるよう、オープンなWebhookベースのプロトコルとスキーマを公開する
- シャドーモード(常に許可)やロールベースの除外、段階的ロールアウトを用意し、本番影響を抑えながら導入できるようにする

## 使いどころ

- 機密データが複数のAI利用経路(チャット・コーディングエージェント・ツール連携)から漏えいしないよう一元的に検査したいセキュリティ・コンプライアンスチーム
- 既存のDLP基盤をAI利用箇所にも拡張したいが、製品ごとに個別統合したくない企業
