---
type: announcement
title: 文書解析APIをv2に刷新し新SDKを提供
title_original: Announcing New LlamaCloud SDKs and Parse API v2
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- llmops
components:
- LlamaParse
- llama-cloud SDK
- LlamaExtract
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/announcing-new-llamacloud-sdks-and-parse-api-v2
published_at: '2026-07-19'
---

## 概要

LlamaIndexが文書解析サービスLlamaParseのAPIをv2に全面刷新し、Python/TypeScript向けの新しい統合SDK「llama-cloud」を発表した。パース対象の指定に開発者の意識を向けられるよう設定を構造化オブジェクトに整理し、出力の型安全性と一貫性を高めている。

## 設計のポイント

- 「どう解析するか」ではなく「何を解析するか」に集中できるよう、パラメータをinput/output/processingの構造化オブジェクトに整理する
- expandパラメータで返却するコンテンツ(text/markdown/items/画像メタデータ)を明示的に選択できるようにする
- 旧SDK(v1)を維持しつつ新SDKをv2専用にすることで、既存ユーザーの段階的な移行を可能にする

## 使いどころ

- 大規模ドキュメント処理パイプラインを型安全なSDKで構築したい開発者
- 表・画像・スクリーンショットなど複数種類の出力を1回のパースAPI呼び出しでまとめて取得したいチーム
- 既存のv1運用を止めずに段階的にv2へ移行したい既存ユーザー
