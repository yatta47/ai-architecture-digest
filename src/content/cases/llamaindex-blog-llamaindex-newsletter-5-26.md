---
type: announcement
title: HEICネイティブ対応とGoogle Agents API連携などLlamaParseの週次アップデート
title_original: LlamaIndex Newsletter 5-26
industry: cross-industry
cloud:
- gcp
patterns:
- document-processing
- ai-agent
components:
- LlamaParse
- LiteParse
- Google Agents API
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-5-26-26
published_at: '2026-07-18'
---

## 概要

LlamaIndexの週次ニュースレターで、LlamaParseのHEICファイルネイティブ対応、Parse/Extract/Classifyジョブのレイテンシメトリクス可視化、GoogleのAgents APIサンドボックス環境へのLlamaParse/LiteParse統合テンプレートが紹介されている。あわせてSEC提出書類を引用付きで解析する財務デューデリジェンスエージェントのデモも共有された。

## 設計のポイント

- iPhone写真などのHEIC形式をJPEG変換なしで直接パースできるようにし、企業のファイル資産をそのまま扱えるようにする
- Parse/Extract/Classifyのキュー時間・処理時間・合計レイテンシを可視化し、本番運用の性能傾向を分析できるようにする

## 使いどころ

- Googleのサンドボックス化エージェント環境でドキュメント処理を自動化したい開発者
- パースジョブのレイテンシを継続的にモニタリングしたい運用チーム
