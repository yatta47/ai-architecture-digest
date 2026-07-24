---
type: announcement
title: LiteParseにgRPCサーバーを追加しサービス間連携を強化
title_original: 'Introducing liteparse-grpc: A gRPC server for LiteParse document parsing'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
components:
- LiteParse
- gRPC
- Protocol Buffers
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-liteparse-grpc-a-grpc-server-for-liteparse
published_at: '2026-07-18'
---

## 概要

LlamaIndexはRust製ドキュメント解析ライブラリLiteParseに、既存のREST APIに加えてgRPCサーバー(liteparse-grpc)を追加。Protocol Buffersによる型付き契約とバイナリフレーミングにより、サービス間連携(polyglotなバックエンド呼び出し)を高速かつ低コストにする。

## 設計のポイント

- REST(ブラウザ向けマルチパートアップロード)とgRPC(サービス間呼び出し)を用途別に使い分けるインターフェース設計
- .protoファイルをパッケージに同梱し多言語向けクライアント生成を容易にする
- Docker/npmの2通りの配布形態を用意し導入コストを下げる

## 使いどころ

- 他言語・他サービスからLiteParseの解析機能を呼び出したいバックエンド連携
- 型安全なドキュメント解析APIをマイクロサービス構成に組み込みたい場合
