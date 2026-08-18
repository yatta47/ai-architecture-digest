---
type: case
title: LlamaParseの大規模文書処理をTemporalの耐久ワークフローで支える
title_original: How LlamaIndex Uses Temporal to Scale Reliable Document Orchestration
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- event-driven
- parallel-execution
- gpu-fleet-reliability
components:
- Temporal
- RabbitMQ
- LlamaParse
outcome:
  type: reliability
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/temporal-scale-document-orchestration
published_at: '2026-08-18'
---

## 概要

LlamaIndexは130種類以上のファイル形式を解析するLlamaParseを支えるオーケストレーション基盤として、当初RabbitMQでキューイングしていたが、状態管理やフェアネス制御が自前実装のパッチワークになり技術的負債化した。耐久実行ランタイムTemporalに移行し、WorkflowとActivityで処理を宣言的に組み、Signalベースの許可証(permit)パターンでGPUプールなど共有リソースへのアクセスを排他制御することで、1日あたり数千万ページ規模の処理をBatch APIとして安定運用している。

## 設計のポイント

- キュー・ロック・リトライカウンタを自前実装する代わりに、Temporalの耐久実行状態管理に処理の再開責任を委譲する
- 子WorkflowのIDをリソース識別子にすることで、開始時の一意性チェックだけで排他ロックを実現し読み取り後書き込みのレース条件を避ける
- ParentClosePolicyやリース期限で、親Workflowの異常終了時にも許可証(permit)が自動的に解放されるようにする
- 1200ページの巨大ドキュメントのように、ページ単位で処理内容(テキスト抽出・OCR・ビジョンモデル)が異なる作業を動的に分割して割り当てる

## 使いどころ

- 1日あたり数千万ページ規模のドキュメント処理を、GPUやモデルプロバイダのレート制限を守りながら公平に捌きたい場合
- 従来のメッセージキュー(RabbitMQ等)でリトライ・フェアネス・可視性を自前実装して技術的負債化しているチーム
- 複数テナントやGPUプールなど共有リソースへの同時アクセスを、外部ロックサービス無しで安全に制御したい場合
